:: Script to use my version of monoexp
:: Auteur: B. Prigent
:: Creation: 06/05/24
:: Last Maj: 06/05/24

@echo off
setlocal enabledelayedexpansion
title Anima EPG Process

cls

set DATASET=C:\Users\bprigent\Desktop\Datas\RECON
set t2out=C:\Users\bprigent\Resultats\RECON_CarteT2Gradient
::set excitationFile=C:\Users\bprigent\Documents\Pro\FilesAnimaMRI\ScriptAnima\Excitation_Normal.txt
::set pulseProfileFile=C:\Users\bprigent\Documents\Pro\FilesAnimaMRI\ScriptAnima\Excitation_Normal.txt

if not exist %t2out%\b1 (
    mkdir %t2out%\b1 
)

if not exist %t2out%\EPG  (
    mkdir %t2out%\EPG  
)

if not exist %t2out%\m0 (
    mkdir %t2out%\m0 
)


animaT2EPGRelaxometryEstimation.exe ^
    --t2-flip 180 ^
    -e 10.2 ^
    --tr 2000 ^
    -w 1.3 ^
    -i "!DATASET!\OSV-IRM 11180_16388\ReCon_23545\Dataset_OSV-IRM_11180_518927_irstea_semc_diff_C0PI_HP_irstea_semc_diff_C0PI_HP_20240507090135\OSV-IRM 11180_irstea_semc_diff C0PI HP_10_HP_9_1.nii.gz" ^
    -o %t2out%\EPG\11180_irstea_semc_t2EPGC0.nii.gz ^
    -O %t2out%\m0\11180_irstea_semc_m0C0.nii.gz ^
    --t1 "C:\Users\bprigent\Desktop\OSV-IRM 11180_t1_mprage_sag_p2_iso_5_4_0.nii.gz"

pause