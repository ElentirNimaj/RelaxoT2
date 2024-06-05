rem Script to collapse some omages
rem Auteur: B. Prigent
rem Creation: 07/05/24
rem Last Maj: 29/05/24

@echo off
setlocal enabledelayedexpansion
title animaConcatenateImages

set DATASET=C:\\Users\\bprigent\\MyDatas\\TestFolder\\NODAL1Test

animaConcatenateImages.exe ^
     -i C:\\Users\\bprigent\\MyDatas\\TestFolder\\NODAL1Test\\NODAL_01_masked.nii.gz ^
     -i C:\\Users\\bprigent\\MyDatas\\TestFolder\\NODAL1Test\\NODAL_02_masked.nii.gz ^
     -o %DATASET%\\Concatenated.nii.gz

pause 
echo 