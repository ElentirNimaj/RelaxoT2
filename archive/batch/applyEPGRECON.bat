rem Script to use animaT2EPG for Recon datas
rem Auteur: B. Prigent
rem Creation: 07/05/24
rem Last Maj: 29/05/24

@echo off
setlocal enabledelayedexpansion
title Anima EPG Process Marc

cls

set DATASET=C:\Users\bprigent\Desktop\Datas\RECON
set t2out=C:\Users\bprigent\Resultats\RECON_CarteT2Gradient
set excitationFile=C:\Users\bprigent\Documents\Pro\FilesAnimaMRI\ScriptAnima\Excitation_Normal.txt
set pulseProfileFile=C:\Users\bprigent\Documents\Pro\FilesAnimaMRI\ScriptAnima\Excitation_Normal.txt
set maskFile=

if not exist %DATASET% (
    mkdir %DATASET%
)

if not exist %t2out%\b1 (
    mkdir %t2out%\b1 
)

if not exist %t2out%\EPG  (
    mkdir %t2out%\EPG  
)

if not exist %t2out%\m0 (
    mkdir %t2out%\m0 
)

:: if not exist %DATASET%\allFiles_RECON_11181.txt (
::     for /r %DATASET%\ %%B in ("*.nii.gz") do (
:: 	ECHO %%B>> %DATASET%\allFiles_RECON_11181.txt
:: 	)
:: ) else (
::         del %DATASET%\allFiles_RECON_11181.txt
::         for /r %DATASET%\ %%B in ("*.nii.gz") do (
:: 	    ECHO %%B>> %DATASET%\allFiles_RECON_11181.txt
::     )
:: )


animaT2EPGRelaxometryEstimation.exe ^
    --t2-flip 180 ^
    -e 10.2 ^
    --tr 2000 ^
    -w 1.3 ^
    -i "C:\Users\bprigent\Datas\RECON\OSV-IRM 11180_16388\ReCon_23545\Dataset_OSV-IRM_11180_518927_irstea_semc_diff_C0PI_HP_irstea_semc_diff_C0PI_HP_20240507090135\OSV-IRM 11180_irstea_semc_diff C0PI HP_10_HP_9_1.nii.gz" ^
    -o %t2out%\EPG\11180_irstea_semc_t2EPGC0.nii.gz ^
    -O %t2out%\m0\11180_irstea_semc_m0C0.nii.gz 
