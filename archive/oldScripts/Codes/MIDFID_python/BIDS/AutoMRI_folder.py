#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

# ============================================= #
# AutoMRI Folder
# B. Prigent
# v 1, 13-Apr-2023
# ============================================= #
"""
    Creation and modification of automri folder
"""

import os
import pandas as pan
import shutil
import numpy as np
import onsetintotsv
import tkinter as tk
from tkinter.filedialog import askdirectory

MIDFIDDIR = "C:/Users/bprigent/Code/Python_files/MIDFID_python/"
MIDFID_PATH = "C:/users/bprigent/Documents/Pro/MIDFID_Experiment/MIDFID_AutoMRI/data/gr_A/"
RAWDATA_PATH = "C:/Users/bprigent/Documents/Pro/MIDFID_Experiment/Data/RAW_DATA/"

def creation_folder():
    try:
        os.makedirs(MIDFID_PATH)
    except FileExistsError:
        pass
    for index_subject in range(1,16):
        label = str(index_subject)
        if index_subject <= 9:
            subject = 'su_A0'+label
        else:
            subject = 'su_A'+label
        try:
            os.makedirs(MIDFID_PATH+subject+'/structural/')
        except FileExistsError:
            pass
        try:
            os.makedirs(MIDFID_PATH+subject+'/functional/se_midnirs/')
        except FileExistsError:
            pass
    return

def AutoMRIdata():
    RAWDATA = RAWDATA_PATH
    Rawdata_folder = os.listdir(RAWDATA)
    # del Rawdata_folder[0]
    del Rawdata_folder[15:21]
    subject = 0
    subject_folder = os.listdir(MIDFID_PATH)
    for folder in Rawdata_folder:
        bold ='Fonct_'+ subject_folder[subject] + '_task-midnirs_bold.nii.gz'
        anat = 'T13D_' + subject_folder[subject] + '_T1w.nii.gz'
        cemov_file = os.listdir(RAWDATA+folder+'/')
        cemov_file.pop(0)
        try:
            os.link(RAWDATA+folder+'/'+cemov_file[0],MIDFID_PATH+subject_folder[subject]+'/'+'functional/se_midnirs/'+bold)
        except FileExistsError:
            print(RAWDATA+folder+'/'+cemov_file[0],MIDFID_PATH+subject_folder[subject]+'/'+'functional/se_midnirs/'+bold +' already exists')
        try:
            os.link(RAWDATA+folder+'/'+cemov_file[2],MIDFID_PATH+subject_folder[subject]+'/'+'structural/'+anat)
        except FileExistsError:
            print(RAWDATA+folder+'/'+cemov_file[2],MIDFID_PATH+subject_folder[subject]+'/'+'structural/'+anat+' already exists')
        subject += 1
    return

creation_folder()
AutoMRIdata()
onsetintotsv.onset_AutoMRI()