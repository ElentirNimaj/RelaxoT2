#!/usr/bin/env python3
# -*- coding: utf-8 -*- #
# ============================================= #
# Extraction/Concatenation brain
# B. Prigent
# v 2, 04-Jun-2024
# ============================================= #
"""
    Extract each brain in a folder then concatenate them in one file.
"""

import os
from datetime import datetime
import glob
from subprocess import run
import shutil

# DATASET = r"C:\Users\bprigent\MyDatas\TestFolder\NODAL1"
# DATASET = r"C:\Users\bprigent\MyDatas\TestFolder\"
DATASET = r"C:\Users\bprigent\MyDatas\TestFolder\C0PIDCMCrop.nrrd"
EXTRACT_SCRIPT = r"C:\d\Anima-Scripts-Public\brain_extraction\animaAtlasBasedBrainExtraction.py"
CONCATENATE_SCRIPT = r"C:\d\Anima-build\bin\Debug\animaConcatenateImages.exe"
CONVERT_SCRIPT = r"C:\d\Anima-build\bin\Debug\animaConvertImage.exe"
DATA_EXTRACTED = r"C:\Users\bprigent\MyDatas\TestFolder"
ATLAS = r"C:\Users\bprigent\MyDatas\TestFolder\NODALT1"

date_time = datetime.now()
current_time = date_time.strftime("%H:%M:%S")


def extract_brain():
    print("Brain extraction")
    print(f"Started at {current_time}\n")

    list_nii = glob.glob(DATASET + "/*.gz")

    for niiImage in list_nii:
        command=["python", EXTRACT_SCRIPT, "-i" , niiImage,"-K"]
        run(command)
    return None

def convert_nrrd():
    print("Brain conversion")
    print(f"Started at {current_time}\n")

    list_nrrd = glob.glob(DATASET + "/*brainMask.nrrd")
    command = [CONVERT_SCRIPT,"-i", DATASET, "-o ", r"C:\Users\bprigent\MyDatas\TestFolder\C0PIDCMCrop.nrrd".replace("nrrd","nii.gz")]
    run(command)
    # for nrrdImage in list_nrrd:
        # command = [CONVERT_SCRIPT,"-i", nrrdImage, "-o ", nrrdImage.replace("nrrd","nii.gz")]
        # run(command)
        # os.remove(nrrdImage)

    return None

def concat_echoes():
    print("Image concatenation")
    print(f"Started at {current_time}\n")

    path_nii = glob.glob(DATASET + "/*brainMask.nii.gz")
    path_nii = [' -i ' + nii for nii in path_nii]
    
    command = CONCATENATE_SCRIPT + "".join(path_nii) + " -o " + DATASET + "\\ConcatenatedbrainMask.nii.gz" 
    run(command)
    
    return None

if __name__ == "__main__":
    # extract_brain()
    convert_nrrd()
    # concat_echoes()