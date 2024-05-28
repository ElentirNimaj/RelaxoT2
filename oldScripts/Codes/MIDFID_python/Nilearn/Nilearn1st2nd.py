#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

# ============================================= #
# 1st and 2nd Lvl
# B. Prigent
# v 1, 13-June-2023
# ============================================= #
"""
    Script to realize a first and second level analyzis by using fMRIPrep derivatives with nilearn
"""

# %% 0- Library
import os
import nilearn
import shutil
import json
import warnings
from nilearn import datasets
from nilearn import plotting
from nilearn import glm
from nilearn.glm.first_level import make_first_level_design_matrix
from nilearn import interfaces
from nilearn.interfaces.fsl import get_design_from_fslmat
from nilearn.interfaces.bids import get_bids_files
from nilearn.image import concat_imgs,mean_img,resample_img
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import gzip

BIDS_DIR = "c:/users/bprigent/Documents/Pro/MIDFID_Experiment/Data/BIDS/rawdata/"
DERIVATES_DIR = BIDS_DIR+'derivatives/'
OUTPUT1_DIR = 'c:/users/bprigent/Documents/Pro/MIDFID_Experiment/1stLevel/'
OUTPUT2_DIR = 'c:/users/bprigent/Documents/Pro/MIDFID_Experiment/2ndLevel/'

# %% 1- Data

def gunzip():
    derivativesfolderanat=[]
    derivativesfolderfunc=[]
    with os.scandir(DERIVATES_DIR) as dd:
        for sub in dd:
            if sub.name.startswith('sub') and not sub.name.endswith('html'):
                derivativesfolderanat.append(DERIVATES_DIR+sub.name+'/anat/')
                derivativesfolderfunc.append(DERIVATES_DIR+sub.name+'/func/')
    
    for anatsubject in derivativesfolderanat:
        with os.scandir(anatsubject) as ans:
            for file in ans:
                if file.name.endswith('desc-preproc_T1w.nii.gz'):
                    with gzip.open(anatsubject+file.name,'rb') as f_in:
                        with open(anatsubject+file.name.replace('.gz',''),'wb') as f_out:
                            shutil.copyfileobj(f_in,f_out)
    
    for funcsubject in derivativesfolderfunc:
        with os.scandir(funcsubject) as fus:
            for file in fus:
                if file.name.endswith('desc-preproc_bold.nii.gz'):
                    with gzip.open(funcsubject+file.name,'rb') as f_in:
                        with open(funcsubject+file.name.replace('.gz',''),'wb') as f_out:
                            shutil.copyfileobj(f_in,f_out)
    return

def delnii():
    derivativesfolderanat=[]
    derivativesfolderfunc=[]
    with os.scandir(DERIVATES_DIR) as dd:
        for sub in dd:
            if sub.name.startswith('sub') and not sub.name.endswith('html'):
                sub.name.find
                derivativesfolderanat.append(DERIVATES_DIR+sub.name+'/anat/')
                derivativesfolderfunc.append(DERIVATES_DIR+sub.name+'/func/')
    
    for anatsubject in derivativesfolderanat:
        with os.scandir(anatsubject) as ans:
            for file in ans:
                if file.name.endswith('nii'):
                    os.remove(anatsubject+file.name)
    
    for funcsubject in derivativesfolderfunc:
        with os.scandir(funcsubject) as fus:
            for file in fus:
                if file.name.endswith('nii'):
                    os.remove(funcsubject+file.name)
    return

task_label = "midnirs"
space_label = "MNI152NLin2009cAsym"

BIDSFILE = get_bids_files(BIDS_DIR)

models,models_run_imgs,models_events,models_confounds = glm.first_level.first_level_from_bids(BIDS_DIR,task_label,space_label,derivatives_folder=DERIVATES_DIR)

model,imgs,events,confounds = (models[0],models_run_imgs[0],models_events[0],models_confounds[0])
EVENTSFORMATRIX = pd.read_table(BIDS_DIR+'sub-A01/func/sub-A01_task-midnirs_events.tsv')
hrf_model = "spm"
with open(BIDS_DIR+'sub-A01/func/sub-A01_task-midnirs_bold.json','rt') as fp:
    task_info = json.load(fp)
SliceTiming = np.asarray(task_info['SliceTiming'])
SliceTiming = np.delete(SliceTiming,[17,34,51])
print(SliceTiming)
X1 = make_first_level_design_matrix(
    np.asarray(SliceTiming),
    EVENTSFORMATRIX,
    drift_model='polynomial',
    drift_order=3,
    hrf_model=hrf_model
)

# subject = f'sub-{model.subject_label}'
# model.minimize_memory = False

# fsl_design_matrix_path = os.path.join(BIDS_DIR,DERIVATES_DIR,task_label,subject,"try.feat","design.mat")

# design_matrix = get_design_from_fslmat(fsl_design_matrix_path,column_names=None)

# design_columns = [
# f"cond_{int(i):02}" for i in range(len(design_matrix.columns))]

# print(design_columns)