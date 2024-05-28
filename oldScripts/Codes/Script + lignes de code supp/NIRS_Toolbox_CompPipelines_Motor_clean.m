
function NIRS_Toolbox_CompPipelines_Motor_clean(myDataFolder, threshSNR)

%% Specify Working directory and load nirs file

%This is just to open the browser in the path where the script is
% [path,~,~] = fileparts(matlab.desktop.editor.getActiveFilename);
[MyDataFolder]=uigetdir(path,'Select NIRx Data Folder');
raw = nirs.io.loadDirectory(MyDataFolder,{'subject','session'});

%% Create demographics
Demographics=nirs.createDemographicsTable(raw);

% Comments Elise - Training session with Hector July 22nd 2020 : 
%raw.draw % shows the timeseries for all channels, the first trigger from the
%MRI (blue) and then the markers (orange), close, raw.draw(1:2) to display
%channels 1 for both wavelength, 3:4 : channel 2 for both wavelength...see raw.probe.link 
% After conversion to HbR and Hb0, raw 1: Hb0 channel 1, raw 2 : HbR
% channel 1

% nirs.viz.nirsviewer to view the data, the layout and chose the channels
% to view. Analysis module not used by Hector. 
% triggers/markers have no durations -> stim_dur gives the durations
% (channel/condition 1 and channel/condition 2) - only 2 first are useful
% here but in case of processing with nirslab extra names are added to the
% stimulus (duplicates) and saves it in the stimulation information in the
% raw data

%% Edit stimulus duration (event mode)
stim_dur = [0 0 18]; %array with duration of each condition in seconds (PAY ATTENTION TO THE ORDER!!)
                      % Got it! It's alphabetical order!            
raw_edit = nirs.design.change_stimulus_duration(raw, [], stim_dur); 

%% Change Condtions Names
% Changing the names should be done after setting the time durations;
% otherwhise, we run the risk of mismatching each stimulus and the
% corresponding duration, since the stimuli field is sorted in alphabetical
% order
job = nirs.modules.RenameStims();
job.listOfChanges = { ...
    
    'channel_2',     'Baseline';
    'channel_3',     'Motor';
      };
raw_edit=job.run(raw_edit);

