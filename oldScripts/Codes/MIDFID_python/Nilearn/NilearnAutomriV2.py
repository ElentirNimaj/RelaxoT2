#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

# ============================================= #
# Nilearn for AutoMRI
# B. Prigent
# v 2, 19-June-2023
# ============================================= #
"""
    Script to realize a 2nd level analysis with data preproc by automri 
"""

# %% 0- Library
import os
import glob
from nilearn import datasets
from nilearn import reporting
from nilearn import plotting
from nilearn import surface
from nilearn.glm.second_level import SecondLevelModel
from nilearn.glm import threshold_stats_img
from nilearn import plotting
from nilearn.reporting import get_clusters_table
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import nibabel as nib
import gzip

AUTODIR = "c:/users/bprigent/Documents/Pro/MIDFID_Experiment/MIDFID_AutoMRI/"
PREPROC = "c:/users/bprigent/Documents/Pro/MIDFID_Experiment/MIDFID_AutoMRI/pre-processing/"
FIRSTLVL = "c:/users/bprigent/Documents/Pro/MIDFID_Experiment/MIDFID_AutoMRI/results/functional/d01_AnticipationAndReward/1st_level/gr_A/"
SECONDLVL = "c:/users/bprigent/Documents/Pro/MIDFID_Experiment/MIDFID_AutoMRI/results/functional/d01_AnticipationAndReward/2nd_level/gr_A/"

CONDITIONS = ['Ant_Food_High','Ant_Food_No','Ant_Money_High','Ant_Money_No',
            'Ant_Food_HighvsNo','Ant_Money_HighvsNo', 'Rew_Food_High','Rew_Food_No','Rew_Money_High','Rew_Money_No','Rew_Food_HighvsNo','Rew_Money_HighvsNo','Ant_FoodAndMoney_High','Ant_FoodAndMoney_HighvsNo',
            'Rew_FoodAndMoney_High','Rew_FoodAndMoney_HighvsNo','Ant_FoodvsMoney_High','Rew_FoodvsMoney_High','Ant_FoodvsMoney_HighvsNo','Rew_FoodvsMoney_HighvsNo']



subject = ['su_A01','su_A02','su_A03','su_A04','su_A05','su_A06','su_A07','su_A08','su_A09',
           'su_A10','su_A11','su_A12','su_A13','su_A14','su_A15']

design_matrix = pd.DataFrame([1] * 15, columns=["intercept"])

