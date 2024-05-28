% nom du répertoire où se situent les fichiers fonction .p
path_functions = 'C:\Users\bprigent\MyScript\matlab\pFilePRISM\';

% nom du repertoire où se situent les images dcm
rep_dcm='C:\Users\bprigent\Datas\testFolder\Shanoir-download_1ds_22-05-2024_15h1549\C2PI\';

%nom du repertoire resultat
rep_res='C:\Users\bprigent\Resultats\carteMatlab\'; 

%nom racine des fichiers resultats
nom_res='testCarte'; 

%nom du fichier representant le masque  (format png ok)
nom_masque='C:\Users\bprigent\Datas\testFolder\Shanoir-download_1ds_22-05-2024_15h1549\mask.nii.jpg'; 

%nombre d'iterations maximal
NB_ITER_MAX=200;

Nc=3;  %nombre de composantes
A0=[0.2 0.5 0.3]; %valeurs initiales en proportion
T2=[50 150 400]; % valeurs initiales en ms

bruit=22/sqrt(pi/2); % moyenne du fond divisée par sqrt(pi/2);

%parametres de regularisation
bet=0.4;
del=7;

p=genpath(path_functions);
addpath(p,'-begin');
fonction_estimation(rep_dcm,rep_res,nom_res,Nc,A0,T2,nom_masque,bet,del,bruit,NB_ITER_MAX);