%% Remove unuseful markers (since they're not necessary for the processing)
discStim = 1;
if discStim
    job = nirs.modules.DiscardStims();
    job.listOfStims = {'channel_1','Intro','channel_99'};
    raw_edit = job.run(raw_edit);
end

%% Trim baseline (step  to remove excessive baseline at the beginning or end of the files, suggested by Johnathan Perry in
%%https://www.youtube.com/watch?v=u55Qd1pNnc8&list=PLU3kfSR019bnRzM3QUZWPOBNc_LExgStl)
trimflag = 1;
if trimflag
    job = nirs.modules.TrimBaseline();
    job.preBaseline = 10;        % Time (seconds) before beginning of first trigger
    job.postBaseline = 50;       % Time (seconds) after end of last trigger
    raw_trim = job.run(raw_edit);
else
    raw_trim = raw_edit;
end

%% Discard channels with low SNR (SNR = - mean intensity of each channel divided by the SD 
%  of the same channel --> SNR < 8 : very noisy - do not contain useful information si threshold > 8 
%  --> sometimes discard good channels (with useful information). [Novi20]
[nbTimePoints nbChannels] = size(raw_trim.data);
raw_SNR = mean(raw_trim.data) ./ std(raw_trim.data);
excluded_channels = raw_trim.probe.link(find(raw_SNR < threshSNR), :);
writetable(excluded_channels, 'excluded_channels.txt','Delimiter',' ')  
type 'excluded_channels.txt'


%% Pipelines

% Our pipeline
job_ours = nirs.modules.OpticalDensity;
job_ours = nirs.modules.WaveletFilter3(job_ours);
job_ours.sthresh = 0.005;            % std dev to define outliers
job_ours.removeScaling = false;
job_ours = eeg.modules.BandPassFilter(job_ours);
job_ours.lowpass = .09;
job_ours.highpass = 0.01;
job_ours.do_downsample = false;
job_ours = nirs.modules.BeerLambertLaw(job_ours);% it uses PPF = 0.1 (5/50)
job_ours.PPF = [6 7];
job_ours = nirs.modules.AR_IRLS(job_ours);
job_ours.verbose = true;
job_ours.basis = Dictionary();
job_ours.basis('default') = nirs.design.basis.Canonical();

job_def = job_ours;
SubjStats=job_def.run(raw_trim);

SubjStats.draw('tstat',[],'q<5e^-2');
hold off

%% Same pipeline as before, but without resampling, to compute block averages

SSD = 0; % No short channels
    fprintf('SSD off\n');
    job_BA=nirs.modules.OpticalDensity;
    job_BA=nirs.modules.Run_HOMER2(job_BA);
    job_BA.fcn='hmrMotionCorrectPCArecurse';
    job_BA.vars.tMotion=0.5;
    job_BA.vars.tMask=1.;
    job_BA.vars.std_thresh=10;
    job_BA.vars.amp_thresh=5;
    job_BA.vars.nSV=0.97;
    job_BA.vars.maxIter=5;
    job_BA=nirs.modules.BeerLambertLaw(job_BA);
    job_BA.PPF = [6 7];
    job_BA = nirs.modules.WaveletFilter3(job_BA);
     job_BA.sthresh = 0.005;            % std dev to define outliers
     job_BA.removeScaling = false;
    job_BA = eeg.modules.BandPassFilter(job_BA);
    job_BA.lowpass = .09;
    job_BA.highpass = 0.01;
    job_BA.do_downsample = false;
    hb = job_BA.run(raw_trim);


% Compute Block Averages (uses Homer2) 
stim_arr = zeros(length(hb.time),hb.stimulus.count);
for s=1:hb.stimulus.count
    [~,idxs] = ismembertol(hb.stimulus.values{1,s}.onset,hb.time,2.5*10^-4);
    stim_arr(idxs,s) = 1;
    trange = [-5 45];
    [BlockAVG2(s).data,BlockAVG2(s).stdBA,BlockAVG2(s).time] = hmrBlockAvg(hb.data,stim_arr(:,s),hb.time,trange);
end

% Plot - only Hb channels
for s=1:hb.stimulus.count%1:1%2:2%1:hb.stimulus.count    %Loop through the markers that are going to create de block averages plots
    maxv = max(max(abs(BlockAVG2(s).data)));   %Vertical limits of the plots
    hbchan = size(BlockAVG2(s).data,2)/2;    % Split into hbo and hbr channels
    for i=1:hbchan
        figure;
        %HbO channels
        p1 = fill([BlockAVG2(s).time';flipud(BlockAVG2(s).time')],[BlockAVG2(s).data(:,2*i-1)-BlockAVG2(s).stdBA(:,2*i-1);flipud(BlockAVG2(s).data(:,2*i-1)+BlockAVG2(s).stdBA(:,2*i-1))],'r','FaceAlpha',.1,'LineStyle','None');
        p2 = line(BlockAVG2(s).time',BlockAVG2(s).data(:,2*i-1),'LineWidth',2,'Color','r');
        hold on
        %HbR channels
        p3 = fill([BlockAVG2(s).time';flipud(BlockAVG2(s).time')],[BlockAVG2(s).data(:,2*i)-BlockAVG2(s).stdBA(:,2*i);flipud(BlockAVG2(s).data(:,2*i)+BlockAVG2(s).stdBA(:,2*i))],'b','FaceAlpha',.1,'LineStyle','None');
        p4 = line(BlockAVG2(s).time',BlockAVG2(s).data(:,2*i),'LineWidth',2,'Color','b');
        %HbT
        %fill([BlockAVG2(s).time';flipud(BlockAVG2(s).time')],[HbT(:,i)-HbTstd(:,i);flipud(HbT(:,i)+HbTstd(:,i))],'y','FaceAlpha',.1,'LineStyle','None');
        %line(BlockAVG2(s).time',HbT(:,i),'Color','y','r','LineWidth',2);

        title(['Cond: ', num2str(hb.stimulus.values{1,s}.name), ' -- Source ' , num2str(hb.probe.link{2*i,1}), ' - Detector ', num2str(hb.probe.link{2*i,2})]);
        grid on
        xlabel('Time [s]');
        ylabel('Conc. changes [10^-^3 mMol]');
        ylim([-maxv maxv]);
        y2 = [-maxv maxv];
        x1 = trange;

        %Beginning and end of triggers
        p5 = line([0 0],y2,'LineWidth',2,'Color',[0 1 0]);
        p6 = line([18 18],y2,'LineWidth',2,'Color',[0 1 0]);

        %Zero level
        p7 = line(trange,[0 0], 'LineWidth',2,'Color',[0 0 0]);

        %Removing vertical and horizontal lines from legend
        set(get(get(p1,'Annotation'),'LegendInformation'),'IconDisplayStyle','off');
        set(get(get(p3,'Annotation'),'LegendInformation'),'IconDisplayStyle','off');
        set(get(get(p5,'Annotation'),'LegendInformation'),'IconDisplayStyle','off');
        set(get(get(p6,'Annotation'),'LegendInformation'),'IconDisplayStyle','off');
        set(get(get(p7,'Annotation'),'LegendInformation'),'IconDisplayStyle','off');
        legend('HbO','HbR');
        hold off
        %Save results and close figures
        saveas(p1, ['s',num2str(hb.probe.link{2*i,1}),'d',num2str(hb.probe.link{2*i,2}),'.png']);
        close();
    end
end
% End of plot for block averages 

% Plot raw signal time series
plot(raw_trim.time,raw_trim.data,'LineWidth',1.5);
title(['Raw signal time series']);
grid on
xlabel('Time [s]');
ylabel('Amplitude [V]');
yl = ylim;
hold on
for hh=1:length(raw_trim.stimulus.values{1,1}.onset) % adapt second index to number of markers (2 before for the intro marker, which we removed, only task marker left)
    rectangle('Position',[raw_trim.stimulus.values{1,1}.onset(hh) yl(1) raw_trim.stimulus.values{1,1}.dur(1) (yl(2)-yl(1))],'FaceColor',[0.2000 0.8000 0 0.3],'LineStyle','none');
end
hold off

% Plot average HbO and HbR time series to check baseline previous to tasks
meanHbO = mean(hb.data(:,1:2:end),2);
meanHbR = mean(hb.data(:,2:2:end),2);
plot(raw_trim.time,meanHbO,'LineWidth',1.5);
hold on
plot(raw_trim.time,meanHbR,'LineWidth',1.5);
title(['Mean HbX time series']);
grid on
xlabel('Time [s]');
ylabel('Conc. change [10^-^3 mMol]');
yl = ylim;
legend('HbO','HbR')
for hh=1:length(raw_trim.stimulus.values{1,1}.onset)
    rectangle('Position',[raw_trim.stimulus.values{1,1}.onset(hh) yl(1) raw_trim.stimulus.values{1,1}.dur(1) (yl(2)-yl(1))],'FaceColor',[0.2000 0.8000 0 0.3],'LineStyle','none');
end
hold off
end