def creationfolderandfile():
    for task in CONDITIONS:
        try:
            os.makedirs(SECONDLVL+'spmfiles/'+task)
        except FileExistsError:
            pass
        
    for sub in subject:
        with os.scandir(FIRSTLVL+ sub) as spmfiles:
            for spm in spmfiles:
                if spm.name.startswith('spmT_0001'):
                    try:
                        os.link(spm.path,SECONDLVL+'spmfiles/'+CONDITIONS[0]+'/spmT_'+CONDITIONS[0]+'_'+sub+'.nii.gz')
                    except FileExistsError:
                        pass
                elif spm.name.startswith('spmT_0002'):
                    try:
                        os.link(spm.path,SECONDLVL+'spmfiles/'+CONDITIONS[1]+'/spmT_'+CONDITIONS[1]+'_'+sub+'.nii.gz')
                    except FileExistsError:
                        pass
                elif spm.name.startswith('spmT_0003'):
                    try:
                        os.link(spm.path,SECONDLVL+'spmfiles/'+CONDITIONS[2]+'/spmT_'+CONDITIONS[2]+'_'+sub+'.nii.gz')
                    except FileExistsError:
                        pass
                elif spm.name.startswith('spmT_0004'):
                    try:
                        os.link(spm.path,SECONDLVL+'spmfiles/'+CONDITIONS[3]+'/spmT_'+CONDITIONS[3]+'_'+sub+'.nii.gz')
                    except FileExistsError:
                        pass
                elif spm.name.startswith('spmT_0005'):
                    try:
                        os.link(spm.path,SECONDLVL+'spmfiles/'+CONDITIONS[4]+'/spmT_'+CONDITIONS[4]+'_'+sub+'.nii.gz')
                    except FileExistsError:
                        pass                                
                elif spm.name.startswith('spmT_0006'):
                    try:
                        os.link(spm.path,SECONDLVL+'spmfiles/'+CONDITIONS[5]+'/spmT_'+CONDITIONS[5]+'_'+sub+'.nii.gz')
                    except FileExistsError:
                        pass
                elif spm.name.startswith('spmT_0007'):
                    try:
                        os.link(spm.path,SECONDLVL+'spmfiles/'+CONDITIONS[6]+'/spmT_'+CONDITIONS[6]+'_'+sub+'.nii.gz')
                    except FileExistsError:
                        pass
                elif spm.name.startswith('spmT_0008'):
                    try:
                        os.link(spm.path,SECONDLVL+'spmfiles/'+CONDITIONS[7]+'/spmT_'+CONDITIONS[7]+'_'+sub+'.nii.gz')
                    except FileExistsError:
                        pass
                elif spm.name.startswith('spmT_0009'):
                    try:
                        os.link(spm.path,SECONDLVL+'spmfiles/'+CONDITIONS[8]+'/spmT_'+CONDITIONS[8]+'_'+sub+'.nii.gz')
                    except FileExistsError:
                        pass
                elif spm.name.startswith('spmT_0010'):
                    try:
                        os.link(spm.path,SECONDLVL+'spmfiles/'+CONDITIONS[9]+'/spmT_'+CONDITIONS[9]+'_'+sub+'.nii.gz')
                    except FileExistsError:
                        pass
                elif spm.name.startswith('spmT_0011'):
                    try:
                        os.link(spm.path,SECONDLVL+'spmfiles/'+CONDITIONS[10]+'/spmT_'+CONDITIONS[10]+'_'+sub+'.nii.gz')
                    except FileExistsError:
                        pass
                elif spm.name.startswith('spmT_0012'):
                    try:
                        os.link(spm.path,SECONDLVL+'spmfiles/'+CONDITIONS[11]+'/spmT_'+CONDITIONS[11]+'_'+sub+'.nii.gz')
                    except FileExistsError:
                        pass
                elif spm.name.startswith('spmT_0013'):
                    try:
                        os.link(spm.path,SECONDLVL+'spmfiles/'+CONDITIONS[12]+'/spmT_'+CONDITIONS[12]+'_'+sub+'.nii.gz')
                    except FileExistsError:
                        pass  
                elif spm.name.startswith('spmT_0014'):
                    try:
                        os.link(spm.path,SECONDLVL+'spmfiles/'+CONDITIONS[13]+'/spmT_'+CONDITIONS[13]+'_'+sub+'.nii.gz')
                    except FileExistsError:
                        pass
                elif spm.name.startswith('spmT_0015'):
                    try:
                        os.link(spm.path,SECONDLVL+'spmfiles/'+CONDITIONS[14]+'/spmT_'+CONDITIONS[14]+'_'+sub+'.nii.gz')
                    except FileExistsError:
                        pass
                elif spm.name.startswith('spmT_0016'):
                    try:
                        os.link(spm.path,SECONDLVL+'spmfiles/'+CONDITIONS[15]+'/spmT_'+CONDITIONS[15]+'_'+sub+'.nii.gz')
                    except FileExistsError:
                        pass
                elif spm.name.startswith('spmT_0017'):
                    try:
                        os.link(spm.path,SECONDLVL+'spmfiles/'+CONDITIONS[16]+'/spmT_'+CONDITIONS[16]+'_'+sub+'.nii.gz')
                    except FileExistsError:
                        pass             
                elif spm.name.startswith('spmT_0018'):
                    try:
                        os.link(spm.path,SECONDLVL+'spmfiles/'+CONDITIONS[17]+'/spmT_'+CONDITIONS[17]+'_'+sub+'.nii.gz')
                    except FileExistsError:
                        pass
                elif spm.name.startswith('spmT_0019'):
                    try:
                        os.link(spm.path,SECONDLVL+'spmfiles/'+CONDITIONS[18]+'/spmT_'+CONDITIONS[18]+'_'+sub+'.nii.gz')
                    except FileExistsError:
                        pass            
                elif spm.name.startswith('spmT_0020'):
                    try:
                        os.link(spm.path,SECONDLVL+'spmfiles/'+CONDITIONS[19]+'/spmT_'+CONDITIONS[19]+'_'+sub+'.nii.gz')
                    except FileExistsError:
                        pass
    return




