:: Script to use my version of monoexp
:: Auteur: B. Prigent
:: Creation: 07/05/24
:: Last Maj: 07/05/24

@echo off
setlocal enabledelayedexpansion
title Anima Extraction

cls

set DATASET=C:\Users\bprigent\Desktop\Datas\RECON
set scriptFolder=C:\d\Anima-Scripts-Public\brain_extraction\animaAtlasBasedBrainExtraction.py
set dataExtracted=C:\Users\bprigent\Datas\testExtracted

if not exist %dataExtracted% (
    mkdir %dataExtracted%
)

python %scriptFolder% ^
    -i "C:\Users\bprigent\Datas\RECON\OSV-IRM 11180_16388\ReCon_23545\Dataset_OSV-IRM_11180_518926_irstea_semc_diff_C2PI_irstea_semc_diff_C2PI_20240507090113\OSV-IRM 11180_irstea_semc_diff C2PI_7_C2PI_6_1.nii.gz" ^
    -a "C:\d\Anima-Scripts-Data-Public\icc_atlas\Reference_T1.nrrd" ^
    -b %dataExtracted%\brainExtractedTest.nnrd ^
    -m %dataExtracted%\maskExtractedTest.nnrd
pause