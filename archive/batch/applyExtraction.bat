rem Script to use brain extraction of Anima
rem Auteur: B. Prigent
rem Creation: 07/05/24
rem Last Maj: 29/05/24

@REM Besoin d'un nnrd pour l'atlas

@echo off
setlocal enabledelayedexpansion
title Anima Extraction

cls

@REM set DATASET=C:\\Users\\bprigent\\MyDatas\\TestFolder\\pouetT2.nii.gz
@REM set DATASET=C:\\Users\\bprigent\\MyDatas\\TestFolder\\pouetT1.nii.gz

set DATASET=C:\\Users\\bprigent\\MyDatas\\TestFolder\\HC1_concat.nii.gz
set SCRIPTFOLDER=C:\\d\\Anima-Scripts-Public\\brain_extraction\\animaAtlasBasedBrainExtraction.py
set dataExtracted=C:\\Users\\bprigent\\MyDatas\\TestFolder
set ATLAS=C:\\Users\\bprigent\\MyDatas\\TestFolder\\NODALT1
@REM set ATLAS=C:\\d\\Anima-Scripts-Data-Public\\icc_atlas

if not exist %dataExtracted% (
    mkdir %dataExtracted%
)

echo Started:%time%

python %SCRIPTFOLDER% ^
    -i %DATASET% ^
    -a %ATLAS% ^
    -K
    @REM -b %dataExtracted%\\brainExtractedTest.nnrd ^
    @REM -m %dataExtracted%\\maskExtractedTest.nnrd
pause