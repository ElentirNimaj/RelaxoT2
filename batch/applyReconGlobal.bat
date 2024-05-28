:: Script to use my version of monoexp
:: Auteur: B. Prigent
:: Creation: 07/05/24
:: Last Maj: 07/05/24

@echo off
setlocal enabledelayedexpansion
title Anima Recon

cls

set DATASET=C:\Users\bprigent\Desktop\Datas\RECON
set t2out=C:\Users\bprigent\Resultats\RECON_CarteT2Gradient
set excitationFile=C:\Users\bprigent\Documents\Pro\FilesAnimaMRI\ScriptAnima\Excitation_Normal.txt
set pulseProfileFile=C:\Users\bprigent\Documents\Pro\FilesAnimaMRI\ScriptAnima\Excitation_Normal.txt


:: Folder creation
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

:: EPG C0

animaT2EPGRelaxometryEstimation.exe ^
    --t2-flip 180 ^
    -e 10.2 ^
    --tr 1100 ^
    -w 1.3 ^
    -i "C:\Users\bprigent\Datas\RECON\OSV-IRM 11180_16388\ReCon_23545\Dataset_OSV-IRM_11180_518935_irstea_semc_diff_C0PI_irstea_semc_diff_C0PI_20240507090114\OSV-IRM 11180_irstea_semc_diff C0PI_8_C0PI_7_0.nii.gz" ^
    -o %t2out%\EPG\11180_irstea_semc_t2EPGC0.nii.gz ^
    -O %t2out%\m0\11180_irstea_semc_m0C0.nii.gz 

animaT2EPGRelaxometryEstimation.exe ^
    --t2-flip 180 ^
    -e 10.2 ^
    --tr 2000 ^
    -w 1.3 ^
    -i "C:\Users\bprigent\Datas\RECON\OSV-IRM 11180_16388\ReCon_23545\Dataset_OSV-IRM_11180_518927_irstea_semc_diff_C0PI_HP_irstea_semc_diff_C0PI_HP_20240507090135\OSV-IRM 11180_irstea_semc_diff C0PI HP_10_HP_9_1.nii.gz" ^
    -o %t2out%\EPG\11180_irstea_semc_t2EPGC0HP.nii.gz ^
    -O %t2out%\m0\11180_irstea_semc_m0C0HP.nii.gz 

:: GMMT2 C0

animaGMMT2RelaxometryEstimation.exe ^
    --t2-flip 180 ^
    -e 10.2 ^
    -w 1.3 ^
    -i "C:\Users\bprigent\Datas\RECON\OSV-IRM 11180_16388\ReCon_23545\Dataset_OSV-IRM_11180_518935_irstea_semc_diff_C0PI_irstea_semc_diff_C0PI_20240507090114\OSV-IRM 11180_irstea_semc_diff C0PI_8_C0PI_7_0.nii.gz" ^
    -o %t2out%\C0\GMMTC0_woutEPG.nii.gz ^
    -O %t2out%\C0\wgt_GMMTC0_woutEPG.nii.gz 

animaGMMT2RelaxometryEstimation.exe ^
    --t2-flip 180 ^
    -e 10.2 ^
    -w 1.3 ^
    -i "C:\Users\bprigent\Datas\RECON\OSV-IRM 11180_16388\ReCon_23545\Dataset_OSV-IRM_11180_518927_irstea_semc_diff_C0PI_HP_irstea_semc_diff_C0PI_HP_20240507090135\OSV-IRM 11180_irstea_semc_diff C0PI HP_10_HP_9_1.nii.gz" ^
    -o %t2out%\C0\GMMTC0HP_woutEPG.nii.gz ^
    -O %t2out%\C0\wgt_GMMTC0HP_woutEPG.nii.gz 

animaGMMT2RelaxometryEstimation.exe ^
    --t2-flip 180 ^
    -e 10.2 ^
    -w 1.3 ^
    -i %t2out%\EPG\11180_irstea_semc_t2EPGC0.nii.gz ^
    -o %t2out%\C0\GMMTC0_EPG.nii.gz ^
    -O %t2out%\C0\wgt_GMMTC0_EPG.nii.gz 

animaGMMT2RelaxometryEstimation.exe ^
    --t2-flip 180 ^
    -e 10.2 ^
    -w 1.3 ^
    -i %t2out%\EPG\11180_irstea_semc_t2EPGC0HP.nii.gz ^
    -o %t2out%\C0\GMMTC0HP_EPG.nii.gz ^
    -O %t2out%\C0\wgt_GMMTC0HP_EPG.nii.gz 

:: GMMT2 C2

animaGMMT2RelaxometryEstimation.exe ^
    --t2-flip 180 ^
    -e 10 ^
    -w 1.3 ^
    -i "C:\Users\bprigent\Datas\RECON\OSV-IRM 11180_16388\ReCon_23545\Dataset_OSV-IRM_11180_518926_irstea_semc_diff_C2PI_irstea_semc_diff_C2PI_20240507090113\OSV-IRM 11180_irstea_semc_diff C2PI_7_C2PI_6_1.nii.gz" ^
    -o %t2out%\C2\GMMTC2.nii.gz ^
    -O %t2out%\C2\wgt_GMMTC2.nii.gz 

