% ============================================== %
% Comparison Crushers et non crushers
% G. Collewet / S. Moussaoui for B.Prigent
% v 2, 19-Jun-2024
% ============================================== %
%{
Try different values of crushers to identify a difference
%}

clear;
clc;

%% 1- Variables

% nom du répertoire où se situent les fichiers fonction .p
path_functions = 'C:\Users\bprigent\Documents\MATLAB\PRISM\pFilePRISM\';
bet= 0;
del= 0;
dataPath = 'C:\Users\bprigent\MyDatas\RECONDCM\';
resultPath = 'C:\Users\bprigent\MyResults\PRISM\';
listFolder = dir(strcat(dataPath,'*'));

%nom du fichier representant le masque  (format png ok)
nom_masque="C:\Users\bprigent\MyDatas\RECONDCMMask.png";

%nombre d'iterations maximal
NB_ITER_MAX=200;

Nc=3;  %nombre de composantes
A0=[0.2 0.5 0.3]; %valeurs initiales en proportion
T2=[40 100 2000]; % valeurs initiales en ms

bruit=22/sqrt(pi/2); % moyenne du fond divisée par sqrt(pi/2);

%parametres de regularisation

p=genpath(path_functions);
addpath(p,'-begin');

%% 2- Computation

for crushersProfile=listFolder
    % nom du repertoire où se situent les images dcm
    rep_dcm=strcat(dataPath,crushersProfile);

    %nom du repertoire resultat
    rep_res=strcat(resultPath,crushersProfile);

    %nom racine des fichiers resultats
    nom_res=crushersProfile; 
    
    fonction_estimation(rep_dcm,rep_res,nom_res,Nc,A0,T2,nom_masque,bet,del,bruit,NB_ITER_MAX);
    clear rep_dcm rep_res nom_res
end