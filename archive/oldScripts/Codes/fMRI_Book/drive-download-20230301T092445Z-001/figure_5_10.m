%illustrating effects of convolution when data are and are not upsampled


%change to your spm directory, since spm_hrf is used here
addpath /Users/jeanettemumford/Documents/Research/matlabcode/

TR=3;

%Downsampled t series are formed first 
div=30

t=(0:300)*TR/div;

hrf=spm_hrf(TR/div);

stim_1s=zeros(size(t));
stim_1s(t>=0 & t<1)=1;
stim_1s=conv(stim_1s, hrf);
stim_1s=stim_1s(1:length(t));
stim_1s_down=stim_1s(1:div:length(t));

stim_2s=zeros(size(t));
stim_2s(t>=0 & t<2)=1;
stim_2s=conv(stim_2s, hrf);
stim_2s=stim_2s(1:length(t));
stim_2s_down=stim_2s(1:div:length(t));

stim_2_1s=zeros(size(t));
stim_2_1s((t>=0 & t<1) | (t>=1.5 & t<2.5))=1;
stim_2_1s=conv(stim_2_1s, hrf);
stim_2_1s=stim_2_1s(1:length(t));
stim_2_1s_down=stim_2_1s(1:div:length(t));

stim_3s=zeros(size(t));
stim_3s(t>=0 & t<3)=1;
stim_3s=conv(stim_3s, hrf);
stim_3s=stim_3s(1:length(t));
stim_3s_down=stim_3s(1:div:length(t));

stim_1s_delay_2s=zeros(size(t));
stim_1s_delay_2s(t>=2 & t<3)=1;
stim_1s_delay_2s=conv(stim_1s_delay_2s, hrf);
stim_1s_delay_2s=stim_1s_delay_2s(1:length(t));
stim_1s_delay_2s_down=stim_1s_delay_2s(1:div:length(t));


%create curve that is convolved in time resolution of TR
t_down=t(1:div:length(t));

stim_condown=zeros(size(t_down));
stim_condown(1)=1;
stim_condown=conv(stim_condown, spm_hrf(3));
stim_condown=stim_condown(1:length(t_down));


subplot(1,2,1)
plot(t, stim_1s, 'blue-', 'linewidth', 2)
hold on
plot(t, stim_2s, 'red-', 'linewidth', 2)
plot(t, stim_3s, 'yellow-', 'linewidth', 2)
plot(t, stim_1s_delay_2s, 'cyan', 'linewidth', 2)
hold off
hleg=legend('0s-1s','0s-2s', '0s-3s','2s-3s');
set(hleg, 'fontsize', 8)
title('Time resolution=0.1s')
xlabel('Time(s)')
axis([0 27 -0.1 0.6])


subplot(1,2,2)
plot(t_down, stim_condown, 'black--', 'linewidth', 2)
hold on
plot(t_down, stim_1s_down, 'blue-', 'linewidth', 2)
plot(t_down, stim_2s_down, 'red-', 'linewidth', 2)
plot(t_down, stim_3s_down, 'yellow-', 'linewidth', 2)
plot(t_down, stim_1s_delay_2s_down, 'cyan', 'linewidth', 2)
hold off
axis([0 27 -0.1 0.6])
xlabel('Time(s)')
hleg=legend('Convolved in 3s res');
set(hleg, 'fontsize', 8)
title('Time resolution=3s')





