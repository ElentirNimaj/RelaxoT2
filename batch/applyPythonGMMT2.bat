:: Script to use python GMMT
:: Auteur: B. Prigent
:: Creation: 06/05/24
:: Last Maj: 06/05/24

@echo off
setlocal enabledelayedexpansion
title Anima python GMMT2

cls

set DATASET=C:\Users\bprigent\Datas\RECON\OSV-IRM 11180_16388\ReCon_23545

if not exist %t2out%\b1 (
    mkdir %t2out%\b1 
)

if not exist %t2out%\EPG  (
    mkdir %t2out%\EPG  
)

if not exist %t2out%\m0 (
    mkdir %t2out%\m0 
)

if not exist %t2out%\C0 (
    mkdir %t2out%\C0 
)

if not exist %t2out%\C2 (
    mkdir %t2out%\C2 
)
if not exist %t2out%\C4 (
    mkdir %t2out%\C4 
)

python C:\d\Anima-Scripts-Public\relaxometry\animaT2RelaxometryExtraction.py ^
    -i "C:\Users\bprigent\Datas\RECON\OSV-IRM 11180_16388\ReCon_23545\Dataset_OSV-IRM_11180_518930_irstea_semc_diff_C2PI_HP_irstea_semc_diff_C2PI_HP_20240507090136\OSV-IRM 11180_irstea_semc_diff C2PI HP_11_HP_10_1.nii.gz" ^
    -e 10.20 ^
    --tr-value 2000 ^
    -g C:\Users\bprigent\Resultats\C2\pyC2HP_GMMT2.nii.gz ^
    -K

python C:\d\Anima-Scripts-Public\relaxometry\animaT2RelaxometryExtraction.py ^
    -i "C:\Users\bprigent\Datas\RECON\OSV-IRM 11180_16388\ReCon_23545\Dataset_OSV-IRM_11180_518927_irstea_semc_diff_C0PI_HP_irstea_semc_diff_C0PI_HP_20240507090135\OSV-IRM 11180_irstea_semc_diff C0PI HP_10_HP_9_1.nii.gz" ^
    -e 10.20 ^
    --tr-value 2000 ^
    -g C:\Users\bprigent\Resultats\C2\pyC0HP_GMMT2.nii.gz^
    -K

python C:\d\Anima-Scripts-Public\relaxometry\animaT2RelaxometryExtraction.py ^
    -i "C:\Users\bprigent\Datas\RECON\OSV-IRM 11180_16388\ReCon_23545\Dataset_OSV-IRM_11180_518927_irstea_semc_diff_C0PI_HP_irstea_semc_diff_C0PI_HP_20240507090135\OSV-IRM 11180_irstea_semc_diff C0PI HP_10_HP_9_1.nii.gz" ^
    -e 10.20 ^
    --tr-value 2000 ^
    -o C:\Users\bprigent\Resultats\C2\pyC0HP_T2EPG.nii.gz^
    -K

python C:\d\Anima-Scripts-Public\relaxometry\animaT2RelaxometryExtraction.py ^
    -i "C:\Users\bprigent\Resultats\C2\pyC0HP_T2EPG.nii.gz"^
    -e 10.20 ^
    --tr-value 2000 ^
    -g C:\Users\bprigent\Resultats\C2\pyC0HP_GMMT2EPG.nii.gz^
    -K
pause