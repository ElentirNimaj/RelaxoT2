@REM  Script to use brain extraction of Anima then concatenate file
@REM  Auteur: B. Prigent
@REM  Creation: 03/06/24
@REM  Last Maj: 03/06/24

@echo off
setlocal enabledelayedexpansion
title Anima Extraction and concatenation

cls

@REM 
set DATASET=C:\\Users\\bprigent\\MyDatas\\TestFolder\\NODAL1
set EXTRACTSCRIPT=C:\\d\\Anima-Scripts-Public\\brain_extraction\\animaAtlasBasedBrainExtraction.py
set CONCATENATESCRIPT=C:\\d\\Anima-Scripts-Public\\brain_extraction\\animaConcatenateImages.exe
set dataExtracted=C:\\Users\\bprigent\\MyDatas\\TestFolder
set ATLAS=C:\\Users\\bprigent\\MyDatas\\TestFolder\\NODALT1

if not exist %dataExtracted% (
    mkdir %dataExtracted%
)

echo Creation txt extraction file
echo Started:%time%
echo .

@REM Create a txt file with all the path of the nii file we want to extract

if not exist %DATASET%\\allFiles_RELAXO_20240419133106.txt (
    for /r %DATASET%\\ %%B in ("*.nii.gz") do (
	ECHO %%B>> %DATASET%\\allFiles_RELAXO_20240419133106.txt
	)
) else (
        del %DATASET%\\allFiles_RELAXO_20240419133106.txt
        for /r %DATASET%\\ %%B in ("*.nii.gz") do (
	    ECHO %%B>> %DATASET%\\allFiles_RELAXO_20240419133106.txt
    )
)

pause 

@REM Extract all brain present in folder

echo .
echo Brain extraction
echo Started:%time%
echo .

for %%P in (%DATASET%\\.txt) do (
python %SCRIPTFOLDER% ^
    -i %DATASET% ^
    -a %ATLAS% ^
    -K
    @REM -b %dataExtracted%\\brainExtractedTest.nnrd ^
    @REM -m %dataExtracted%\\maskExtractedTest.nnrd
)

@REM Create the brain file with all the path we want to concatenate

if not exist %DATASET%\\allBrainFiles_RELAXO_20240419133106.txt (
    for /r %DATASET%\\Dataset_NODAL_VS_001_489587_RELAXO_VHD_RELAXO_VHD_20240419133106 %%B in ("*.nii.gz") do (
	ECHO %%B>> %DATASET%\\allBrainFiles_RELAXO_20240419133106.txt
	)
) else (
        del %DATASET%\\allBrainFiles_RELAXO_20240419133106.txt
        for /r %DATASET%\\Dataset_NODAL_VS_001_489587_RELAXO_VHD_RELAXO_VHD_20240419133106 %%B in ("*.nii.gz") do (
	    ECHO %%B>> %DATASET%\\allBrainFiles_RELAXO_20240419133106.txt
    )
)