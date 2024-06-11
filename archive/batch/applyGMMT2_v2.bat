rem Script to use GMMT2
rem Auteur: B. Prigent
rem Creation: 06/05/24
rem Last Maj: 29/05/24

@echo off
setlocal enabledelayedexpansion
title Anima Gauss Process

cls

set DATASET=C:\Users\bprigent\Datas\RECON\OSV-IRM 11180_16388\ReCon_23545
set t2out=C:\Users\bprigent\Resultats\CarteC2PI
set excitationFile=C:\Users\bprigent\Documents\Pro\FilesAnimaMRI\ScriptAnima\Excitation_Normal.txt
set pulseProfileFile=C:\Users\bprigent\Documents\Pro\FilesAnimaMRI\ScriptAnima\Excitation_Normal.txt
set 

animaGMMT2RelaxometryEstimation.exe ^
    --t2-flip 180 ^
    -e 10 ^
    -w 1.3 ^
    -p %pulseProfileFile% ^
    -E %excitationFile% ^
    -i "C:\Users\bprigent\Datas\RECON\OSV-IRM 11180_16388\ReCon_23545\Dataset_OSV-IRM_11180_518926_irstea_semc_diff_C2PI_irstea_semc_diff_C2PI_20240507090113\OSV-IRM 11180_irstea_semc_dif"^
    -o %t2out%\GMMT2_C2PI.nii.gz ^
    -O %t2out%\wgtC2PI.nii.gz 

pause