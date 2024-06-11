rem Script to use DECAES
rem Auteur: B. Prigent
rem Creation: 07/05/24
rem Last Maj: 09/05/24

@echo off
setlocal enabledelayedexpansion
title DECAES

decaes ^
    C:/Users/bprigent/Desktop/collapse.nii.gz ^
    --T2map --T2part --TE 9.2e-3 --nT2 40 ^
    --T2Range 9.2e-3 2.0 --SPWin 9.2e-3 25e-3 --MPWin 25e-3 200e-3 --Reg lcurve ^
    --output output/basic/

pause 
echo 