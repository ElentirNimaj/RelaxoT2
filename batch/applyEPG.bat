rem Script to use animaT2EPG
rem Auteur: B. Prigent
rem Creation: 06/05/24
rem Last Maj: 29/05/24

@echo off
setlocal enabledelayedexpansion
title Anima EPG Process

cls

set DATASET=C:\Users\bprigent\Datas\NODALHV
set t2out=C:\Users\bprigent\Resultats\TestCarteMWF
set excitationFile=C:\Users\bprigent\Documents\Pro\FilesAnimaMRI\ScriptAnima\Excitation_Normal.txt
set pulseProfileFile=C:\Users\bprigent\Documents\Pro\FilesAnimaMRI\ScriptAnima\Excitation_Normal.txt
set /a "Counter=0"

if not exist %t2out%\b1 (
    mkdir %t2out%\b1 
)

if not exist %t2out%\EPG  (
    mkdir %t2out%\EPG  
)

if not exist %t2out%\m0 (
    mkdir %t2out%\m0 
)


for /r %DATASET%\Dataset_NODAL_VS_001_489587_RELAXO_VHD_RELAXO_VHD_20240419133106 %%B in ("*.nii.gz") do (
    animaT2EPGRelaxometryEstimation.exe ^
    --t2-flip 180 ^
    -e 9.7 ^
    --tr 2720 ^
    -w 1.3 ^
    -p %pulseProfileFile% ^
    -E %excitationFile% ^
    -i %DATASET%\allFiles_RELAXO_20240419133106.txt ^
    -o %t2out%\EPG\!Counter!_t2EPG.nii.gz ^
    -O %t2out%\m0\!Counter!_m0.nii.gz 
    ::--out-b1 %t2out%\b1\!Counter!_b1.nii.gz
    set /a "Counter+=1")

pause