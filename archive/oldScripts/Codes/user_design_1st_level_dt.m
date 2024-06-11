% ============================================== %
% First level analysis Anticipation and Reward
% Q. Duche for B.Prigent
% v 4, 13-Apr-2023
% ============================================== %

%% Anticipation and Reward

%{
   Block to make first level analysis for anticipation AND reward with multiple contrast.
%}

% Set-up/choose the design
design.name = 'd02_AnticipationAndReward_dt';
design.sessions = {'se_mid'};
design.conditions = {{'AntFoodHigh', 'AntFoodLow', 'AntFoodNo',...
                      'AntMoneyHigh', 'AntMoneyLow', 'AntMoneyNo',...
                      'RewFoodHigh','RewFoodLow','RewFoodNo',...
                      'RewMoneyHigh','RewMoneyLow','RewMoneyNo',...
                      'RewFoodNo30Percent','RewMoneyNo30Percent'}};


% Define contrasts, weights concern regressors only
c{1} = struct('number', 1,'weights',[1 0 0 0 0 0 0 0 0 0 0 0 0 0],'name','dt_Ant_Food_High');
c{2} = struct('number', 2,'weights',[0 0 1 0 0 0 0 0 0 0 0 0 0 0],'name','dt_Ant_Food_No');
c{3} = struct('number', 3,'weights',[0 0 0 1 0 0 0 0 0 0 0 0 0 0],'name','dt_Ant_Money_High');
c{4} = struct('number', 4,'weights',[0 0 0 0 0 1 0 0 0 0 0 0 0 0],'name','dt_Ant_Money_No');

c{5} = struct('number', 5,'weights',[1 0 -1 0 0 0 0 0 0 0 0 0 0 0],'name','dt_Ant_Food_HighvsNo');
c{6} = struct('number', 6,'weights',[0 0 0 1 0 -1 0 0 0 0 0 0 0 0],'name','dt_Ant_Money_HighvsNo');

c{7} = struct('number', 7,'weights',[0 0 0 0 0 0 1 0 0 0 0 0 0 0],'name','dt_Rew_Food_High');
c{8} = struct('number', 8,'weights',[0 0 0 0 0 0 0 0 1 0 0 0 0 0],'name','dt_Rew_Food_No');
c{9} = struct('number', 9,'weights',[0 0 0 0 0 0 0 0 0 1 0 0 0 0],'name','dt_Rew_Money_High');
c{10} = struct('number', 10,'weights',[0 0 0 0 0 0 0 0 0 0 0 1 0 0],'name','dt_Rew_Money_No');

c{11} = struct('number', 11,'weights',[0 0 0 0 0 0 1 0 -1 0 0 0 0 0],'name','dt_Rew_Food_HighvsNo');
c{12} = struct('number', 12,'weights',[0 0 0 0 0 0 0 0 0 1 0 -1 0 0],'name','dt_Rew_Money_HighvsNo');

c{13} = struct('number', 13,'weights',[1 0 0 1 0 0 0 0 0 0 0 0 0 0],'name','dt_Ant_FoodAndMoney_High');
c{14} = struct('number', 14,'weights',[1 0 -1 1 0 -1 0 0 0 0 0 0 0 0],'name','dt_Ant_FoodAndMoney_HighvsNo');
c{15} = struct('number', 15,'weights',[0 0 0 0 0 0 1 0 0 1 0 0 0 0],'name','dt_Rew_FoodAndMoney_High');
c{16} = struct('number', 16,'weights',[0 0 0 0 0 0 1 0 -1 1 0 -1 0 0],'name','dt_Rew_FoodAndMoney_HighvsNo');

c{17} = struct('number', 17,'weights',[1 0 0 -1 0 0 0 0 0 0 0 0 0 0],'name','dt_Ant_FoodvsMoney_High');
c{18} = struct('number', 18,'weights',[0 0 0 0 0 0 1 0 0 -1 0 0 0 0],'name','dt_Rew_FoodvsMoney_High');

design.movement = true;
design.factorial = false; %not a factorial design
design.factors = {}; % no factors then
design.factorLevels = [];
design.allSessionsTogether = true;

% Onsets
   % Onsets provide by the files with Autofmri

% Design duration for each condition
design.durations = {{3.7, 3.7, 3.7,...
                     3.7, 3.7, 3.7,...
                     1.5, 1.5, 1.5,...
                     1.5, 1.5, 1.5,...
                     1.5, 1.5}};

% GLM parameters
design.deriv_time = true;
design.deriv_dispersion = false;

% Explicit mask
design.use_explicit_mask = true;
design.explicit_mask = 'C:/Users/bprigent/Documents/MIDFID/Experiment/mask/rmask20_no_eyeballs.nii';
design.mthresh = 0.0;
design.contrasts = c;


