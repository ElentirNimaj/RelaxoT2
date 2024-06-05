rem Script to use plan relaxometry
rem Auteur: B. Prigent
rem Creation: 06/05/24
rem Last Maj: 29/05/24

@echo off
setlocal enabledelayedexpansion
title Anima mono exp Process

cls

set DATASET=C:\Users\bprigent\Desktop\Datas\RECON
set t2out=C:\Users\bprigent\Resultats\RECON_CarteT2Gradient
::set excitationFile=C:\Users\bprigent\Documents\Pro\FilesAnimaMRI\ScriptAnima\Excitation_Normal.txt
::set pulseProfileFile=C:\Users\bprigent\Documents\Pro\FilesAnimaMRI\ScriptAnima\Excitation_Normal.txt
::mkdir %t2out%\b1 
::mkdir %t2out%\EPG 
::mkdir %t2out%\m0 

animaT2RelaxometryEstimation.exe ^
    -e 9.7 ^
    --tr 2720 ^
    -l "!DATASET!\OSV-IRM 11180_16388\ReCon_23545\Dataset_OSV-IRM_11180_518927_irstea_semc_diff_C0PI_HP_irstea_semc_diff_C0PI_HP_20240507090135\OSV-IRM 11180_irstea_semc_diff C0PI HP_10_HP_9_1.nii.gz" ^
    -o %t2out%\t2.nii.gz

pause