animaGMMT2RelaxometryEstimation.exe ^
    --t2-flip 180 ^
    -e 10.20 ^
    -w 1.3 ^
    -i "C:\Users\bprigent\Datas\RECON\OSV-IRM 11180_16388\ReCon_23545\Dataset_OSV-IRM_11180_518930_irstea_semc_diff_C2PI_HP_irstea_semc_diff_C2PI_HP_20240507090136\OSV-IRM 11180_irstea_semc_diff C2PI HP_11_HP_10_1.nii.gz" ^
    -o %t2out%\C2\GMMTC2HP.nii.gz ^
    -O %t2out%\C2\wgt_GMMTC2HP.nii.gz 

:: GMMT2 C4

animaGMMT2RelaxometryEstimation.exe ^
    --t2-flip 180 ^
    -e 10 ^
    -w 1.3 ^
    -i "C:\Users\bprigent\Datas\RECON\OSV-IRM 11180_16388\ReCon_23545\Dataset_OSV-IRM_11180_518941_irstea_semc_diff_C4PI_irstea_semc_diff_C4PI_20240507090113\OSV-IRM 11180_irstea_semc_diff C4PI_6_C4PI_5_1.nii.gz"^
    -o %t2out%\C4\GMMTC4.nii.gz ^
    -O %t2out%\C4\wgt_GMMTC4.nii.gz 

animaGMMT2RelaxometryEstimation.exe ^
    --t2-flip 180 ^
    -e 10.20 ^
    -w 1.3 ^
    -i "C:\Users\bprigent\Datas\RECON\OSV-IRM 11180_16388\ReCon_23545\Dataset_OSV-IRM_11180_518928_irstea_semc_diff_C4PI_HP_irstea_semc_diff_C4PI_HP_20240507090156\OSV-IRM 11180_irstea_semc_diff C4PI HP_12_HP_11_1.nii.gz"^
    -o %t2out%\C4\GMMTC4HP.nii.gz ^
    -O %t2out%\C4\wgt_GMMTC4HP.nii.gz 


:: GMMT2 11181

animaGMMT2RelaxometryEstimation.exe ^
    --t2-flip 120 ^
    -e 9 ^
    -w 1.3 ^
    -i "C:\Users\bprigent\Datas\RECON\OSV-IRM 11181_16389\ReCon_23546\Dataset_OSV-IRM_11181_518947_irstea_semc_C2PI_HP_ES_9_FA120_irstea_semc_C2PI_HP_ES_9_FA120_20240507090412\OSV-IRM 11181_irstea_semc C2PI HP ES 9 FA120_6_FA120_5_1.nii.gz"^
    -o %t2out%\C2\11181GMMTC2_120.nii.gz ^
    -O %t2out%\C2\11181wgt_GMMTC2_120.nii.gz 

animaGMMT2RelaxometryEstimation.exe ^
    --t2-flip 180 ^
    -e 7 ^
    -w 1.3 ^
    -i "C:\Users\bprigent\Datas\RECON\OSV-IRM 11181_16389\ReCon_23546\Dataset_OSV-IRM_11181_518946_irstea_semc_C2PI_HP_ES_7_FA180_55Echoes_irstea_semc_C2PI_HP_ES_7_FA180_55Echoes_20240507090544\OSV-IRM 11181_irstea_semc C2PI HP ES 7 FA180 55Echoes_11_55Echoes_10_1.nii.gz"^
    -o %t2out%\C2\11181GMMTC2_180.nii.gz ^
    -O %t2out%\C2\11181wgt_GMMTC2HP_180.nii.gz 

:: GMMT2 NODAL

animaGMMT2RelaxometryEstimation.exe ^
    --t2-flip 180 ^
    -e 7 ^
    -w 1.3 ^
    -i "C:\Users\bprigent\Datas\RECON\OSV-IRM 11181_16389\ReCon_23546\Dataset_OSV-IRM_11181_518946_irstea_semc_C2PI_HP_ES_7_FA180_55Echoes_irstea_semc_C2PI_HP_ES_7_FA180_55Echoes_20240507090544\OSV-IRM 11181_irstea_semc C2PI HP ES 7 FA180 55Echoes_11_55Echoes_10_1.nii.gz"^
    -o %t2out%\C2\NODALT2_woutEPG.nii.gz ^
    -O %t2out%\C2\NODALwgt_woutEPG.nii.gz 

animaT2EPGRelaxometryEstimation.exe ^
    --t2-flip 180 ^
    -e 9.7 ^
    -w 1.3 ^
    -i "C:\Users\bprigent\Datas\RECON\OSV-IRM 11181_16389\ReCon_23546\Dataset_OSV-IRM_11181_518946_irstea_semc_C2PI_HP_ES_7_FA180_55Echoes_irstea_semc_C2PI_HP_ES_7_FA180_55Echoes_20240507090544\OSV-IRM 11181_irstea_semc C2PI HP ES 7 FA180 55Echoes_11_55Echoes_10_1.nii.gz"^
    -o %t2out%\C2\NODALT2_EPG.nii.gz ^
    -O %t2out%\C2\NDOALT2_M0.nii.gz 

animaGMMT2RelaxometryEstimation.exe ^
    --t2-flip 180 ^
    -e 9.7 ^
    -w 1.3 ^
    -i %t2out%\C2\NODALT2_EPG.nii.gz^
    -o %t2out%\C2\NODALGMMT2_EPG.nii.gz ^
    -O %t2out%\C2\NODALwgt_EPG.nii.gz 


pause