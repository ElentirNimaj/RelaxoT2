% ============================================== %
% Comparison Beta and delta
% G. Collewet / S. Moussaoui for B.Prigent
% v 1, 17-Jun-2024
% ============================================== %
%{
Try different value for processing of RECON images, beta = 0.4, 1.5, 3, 6
and delta = 7, 65 ,125, 250, 500, 1800
%}

clear;
clc;

%% 1- C2PIHP Beta = 0.4 Delta =  7 

% nom du répertoire où se situent les fichiers fonction .p
path_functions = 'C:\Users\bprigent\Documents\MATLAB\PRISM\pFilePRISM\';

% nom du repertoire où se situent les images dcm
rep_dcm='C:\Users\bprigent\MyDatas\RECONDCM\C2PIHP';

%nom du repertoire resultat
rep_res='C:\Users\bprigent\MyResults\PRISM\C2PIHP\ComparaisonBtaDel\bta0_4_dlta7'; 

try
    mkdir(rep_res)
catch FileExistsError
    warning('Folder already exists')
end

%nom racine des fichiers resultats
nom_res='C2PIHP_bta0_4_dlta7'; 

%nom du fichier representant le masque  (format png ok)
nom_masque='C:\Users\bprigent\MyDatas\RECONMask.png';

%nombre d'iterations maximal
NB_ITER_MAX=200;

Nc=3;  %nombre de composantes
A0=[0.2 0.5 0.3]; %valeurs initiales en proportion
T2=[15 70 2000]; % valeurs initiales en ms

bruit=22/sqrt(pi/2); % moyenne du fond divisée par sqrt(pi/2);

%parametres de regularisation
bet=0.4;
del=7 ;

p=genpath(path_functions);
addpath(p,'-begin');
fonction_estimation(rep_dcm,rep_res,nom_res,Nc,A0,T2,nom_masque,bet,del,bruit,NB_ITER_MAX);

%% 2- C2PIHP Beta = 1.5 Delta =  250

clear;

% nom du répertoire où se situent les fichiers fonction .p
path_functions = 'C:\Users\bprigent\Documents\MATLAB\PRISM\pFilePRISM\';

% nom du repertoire où se situent les images dcm
rep_dcm='C:\Users\bprigent\MyDatas\RECONDCM\C2PIHP';

%nom du repertoire resultat
rep_res='C:\Users\bprigent\MyResults\PRISM\C2PIHP\ComparaisonBtaDel\bta1_5_dlta250'; 

try
    mkdir(rep_res)
catch FileExistsError
    warning('Folder already exists')
end

%nom racine des fichiers resultats
nom_res='C2PIHP_bta1_5_dlta250'; 

%nom du fichier representant le masque  (format png ok)
nom_masque='C:\Users\bprigent\MyDatas\RECONMask.png';

%nombre d'iterations maximal
NB_ITER_MAX=200;

Nc=3;  %nombre de composantes
A0=[0.2 0.5 0.3]; %valeurs initiales en proportion
T2=[15 70 1800]; % valeurs initiales en ms

bruit=22/sqrt(pi/2); % moyenne du fond divisée par sqrt(pi/2);

%parametres de regularisation
bet=1.5;
del=250 ;

p=genpath(path_functions);
addpath(p,'-begin');
fonction_estimation(rep_dcm,rep_res,nom_res,Nc,A0,T2,nom_masque,bet,del,bruit,NB_ITER_MAX);

%% 3- C2PIHP Beta = 3 Delta =  500

clear;

% nom du répertoire où se situent les fichiers fonction .p
path_functions = 'C:\Users\bprigent\Documents\MATLAB\PRISM\pFilePRISM\';

% nom du repertoire où se situent les images dcm
rep_dcm='C:\Users\bprigent\MyDatas\RECONDCM\C2PIHP';

%nom du repertoire resultat
rep_res='C:\Users\bprigent\MyResults\PRISM\C2PIHP\ComparaisonBtaDel\bta3_dlta500'; 

try
    mkdir(rep_res)
catch FileExistsError
    warning('Folder already exists')
end

%nom racine des fichiers resultats
nom_res='C2PIHP_bta3_dlta500'; 

%nom du fichier representant le masque  (format png ok)
nom_masque='C:\Users\bprigent\MyDatas\RECONMask.png';

%nombre d'iterations maximal
NB_ITER_MAX=200;

Nc=3;  %nombre de composantes
A0=[0.2 0.5 0.3]; %valeurs initiales en proportion
T2=[15 70 1800]; % valeurs initiales en ms

bruit=22/sqrt(pi/2); % moyenne du fond divisée par sqrt(pi/2);

