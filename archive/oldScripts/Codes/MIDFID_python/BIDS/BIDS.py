#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

# ============================================= #
# BIDS Folder
# B. Prigent
# v 1, 13-Apr-2023
# ============================================= #
"""
    Script to create BIDS folders, files, ...
"""

# %% 0 - Library
import os
import pandas as pan
import shutil
import numpy as np
import tkinter as tk
from tkinter.filedialog import askdirectory
import onsetintotsv2
import LibraryjsAndtsv as lib
# %% 1 - Markdown

BIDSpath = "C:/Users/bprigent/Documents/Pro/MIDFID_Experiment/Data/"
MIDFIDDIR = "C:/Users/bprigent/Code/Python_files/MIDFID_python/"
BIDS = BIDSpath+"BIDS/"

def creation_md():
    with open(BIDS+'rawdata/README', 'w') as readme:
        readme.write('MIDFID experiment') 
    with open(BIDS+'rawdata/LICENSE', 'w') as licence:
        licence.write('Used Licence')
    with open(BIDS+'rawdata/CHANGES', 'w') as changes:
        changes.write('Version History')
    return

# %% 2 - Json and tsv

def creation_participants():
    with open(BIDS+'rawdata/participants.json','w') as pjson:
        pjson.write(lib.participant_json)
    with open(BIDS+'rawdata/participants.tsv','w') as ptsv:
        ptsv.write(lib.participant_tsv)
    with open(BIDS+'rawdata/dataset_description.json','w') as data:
        data.write(lib.description_json)   
    return

# %% 3 - Folders and hardlink

def BIDSfolder():
    try: 
        os.makedirs(BIDS+'rawdata')
    except FileExistsError:
        pass
    try: 
        os.makedirs(BIDS+'rawdata/code')
    except FileExistsError:
        pass
    try: 
        os.makedirs(BIDS+'rawdata/stimuli')
    except FileExistsError:
        pass
    try: 
        os.makedirs(BIDS+'rawdata/derivatives')
    except FileExistsError:
        pass 
    try: 
        os.makedirs(BIDS+'rawdata/sourcedata')
    except FileExistsError:
        pass
    
    for index_subject in range(1,16):
        label = str(index_subject)
        if index_subject <= 9:
            subject = 'sub-A0'+label
        else:
            subject = 'sub-A'+label
        try:
            os.makedirs(BIDS+'rawdata/'+subject+'/anat')
        except FileExistsError:
            pass
        try:
            os.makedirs(BIDS+'rawdata/'+subject+'/func')
        except FileExistsError:
            pass

    return


def BIDSdata():
    RAWDATA = BIDSpath + "RAW_DATA/"
    Rawdata_folder = os.listdir(RAWDATA)
    # del Rawdata_folder[0]
    del Rawdata_folder[15:21]
    subject = 0
    subject_folder = os.listdir(BIDS+'rawdata/')
    del subject_folder[0:10]
    print(Rawdata_folder)
    for folder in Rawdata_folder:
        bold = subject_folder[subject] + '_task-midnirs_bold.nii.gz'
        bold_json = subject_folder[subject] + '_task-midnirs_bold.json'
        anat = subject_folder[subject] + '_T1w.nii.gz'
        anat_json = subject_folder[subject] + '_T1w.json'
        cemov_file = os.listdir(RAWDATA+folder+'/')
        cemov_file.pop(0)
        try:
            os.link(RAWDATA+folder+'/'+cemov_file[0],BIDS+'rawdata/'+subject_folder[subject]+'/'+'func/'+bold)
        except FileExistsError:
            print(RAWDATA+folder+'/'+cemov_file[0],BIDS+'rawdata/'+subject_folder[subject]+'/'+'func/'+bold +' already exists')
        try:
            os.link(RAWDATA+folder+'/'+cemov_file[1],BIDS+'rawdata/'+subject_folder[subject]+'/'+'func/'+bold_json)
        except FileExistsError:
            print(RAWDATA+folder+'/'+cemov_file[1],BIDS+'rawdata/'+subject_folder[subject]+'/'+'func/'+bold_json+' already exists')
        try:
            os.link(RAWDATA+folder+'/'+cemov_file[2],BIDS+'rawdata/'+subject_folder[subject]+'/'+'anat/'+anat)
        except FileExistsError:
            print(RAWDATA+folder+'/'+cemov_file[2],BIDS+'rawdata/'+subject_folder[subject]+'/'+'anat/'+anat+' already exists')
        try:
            os.link(RAWDATA+folder+'/'+cemov_file[3],BIDS+'rawdata/'+subject_folder[subject]+'/'+'anat/'+anat_json)
        except FileExistsError:
            print(RAWDATA+folder+'/'+cemov_file[3],BIDS+'rawdata/'+subject_folder[subject]+'/'+'anat/'+anat_json + ' already exist')
        subject += 1
    return
        
# %% 4 - Run 


# BIDSfolder()
# creation_md()
# creation_participants()
# BIDSdata()

onsetintotsv.rm_old_tsv()
onsetintotsv.concatenate_onset()

try:
    os.link(MIDFIDDIR + "BIDS.py",BIDS+'/rawdata/code/BIDS.py')
except FileExistsError:
    os.remove(BIDS+'/rawdata/code/BIDS.py')
    os.link(MIDFIDDIR +"BIDS.py",BIDS+'/rawdata/code/BIDS.py')

try:
    os.link(MIDFIDDIR +"onsetintotsv.py",BIDS+'/rawdata/code/onsetintotsv.py')
except FileExistsError:
    os.remove(BIDS+'/rawdata/code/onsetintotsv.py')
    os.link(MIDFIDDIR +"onsetintotsv.py",BIDS+'/rawdata/code/onsetintotsv.py')