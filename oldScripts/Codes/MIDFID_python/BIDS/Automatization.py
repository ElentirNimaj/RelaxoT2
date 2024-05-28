#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

# ============================================= #
# Automatization of task
# B. Prigent
# v 1, 15-May-2023
# ============================================= #
"""
    Script to accelerate treatment of files to have them in a unique folder
"""
# %% 0- Library
import os
import shutil
import numpy as np
import pandas as pan

# %% 1- Folder and hardlink to have all files in one place

folder_origin = str(input('Name of the origin folder : '))
folder_destination = str(input('Name of the destination folder : '))
ORIGINE ="C:/Users/bprigent/Documents/Pro/MIDFID_Experiment/MIDFID_AutoMRI/autofmri_analysis_dir/"
DESTINATION = "C:/Users/bprigent/Documents/Pro/MIDFID_Experiment/AutoMRI_final/"

while os.path.isdir(ORIGINE+folder_origin) == False:
    print('\n Folder name not recognize')
    folder_origin = str(input('Name of the origin folder : '))
    

def AutoFolder(endfolder=folder_destination):
    try:
        os.mkdir(DESTINATION + endfolder+ '/')
    except FileExistsError:
        pass
    try:
        os.mkdir(DESTINATION + endfolder+ '/' + 'p0_001')
    except FileExistsError:
        pass
    try: 
        os.mkdir(DESTINATION + endfolder+ '/' + 'p0_05')
    except FileExistsError:
        pass
    try: 
        os.mkdir(DESTINATION + endfolder+ '/' + 'AllContrastsOneROI')
    except FileExistsError:
        pass
    try:        
        os.mkdir(DESTINATION + endfolder+ '/' + 'AllROIOneContrast')
    except FileExistsError:
        pass
    return


def Autoclean(startdir=folder_origin,endfolder=folder_destination):
    for folder in os.listdir(ORIGINE+startdir+"/Analysis_2nd_level/gr_A/"):
        endir = ORIGINE+startdir + "/Analysis_2nd_level/gr_A/" + folder +'/stat_map_plots/'
        map = os.listdir(endir)
        try:
            os.link(endir+map[0],DESTINATION+endfolder+'/p0_001/'+map[0])
        except FileExistsError:
            pass
        try:
            os.link(endir+map[1],DESTINATION+endfolder+'/p0_05/'+map[1])
        except FileExistsError:
            pass
        endir = ORIGINE+ startdir + "/Analysis_ROI/MIDFID/"
        try:
            os.link(endir+"individual_avg_contrasts_in_ROIs.csv",DESTINATION + endfolder+ '/')
        except FileExistsError:
            pass
        endir = endir + "all_contrasts_in_one_roi/"
        map = os.listdir(endir)
        for contrast in map:
            try:
                os.link(endir + contrast,DESTINATION + endfolder+'/AllContrastsOneROI/'+contrast)
            except FileExistsError:
                pass
        endir = ORIGINE+startdir + "/Analysis_ROI/MIDFID/all_rois_in_one_contrast/"
        map = os.listdir(endir)
        for contrast in map:
            try:
                os.link(endir + contrast,DESTINATION + endfolder+'/AllROIOneContrast/'+contrast)
            except FileExistsError:
                pass
    return
# %% 2- Modify CSV, add column and data
def AllinOneCSV(startdir=folder_origin,endfolder=folder_destination):
    Avg_Contrast = pan.read_csv(ORIGINE+startdir+'/Analysis_ROI/MIDFID/individual_avg_contrasts_in_ROIs.csv')

    conditions = [
        (Avg_Contrast['Subject'] == 'A01'),(Avg_Contrast['Subject'] == 'A02'),
        (Avg_Contrast['Subject'] == 'A03'),(Avg_Contrast['Subject'] == 'A04'),
        (Avg_Contrast['Subject'] == 'A05'),(Avg_Contrast['Subject'] == 'A06'),
        (Avg_Contrast['Subject'] == 'A07'),(Avg_Contrast['Subject'] == 'A08'),
        (Avg_Contrast['Subject'] == 'A09'),(Avg_Contrast['Subject'] == 'A10'),
        (Avg_Contrast['Subject'] == 'A11'),(Avg_Contrast['Subject'] == 'A12'),
        (Avg_Contrast['Subject'] == 'A13'),(Avg_Contrast['Subject'] == 'A14'),
        (Avg_Contrast['Subject'] == 'A15')
    ]

    value_age = [30,21,19,43,32,21,33,20,30,30,30,18,36,37,30]
    value_genre = ["Femme","Homme","Femme","Homme","Femme","Femme","Homme",
                "Femme","Femme","Homme","Femme","Femme","Femme","Homme","Homme"]

    Avg_Contrast['Age'] = np.select(conditions,value_age)
    Avg_Contrast['Genre'] = np.select(conditions,value_genre)

    Avg_Contrast.to_excel(DESTINATION+'/'+endfolder+'/'+endfolder+'_AvgContrast.xlsx', index=False)
    
    return

AutoFolder()
Autoclean()
AllinOneCSV()


print('\n*- End of the script -*')