%parametres de regularisation
bet=3;
del=500 ;

p=genpath(path_functions);
addpath(p,'-begin');
fonction_estimation(rep_dcm,rep_res,nom_res,Nc,A0,T2,nom_masque,bet,del,bruit,NB_ITER_MAX);

%% 4- C2PIHP Beta = 6 Delta =  1000
clear;

% nom du répertoire où se situent les fichiers fonction .p
path_functions = 'C:\Users\bprigent\Documents\MATLAB\PRISM\pFilePRISM\';

% nom du repertoire où se situent les images dcm
rep_dcm='C:\Users\bprigent\MyDatas\RECONDCM\C2PIHP';

%nom du repertoire resultat
rep_res='C:\Users\bprigent\MyResults\PRISM\C2PIHP\ComparaisonBtaDel\bta6_dlta1000'; 

try
    mkdir(rep_res)
catch FileExistsError
    warning('Folder already exists')
end

%nom racine des fichiers resultats
nom_res='C2PIHP_bta6_dlta1000'; 

%nom du fichier representant le masque  (format png ok)
nom_masque='C:\Users\bprigent\MyDatas\RECONMask.png';

%nombre d'iterations maximal
NB_ITER_MAX=200;

Nc=3;  %nombre de composantes
A0=[0.2 0.5 0.3]; %valeurs initiales en proportion
T2=[15 70 1800]; % valeurs initiales en ms

bruit=22/sqrt(pi/2); % moyenne du fond divisée par sqrt(pi/2);

%parametres de regularisation
bet=6;
del=1000 ;

p=genpath(path_functions);
addpath(p,'-begin');
fonction_estimation(rep_dcm,rep_res,nom_res,Nc,A0,T2,nom_masque,bet,del,bruit,NB_ITER_MAX);

%% 5- C2PIHP Beta = 3 Delta =  250
clear;

% nom du répertoire où se situent les fichiers fonction .p
path_functions = 'C:\Users\bprigent\Documents\MATLAB\PRISM\pFilePRISM\';

% nom du repertoire où se situent les images dcm
rep_dcm='C:\Users\bprigent\MyDatas\RECONDCM\C2PIHP';

%nom du repertoire resultat
rep_res='C:\Users\bprigent\MyResults\PRISM\C2PIHP\ComparaisonBtaDel\bta3_dlta250'; 

try
    mkdir(rep_res)
catch FileExistsError
    warning('Folder already exists')
end

%nom racine des fichiers resultats
nom_res='C2PIHP_bta3_dlta250'; 

%nom du fichier representant le masque  (format png ok)
nom_masque='C:\Users\bprigent\MyDatas\RECONMask.png';

%nombre d'iterations maximal
NB_ITER_MAX=200;

Nc=3;  %nombre de composantes
A0=[0.2 0.5 0.3]; %valeurs initiales en proportion
T2=[15 70 1800]; % valeurs initiales en ms

bruit=22/sqrt(pi/2); % moyenne du fond divisée par sqrt(pi/2);

%parametres de regularisation
bet=3;
del=250 ;

p=genpath(path_functions);
addpath(p,'-begin');
fonction_estimation(rep_dcm,rep_res,nom_res,Nc,A0,T2,nom_masque,bet,del,bruit,NB_ITER_MAX);

%% 6- C2PIHP Beta = 1.5 Delta =  500
clear;

% nom du répertoire où se situent les fichiers fonction .p
path_functions = 'C:\Users\bprigent\Documents\MATLAB\PRISM\pFilePRISM\';

% nom du repertoire où se situent les images dcm
rep_dcm='C:\Users\bprigent\MyDatas\RECONDCM\C2PIHP';

%nom du repertoire resultat
rep_res='C:\Users\bprigent\MyResults\PRISM\C2PIHP\ComparaisonBtaDel\bta1_5_dlta500'; 

try
    mkdir(rep_res)
catch FileExistsError
    warning('Folder already exists')
end

%nom racine des fichiers resultats
nom_res='C2PIHP_bta1_5_dlta500'; 

%nom du fichier representant le masque  (format png ok)
nom_masque='C:\Users\bprigent\MyDatas\RECONMask.png';

%nombre d'iterations maximal
NB_ITER_MAX=200;

Nc=3;  %nombre de composantes
A0=[0.2 0.5 0.3]; %valeurs initiales en proportion
T2=[15 70 1800]; % valeurs initiales en ms

bruit=22/sqrt(pi/2); % moyenne du fond divisée par sqrt(pi/2);

%parametres de regularisation
bet=1.5;
del=500 ;

