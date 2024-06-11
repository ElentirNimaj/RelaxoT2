rem Script to configure
rem Auteur: B. Prigent
rem Creation: 07/05/24
rem Last Maj: 29/05/24

@echo off
setlocal enabledelayedexpansion
title Anima configure for scripting

cls

@REM set DATASET=C:/Users/bprigent/MyDatas/TestFolder/pouet.nii.gz
@REM set SCRIPTFOLDER=C:/d/Anima-Scripts-Public/brain_extraction/animaAtlasBasedBrainExtraction_simple.py
@REM set dataExtracted=C:/Users/bprigent/MyDatas/TestFolder/
@REM set ATLAS=C:/d/Anima-Scripts-Data-Public/icc_atlas/Reference_T1.nrrd

@REM if not exist %dataExtracted% (
@REM     mkdir %dataExtracted%
@REM )

python C:/d/Anima-Scripts-Public/configure.py ^
    -a C:/d/anima-build/bin/Debug ^
    -d C:/d/Anima-Scripts-Data-Public ^
    -s C:/d/Anima-Scripts-Public
pause