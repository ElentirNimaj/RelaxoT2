% Session se_imanes

% Set-up/choose the design
design.name = 'd01_try'; 
% Bloc design Motor, 27s baseline, and 6 cycles of 18s motor, 27s rest)
% Bloc design Breathhold, 45s baseline, and 6 cycles of 18s breathhold (breathing in 2s before end of rest), 45s rest)
design.sessions = {'se_ge','se_reco','se_ra'};
%design.conditions = {{'motor'},{'breathhold'}};       %1}};
design.conditions = {{'encoTask','encoCorrect','encoIncorrect','encoControl'},{'recoControl','recoCorrect','recoIncorrect','recoNew','recoOld'},{'recall','recallBase'}};       %1}};

design.movement = true;
design.factorial = false; %not a factorial design
design.factors = {}; % no factors then
design.factorLevels = [];
design.allSessionsTogether = 1;

% Onsets

% 
% %rest_onsets = [0 40 80 120 160 200 240 280];
% %breathhold_onsets = [45 108 171 234 297 360];
% %breathhold_onsets = [27 135 243 351];
% %rest_onsets = [0 45 90 135 180 225 270];
% 
% design.onsets = {...
%     {enco_control,enco_correct,enco_incorrect,enco_task},...
%     {reco_control,reco_correct,reco_incorrect,reco_new,reco_old},...
%     {recall,recall_base}
%     };

%design.onsets = {...
    %{breathhold_onsets},...
    %{breathhold_onsets},...
    %};
%    {breathhold_onsets},...
%design.durations = {{18}};
design.durations = {{5,5,5,5},{2.5,2.5,2.5,2.5,2.5},{5,2.5}};

design.units = 'secs'; 
design.realign_rp_cov = true; 
design.repeat_contrast_sess = false;

% GLM parameters
design.deriv.time = 1;
design.deriv.dispersion = 0;

% Explicit mask
design.useExplicitMask = true;
design.explicitMask = 'C:\Users\vseptier\Documents\Stage\Data\monProjetGE2REC\pre-processing\gr_control\su_01\structural\mask0.5_c1T13D_mprage_sag_p2_iso_verio_20211215000000_5_c1c2c3.nii.gz';

% Define contrasts, weights concern regressors only
% Main contrasts
%c{1} = struct('number', 1,'weights',[1],'name','breathhold'); % breathhold Task
%c{2} = struct('number', 1,'weights',[0 1],'name','breathhold'); % Breathhold Task
%c{1} = struct('number',1,'weights',[ 1 0 0 -1 0 0 0 0 0 0 0 ], 'name','encoTask−encoControl');
c{1} = struct('number',1,'weights',[ 0 1 -1 0 0 0 0 0 0 0 0 ], 'name','encoCorrect−encoIncorrect');
c{2} = struct('number',2,'weights',[ 0 0 0 0 0 1 -1 0 0 0 0 ], 'name','recoCorrect−recoIncorrect');
c{3} = struct('number',3,'weights',[ 0 0 0 0 0 0 0 -1 1 0 0 ], 'name','recoOld−recoNew');
c{4} = struct('number',4,'weights',[ 0 0 0 0 0 0 0 1 -1 0 0 ], 'name','recoNew−recoOld');
%c{6} = struct('number',6,'weights',[ 0 0 0 0 0 0 0 0 0 1 -1 ], 'name','recall−recallBase');
%c{7} = struct('number',7,'weights',[ -1 0 0 0 0 0 0 0 0 1 0 ], 'name','recall−encoTask');

design.contrasts = c;