p=genpath(path_functions);
addpath(p,'-begin');
fonction_estimation(rep_dcm,rep_res,nom_res,Nc,A0,T2,nom_masque,bet,del,bruit,NB_ITER_MAX);

%% 7- C2PIHP Beta = 1.5 Delta =  125
clear;

% nom du répertoire où se situent les fichiers fonction .p
path_functions = 'C:\Users\bprigent\Documents\MATLAB\PRISM\pFilePRISM\';

% nom du repertoire où se situent les images dcm
rep_dcm='C:\Users\bprigent\MyDatas\RECONDCM\C2PIHP';

%nom du repertoire resultat
rep_res='C:\Users\bprigent\MyResults\PRISM\C2PIHP\ComparaisonBtaDel\bta1_5_dlta125'; 

try
    mkdir(rep_res)
catch FileExistsError
    warning('Folder already exists')
end

%nom racine des fichiers resultats
nom_res='C2PIHP_bta1_5_dlta125'; 

%nom du fichier representant le masque  (format png ok)
nom_masque='C:\Users\bprigent\MyDatas\RECONMask.png';

%nombre d'iterations maximal
NB_ITER_MAX=200;

Nc=3;  %nombre de composantes
A0=[0.2 0.5 0.3]; %valeurs initiales en proportion
T2=[15 70 1800]; % valeurs initiales en ms

bruit=22/sqrt(pi/2); % moyenne du fond divisée par sqrt(pi/2);

%parametres de regularisation
bet=1.5;
del=125 ;

p=genpath(path_functions);
addpath(p,'-begin');
fonction_estimation(rep_dcm,rep_res,nom_res,Nc,A0,T2,nom_masque,bet,del,bruit,NB_ITER_MAX);

%% 8- C2PIHP Beta = 6 Delta =  250
clear;

% nom du répertoire où se situent les fichiers fonction .p
path_functions = 'C:\Users\bprigent\Documents\MATLAB\PRISM\pFilePRISM\';

% nom du repertoire où se situent les images dcm
rep_dcm='C:\Users\bprigent\MyDatas\RECONDCM\C2PIHP';

%nom du repertoire resultat
rep_res='C:\Users\bprigent\MyResults\PRISM\C2PIHP\ComparaisonBtaDel\bta6_dlta250'; 

try
    mkdir(rep_res)
catch FileExistsError
    warning('Folder already exists')
end

%nom racine des fichiers resultats
nom_res='C2PIHP_bta6_dlta250'; 

%nom du fichier representant le masque  (format png ok)
nom_masque='C:\Users\bprigent\MyDatas\RECONMask.png';

%nombre d'iterations maximal
NB_ITER_MAX=200;

Nc=3;  %nombre de composantes
A0=[0.2 0.5 0.3]; %valeurs initiales en proportion
T2=[15 70 1800]; % valeurs initiales en ms

bruit=22/sqrt(pi/2); % moyenne du fond divisée par sqrt(pi/2);

%parametres de regularisation
bet=6;
del=250 ;

p=genpath(path_functions);
addpath(p,'-begin');
fonction_estimation(rep_dcm,rep_res,nom_res,Nc,A0,T2,nom_masque,bet,del,bruit,NB_ITER_MAX);

%% 9- C2PIHP Beta = 0 Delta = 0
clear;

% nom du répertoire où se situent les fichiers fonction .p
path_functions = 'C:\Users\bprigent\Documents\MATLAB\PRISM\pFilePRISM\';

% nom du repertoire où se situent les images dcm
rep_dcm='C:\Users\bprigent\MyDatas\RECONDCM\C2PIHP';

%nom du repertoire resultat
rep_res='C:\Users\bprigent\MyResults\PRISM\C2PIHP\ComparaisonBtaDel\bta0_dlta0'; 

try
    mkdir(rep_res)
catch FileExistsError
    warning('Folder already exists')
end

%nom racine des fichiers resultats
nom_res='C2PIHP_bta0_dlta0'; 

%nom du fichier representant le masque  (format png ok)
nom_masque='C:\Users\bprigent\MyDatas\RECONMask.png';

%nombre d'iterations maximal
NB_ITER_MAX=200;

Nc=3;  %nombre de composantes
A0=[0.2 0.5 0.3]; %valeurs initiales en proportion
T2=[15 70 1800]; % valeurs initiales en ms

bruit=22/sqrt(pi/2); % moyenne du fond divisée par sqrt(pi/2);

%parametres de regularisation
bet=0;
del=0 ;

p=genpath(path_functions);
addpath(p,'-begin');
fonction_estimation(rep_dcm,rep_res,nom_res,Nc,A0,T2,nom_masque,bet,del,bruit,NB_ITER_MAX);