# def surfacemaps(conditions='Ant_Food_High',p_val=0.001):
#     spmconditions = glob.glob(SECONDLVL+'spmfiles/'+conditions+'/*')
#     p_uncorrected = norm.isf(p_val)
#     secondlvl = SecondLevelModel(smoothing_fwhm=8)
#     fit = secondlvl.fit(spmconditions,design_matrix=design_matrix)
#     z_map = secondlvl.compute_contrast(second_level_stat_type='t',output_type="z_score")
#     threshold_map1,threshold1 = threshold_stats_img(z_map,alpha=0.001,height_control="fdr",cluster_threshold=5,two_sided=True)
#     print(threshold1)
    # if threshold1 != 'inf':                
    #     nib.save(threshold_map1,SECONDLVL+'/spmfiles/'+conditions+'/spmT_'+conditions+'_GLOBAL_p0001_fdr.nii.gz')
    #     try:
    #         os.link(SECONDLVL+'/spmfiles/'+conditions+'/spmT_'+conditions+'_GLOBAL_p0001_fdr.nii.gz','c:/users/bprigent/Documents/Pro/MIDFID_Experiment/BILAN_AUTOMRI/spmT_'+conditions+'_GLOBAL_p0001_fdr.nii.gz')
    #     except FileExistsError:
    #         pass
    #     print('\nici')
    #     fsaverage = datasets.fetch_surf_fsaverage()
    #     curv_left = surface.load_surf_data(fsaverage.curv_left)
    #     curv_left_sign = np.sign(curv_left)
    #     textureL = surface.vol_to_surf(threshold_map1,fsaverage.pial_left)
    #     curv_right = surface.load_surf_data(fsaverage.curv_right)
    #     curv_right_sign = np.sign(curv_right)
    #     textureR = surface.vol_to_surf(threshold_map1,fsaverage.pial_right)
    #     displayL = plotting.plot_surf_stat_map(fsaverage.infl_left,textureL,hemi='left',colorbar=True,threshold=threshold1,bg_map=fsaverage.sulc_left)
    #     displayR = plotting.plot_surf_stat_map(fsaverage.infl_right,textureR,hemi='right',colorbar=True,threshold=threshold1,bg_map=fsaverage.sulc_right)
    #     displayL.savefig(SECONDLVL+'spmfiles/'+ conditions+'/'+conditions+'_Left_brain_surface.png')
    #     displayR.savefig(SECONDLVL+'spmfiles/'+ conditions+'/'+conditions+'_Right_brain_surface.png')
    #     display3D = plotting.plot_stat_map(
    #         threshold_map1,
    #         threshold=threshold1,
    #         colorbar=True,
    #         display_mode="mosaic",
    #         cut_coords=10,
    #         title='test',
    #         black_bg=True
    #     )
    #     display3D.savefig(SECONDLVL+'spmfiles/'+ conditions+'/'+conditions+'3D.png')
    #     plt.close('all')
    #     try:
    #         os.link(SECONDLVL+'spmfiles/'+ conditions+'/'+conditions+'_Left_brain_surface.png','c:/users/bprigent/Documents/Pro/MIDFID_Experiment/BILAN_AUTOMRI/Surface/'+conditions+'_Left_brain_surface_fdr.png')
    #     except FileExistsError:
    #         pass
    #     try:
    #         os.link(SECONDLVL+'spmfiles/'+ conditions+'/'+conditions+'_Right_brain_surface.png','c:/users/bprigent/Documents/Pro/MIDFID_Experiment/BILAN_AUTOMRI/Surface/'+conditions+'_Right_brain_surface_fdr.png')
    #     except FileExistsError:
    #         pass
    #     try:
    #         os.link(SECONDLVL+'spmfiles/'+ conditions+'/'+conditions+'3D.png','c:/users/bprigent/Documents/Pro/MIDFID_Experiment/BILAN_AUTOMRI/mosaicNI/'+conditions+'3D_mosaic_fdr.png')
    #     except FileExistsError:
    #         pass
    #     return
    # else:
    #     print('\nla')
    #     threshold1 = 0.001
    #     fsaverage = datasets.fetch_surf_fsaverage()
    #     curv_left = surface.load_surf_data(fsaverage.curv_left)
    #     curv_left_sign = np.sign(curv_left)
    #     textureL = surface.vol_to_surf(z_map,fsaverage.pial_left)
    #     curv_right = surface.load_surf_data(fsaverage.curv_right)
    #     curv_right_sign = np.sign(curv_right)
    #     textureR = surface.vol_to_surf(z_map,fsaverage.pial_right)
    #     displayL = plotting.plot_surf_stat_map(fsaverage.infl_left,textureL,hemi='left',colorbar=True,threshold=threshold1,bg_map=fsaverage.sulc_left)
    #     displayR = plotting.plot_surf_stat_map(fsaverage.infl_right,textureR,hemi='right',colorbar=True,threshold=threshold1,bg_map=fsaverage.sulc_right)
    #     displayL.savefig(SECONDLVL+'spmfiles/'+ conditions+'/'+conditions+'_Left_brain_surface.png')
    #     displayR.savefig(SECONDLVL+'spmfiles/'+ conditions+'/'+conditions+'_Right_brain_surface.png')
    #     display3D = plotting.plot_stat_map(
    #         z_map,
    #         threshold=threshold1,
    #         colorbar=True,
    #         display_mode="mosaic",
    #         cut_coords=10,
    #         title='test',
    #         black_bg=True
    #     )
    #     display3D.savefig(SECONDLVL+'spmfiles/'+ conditions+'/'+conditions+'3D.png')
    #     plt.close('all')
    #     try:
    #         os.link(SECONDLVL+'spmfiles/'+ conditions+'/'+conditions+'_Left_brain_surface.png','c:/users/bprigent/Documents/Pro/MIDFID_Experiment/BILAN_AUTOMRI/Surface/'+conditions+'_Left_brain_surface_nofdr.png')
    #     except FileExistsError:
    #         pass
    #     try:
    #         os.link(SECONDLVL+'spmfiles/'+ conditions+'/'+conditions+'_Right_brain_surface.png','c:/users/bprigent/Documents/Pro/MIDFID_Experiment/BILAN_AUTOMRI/Surface/'+conditions+'_Right_brain_surface_nofdr.png')
    #     except FileExistsError:
    #         pass
    #     try:
    #         os.link(SECONDLVL+'spmfiles/'+ conditions+'/'+conditions+'3D.png','c:/users/bprigent/Documents/Pro/MIDFID_Experiment/BILAN_AUTOMRI/mosaicNI/'+conditions+'3D_mosaic_nofdr.png')
    #     except FileExistsError:
    #         pass
    # return


