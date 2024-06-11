#!/usr/bin/env python3
# -*- coding: utf-8 -*- #
# ============================================= #
# GMMT2 relaxo
# B. Prigent
# v 1, 04-Jun-2024
# ============================================= #
"""
    Apply GMMT2.
"""

import os
from datetime import datetime
import glob
from subprocess import run
import shutil

# DATASET = r"C:\Users\bprigent\MyDatas\TestFolder\NODAL1"
# DATASET = r"C:\Users\bprigent\MyDatas\TestFolder\C0PI\C0PI.nii.gz"
DATASET = r"C:\Users\bprigent\MyDatas\TestFolder\C0PI.nii.gz"
GMMT2_SCRIPT = r"C:\d\Anima-build\bin\Debug\animaGMMT2RelaxometryEstimation.exe"
MULTIT2_SCRIPT = r"C:\d\Anima-build\bin\Debug\animaMultiT2RelaxometryEstimation.exe"
EPG_SCRIPT = r"C:\d\Anima-build\bin\Debug\animaT2EPGRelaxometryEstimation.exe"
DATA_EXTRACTED = r"C:\Users\bprigent\MyDatas\TestFolder"
PULSE_PATH = r"C:\Users\bprigent\MyDatas\Scaling_Normal.txt"
EXCITATION_PATH=r"C:\Users\bprigent\MyDatas\Excitation_Normal.txt"


date_time = datetime.now()
current_time = date_time.strftime("%H:%M:%S")

# def apply_epg():
#     print("Estimate EPG\n")
#     print(f"Started {os.path.dirname(DATASET)} at {current_time}\n")
#     command = [EPG_SCRIPT,"-i",DATASET+"\\Concatenated.nii.gz","-o",DATA_EXTRACTED+"\\TestEPG.nii.gz",
#             "--t2-flip","180","--tr","2720","-e","9.7",
#             "-p",PULSE_PATH,"-E",EXCITATION_PATH]
#     run(command)
#     return None

# def apply_gmmt2_multipleechos():
#     path_echoes = glob.glob(DATASET+"/*_masked.nii.gz")
#     print(path_echoes)
#     print("GMMT2\n")
#     for niiImage in path_echoes:
#         print(f"Started {os.path.basename(niiImage)} at {current_time}\n")
#         command = [GMMT2_SCRIPT,"-i",niiImage,"-o",DATA_EXTRACTED+"\\"+os.path.basename(niiImage)+"_t2.nii.gz",
#                    "-O", DATA_EXTRACTED+"\\"+os.path.basename(niiImage)+"_weight.nii.gz",
#                    "--t2-flip","180","-e","9.7",
#                    "-p",PULSE_PATH,"-E",EXCITATION_PATH]
#         run(command)
#         print(f"\nFinished {os.path.basename(niiImage)} at {current_time}\n")
#     return None

def apply_gmmt2():
    print("GMMT2\n")
    print(f"Started {os.path.dirname(DATASET)} at {current_time}\n")
    command = [GMMT2_SCRIPT,"-i",DATASET,"-o",DATA_EXTRACTED+"\\C0PIT2.nii.gz",
                   "-O", DATA_EXTRACTED+"\\C0PI_weightGMMT2.nii.gz",
                   "--t2-flip","180","-e","10"]#,
                #    "-p",PULSE_PATH,"-E",EXCITATION_PATH]
    run(command)
    print(f"\nFinished {os.path.dirname(DATASET)} at {current_time}\n")
    return None

def apply_MultiT2():
    print("Multi T2 Erick Canales \n")
    print(f"Started {os.path.dirname(DATASET)} at {current_time}\n")
    command = [MULTIT2_SCRIPT,"-i",DATASET,"-o",
               DATA_EXTRACTED+"\\C0PI_MWFCR.nii.gz",
               "-O", DATA_EXTRACTED+"\\C0PIT2CR.nii.gz",
               "--t2-flip","180","-e","10"]#,
            #    "-p",PULSE_PATH,"-E",EXCITATION_PATH]
    run(command)
    print(f"\nFinished {os.path.dirname(DATASET)} at {current_time}\n")
    return None

if __name__ == "__main__":
    # apply_epg()
    apply_gmmt2()
    # apply_MultiT2()