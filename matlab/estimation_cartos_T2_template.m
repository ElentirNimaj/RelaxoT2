% nom du r�pertoire o� se situent les fichiers fonction .p
path_functions = 'C:\Users\bprigent\Documents\MATLAB\PRISM\pFilePRISM\';

% nom du repertoire o� se situent les images dcm
rep_dcm='C:\Users\bprigent\MyDatas\TestFolder\C0PIDCM\';

%nom du repertoire resultat
rep_res='C:\Users\bprigent\MyDatas\TestFolder\'; 

%nom racine des fichiers resultats
nom_res='ProcessPRISM'; 

%nom du fichier representant le masque  (format png ok)
nom_masque="C:\Users\bprigent\MyDatas\ReconMask.png";

%nombre d'iterations maximal
NB_ITER_MAX=200;

Nc=3;  %nombre de composantes
A0=[0.2 0.5 0.3]; %valeurs initiales en proportion
T2=[40 100 2000]; % valeurs initiales en ms

bruit=22/sqrt(pi/2); % moyenne du fond divis�e par sqrt(pi/2);

%parametres de regularisation
bet=1.5;
del=250 ;

p=genpath(path_functions);
addpath(p,'-begin');
fonction_estimation(rep_dcm,rep_res,nom_res,Nc,A0,T2,nom_masque,bet,del,bruit,NB_ITER_MAX);