def surfacemaps(conditions='Ant_Food_High',p_val=0.001):
    spmconditions = glob.glob(SECONDLVL+'spmfiles/'+conditions+'/*')
    p_uncorrected = norm.isf(p_val)
    secondlvl = SecondLevelModel(smoothing_fwhm=8)
    fit = secondlvl.fit(spmconditions,design_matrix=design_matrix)
    z_map = secondlvl.compute_contrast(second_level_stat_type='t',output_type="z_score")
    threshold_map1,threshold1 = threshold_stats_img(z_map,alpha=0.001,height_control="fdr",cluster_threshold=5,two_sided=True)                
    nib.save(z_map,SECONDLVL+'/spmfiles/'+conditions+'/spmT_'+conditions+'_GLOBAL_p0001_fdr.nii.gz')
    try:
        os.link(SECONDLVL+'/spmfiles/'+conditions+'/spmT_'+conditions+'_GLOBAL_p0001_fdr.nii.gz','c:/users/bprigent/Documents/Pro/MIDFID_Experiment/BILAN_AUTOMRI/spmT_'+conditions+'_GLOBAL_p0001_fdr.nii.gz')
    except FileExistsError:
        pass
    fsaverage = datasets.fetch_surf_fsaverage()
    curv_left = surface.load_surf_data(fsaverage.curv_left)
    curv_left_sign = np.sign(curv_left)
    textureL = surface.vol_to_surf(z_map,fsaverage.pial_left)
    curv_right = surface.load_surf_data(fsaverage.curv_right)
    curv_right_sign = np.sign(curv_right)
    textureR = surface.vol_to_surf(z_map,fsaverage.pial_right)
    displayL = plotting.plot_surf_stat_map(fsaverage.infl_left,textureL,hemi='left',colorbar=True,threshold=threshold1,bg_map=fsaverage.sulc_left)
    displayR = plotting.plot_surf_stat_map(fsaverage.infl_right,textureR,hemi='right',colorbar=True,threshold=threshold1,bg_map=fsaverage.sulc_right)
    displayL.savefig(SECONDLVL+'spmfiles/'+ conditions+'/'+conditions+'_Left_brain_surface.png')
    displayR.savefig(SECONDLVL+'spmfiles/'+ conditions+'/'+conditions+'_Right_brain_surface.png')
    display3D = plotting.plot_stat_map(
        z_map,
        threshold=0.1,
        colorbar=True,
        display_mode="mosaic",
        cut_coords=10,
        title='test',
        black_bg=True
    )
    display3D.savefig(SECONDLVL+'spmfiles/'+ conditions+'/'+conditions+'3D.png')
    plt.close('all')
    try:
        os.link(SECONDLVL+'spmfiles/'+ conditions+'/'+conditions+'_Left_brain_surface.png','c:/users/bprigent/Documents/Pro/MIDFID_Experiment/BILAN_AUTOMRI/Surface/'+conditions+'_Left_brain_surface.png')
    except FileExistsError:
        pass
    try:
        os.link(SECONDLVL+'spmfiles/'+ conditions+'/'+conditions+'_Right_brain_surface.png','c:/users/bprigent/Documents/Pro/MIDFID_Experiment/BILAN_AUTOMRI/Surface/'+conditions+'_Right_brain_surface.png')
    except FileExistsError:
        pass
    try:
        os.link(SECONDLVL+'spmfiles/'+ conditions+'/'+conditions+'3D.png','c:/users/bprigent/Documents/Pro/MIDFID_Experiment/BILAN_AUTOMRI/mosaicNI/'+conditions+'3D_mosaic.png')
    except FileExistsError:
        pass
    return
    
for conditions in CONDITIONS:
    surfacemaps(conditions)
