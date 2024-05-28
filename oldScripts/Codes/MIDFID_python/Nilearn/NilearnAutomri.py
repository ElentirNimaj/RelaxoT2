#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

# ============================================= #
# Nilearn for AutoMRI
# B. Prigent
# v 1, 13-June-2023
# ============================================= #
"""
    Script to realize a 2nd level analysis with data preproc by automri 
"""

# %% 0- Library
import os
import nilearn
import shutil
import json
import warnings
from nilearn import datasets
from nilearn import plotting
from nilearn import surface
from nilearn import glm
from nilearn.glm.first_level import make_first_level_design_matrix
from nilearn.glm.second_level import *
from nilearn.glm import threshold_stats_img
from nilearn import plotting
from nilearn.reporting import get_clusters_table
from nilearn import interfaces
from nilearn.interfaces.fsl import get_design_from_fslmat
from nilearn.interfaces.bids import get_bids_files
from nilearn.image import concat_imgs,mean_img,resample_img
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import gzip

AUTODIR = "c:/users/bprigent/Documents/Pro/MIDFID_Experiment/MIDFID_AutoMRI/"
PREPROC = "c:/users/bprigent/Documents/Pro/MIDFID_Experiment/MIDFID_AutoMRI/pre-processing/"
FIRSTLVL = "c:/users/bprigent/Documents/Pro/MIDFID_Experiment/MIDFID_AutoMRI/results/functional/d01_AnticipationAndReward/1st_level/gr_A/"

p_val=0.05
p001_uncorrected = norm.isf(p_val)
# %% 1- Data

TASKNAME = ['AntFoodHigh','AntMoneyHigh','AntFoodNo','AntMoneyNo','AntFoodLow','AntMoneyLow', 'RewFoodHigh','RewMoneyHigh','RewFoodNo','RewMoneyNo','RewFoodLow','RewMoneyLow','RewFoodNo30','RewMoneyNo30']

subject = ['su_A01','su_A02','su_A03','su_A04','su_A05','su_A06','su_A07','su_A08','su_A09',
       'su_A10','su_A11','su_A12','su_A13','su_A14','su_A15']

spm1stcontrast = [FIRSTLVL+'su_A01/'+'spmT_0001.nii.gz',FIRSTLVL+'su_A02/'+'spmT_0001.nii.gz',
                  FIRSTLVL+'su_A03/'+'spmT_0001.nii.gz',FIRSTLVL+'su_A04/'+'spmT_0001.nii.gz',
                  FIRSTLVL+'su_A05/'+'spmT_0001.nii.gz',FIRSTLVL+'su_A06/'+'spmT_0001.nii.gz',
                  FIRSTLVL+'su_A07/'+'spmT_0001.nii.gz',FIRSTLVL+'su_A08/'+'spmT_0001.nii.gz',
                  FIRSTLVL+'su_A09/'+'spmT_0001.nii.gz',FIRSTLVL+'su_A10/'+'spmT_0001.nii.gz',
                  FIRSTLVL+'su_A11/'+'spmT_0001.nii.gz',FIRSTLVL+'su_A12/'+'spmT_0001.nii.gz',
                  FIRSTLVL+'su_A13/'+'spmT_0001.nii.gz',FIRSTLVL+'su_A14/'+'spmT_0001.nii.gz',
                  FIRSTLVL+'su_A15/'+'spmT_0001.nii.gz']

design_matrix = pd.DataFrame([1] * 15, columns=["intercept"])

SecondLvl = SecondLevelModel(smoothing_fwhm=8)
Fittage = SecondLvl.fit(spm1stcontrast,design_matrix=design_matrix)

z_map = SecondLvl.compute_contrast(output_type="z_score")

threshold_map1,threshold1 = threshold_stats_img(
    z_map,alpha=0.001,height_control="fpr",cluster_threshold=0,two_sided=True
)


# display = plotting.plot_stat_map(z_map)
# plotting.plot_stat_map(threshold_map1,cut_coords=display.cut_coords,threshold=threshold1)
# plotting.show()

test = get_clusters_table(z_map,stat_threshold=threshold1,cluster_threshold=10)
print(test)

fsaverage = datasets.fetch_surf_fsaverage()
curv_left = surface.load_surf_data(fsaverage.curv_left)
curv_left_sign = np.sign(curv_left)
texture = surface.vol_to_surf(z_map,fsaverage.pial_left)


curv_right = surface.load_surf_data(fsaverage.curv_right)
curv_right_sign = np.sign(curv_right)
texture = surface.vol_to_surf(z_map,fsaverage.pial_right)

surfL = plotting.plot_surf_stat_map(fsaverage['infl_left'],texture,hemi='left',colorbar=True,threshold=threshold1,bg_map=fsaverage['sulc_left'])
plotting.show()
surfR = plotting.plot_surf_stat_map(fsaverage['infl_right'],texture,hemi='right',colorbar=True,threshold=threshold1,bg_map=fsaverage['sulc_right'])
plotting.show()