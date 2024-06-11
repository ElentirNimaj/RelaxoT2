# -*- coding: utf-8 -*- #

# ============================================= #
# BIDS Folder
# B. Prigent
# v 1, 13-Apr-2023
# ============================================= #
"""
    Script to create global onset file
"""

# %% 0 - Library
import os
import pandas as pan
import shutil
import numpy as np
# %% 1 - read and sort data

ORIGINE = 'c:/users/bprigent/Documents/Pro/MIDFID_Experiment/Data/onsets/'
DESTINATION = 'c:/users/bprigent/Documents/Pro/MIDFID_Experiment/MIDFID_AutoMRI/onsets/'
print(os.listdir(ORIGINE))
def creation_folder():
    try:
        os.makedirs(DESTINATION)
        print('AH')
    except FileExistsError:
        pass
    for index_subject in range(1,16):
        label = str(index_subject)
        if index_subject <= 9:
            subject = 'su_A0'+label
        else:
            subject = 'su_A'+label
        try:
            os.makedirs(DESTINATION+subject)
        except FileExistsError:
            pass
    return

creation_folder()

for folder in os.listdir(ORIGINE):
    try:
        os.link(ORIGINE+folder+'/onsets_su_'+folder+'_se_mid_NIRS_bold_ant_high_food.txt',DESTINATION+'/su_'+folder+'/onsets_su_'+folder+'_se_midnirs_AntFoodHigh.txt')
    except FileExistsError:
        pass 
    try:
        os.link(ORIGINE+folder+'/onsets_su_'+folder+'_se_mid_NIRS_bold_ant_high_money.txt',DESTINATION+'/su_'+folder+'/onsets_su_'+folder+'_se_midnirs_AntMoneyHigh.txt')
    except FileExistsError:
        pass
    try:
        os.link(ORIGINE+folder+'/onsets_su_'+folder+'_se_mid_NIRS_bold_ant_low_food.txt',DESTINATION+'/su_'+folder+'/onsets_su_'+folder+'_se_midnirs_AntFoodNo.txt')
    except FileExistsError:
        pass
    try:
        os.link(ORIGINE+folder+'/onsets_su_'+folder+'_se_mid_NIRS_bold_ant_low_money.txt',DESTINATION+'/su_'+folder+'/onsets_su_'+folder+'_se_midnirs_AntMoneyNo.txt')
    except FileExistsError:
        pass
    try:
        os.link(ORIGINE+folder+'/onsets_su_'+folder+'_se_mid_NIRS_bold_ant_mid_food.txt',DESTINATION+'/su_'+folder+'/onsets_su_'+folder+'_se_midnirs_AntFoodLow.txt')
    except FileExistsError:
        pass
    try:
        os.link(ORIGINE+folder+'/onsets_su_'+folder+'_se_mid_NIRS_bold_ant_mid_money.txt',DESTINATION+'/su_'+folder+'/onsets_su_'+folder+'_se_midnirs_AntMoneyLow.txt')
    except FileExistsError:
        pass
    try:
        os.link(ORIGINE+folder+'/onsets_su_'+folder+'_se_mid_NIRS_bold_high_food.txt',DESTINATION+'/su_'+folder+'/onsets_su_'+folder+'_se_midnirs_RewFoodHigh.txt')
    except FileExistsError:
        pass
    try:
        os.link(ORIGINE+folder+'/onsets_su_'+folder+'_se_mid_NIRS_bold_high_money.txt',DESTINATION+'/su_'+folder+'/onsets_su_'+folder+'_se_midnirs_RewMoneyHigh.txt')
    except FileExistsError:
        pass
    try:
        os.link(ORIGINE+folder+'/onsets_su_'+folder+'_se_mid_NIRS_bold_low_food.txt',DESTINATION+'/su_'+folder+'/onsets_su_'+folder+'_se_midnirs_RewFoodNo.txt')
    except FileExistsError:
        pass
    try:
        os.link(ORIGINE+folder+'/onsets_su_'+folder+'_se_mid_NIRS_bold_low_money.txt',DESTINATION+'/su_'+folder+'/onsets_su_'+folder+'_se_midnirs_RewMoneyNo.txt')
    except FileExistsError:
        pass
    try:
        os.link(ORIGINE+folder+'/onsets_su_'+folder+'_se_mid_NIRS_bold_mid_food.txt',DESTINATION+'/su_'+folder+'/onsets_su_'+folder+'_se_midnirs_RewFoodLow.txt')
    except FileExistsError:
        pass
    try:
        os.link(ORIGINE+folder+'/onsets_su_'+folder+'_se_mid_NIRS_bold_mid_money.txt',DESTINATION+'/su_'+folder+'/onsets_su_'+folder+'_se_midnirs_RewMoneyLow.txt')
    except FileExistsError:
        pass
    try:
        os.link(ORIGINE+folder+'/onsets_su_'+folder+'_se_mid_NIRS_bold_no_food.txt',DESTINATION+'/su_'+folder+'/onsets_su_'+folder+'_se_midnirs_RewFoodNo30.txt')
    except FileExistsError:
        pass
    try:
        os.link(ORIGINE+folder+'/onsets_su_'+folder+'_se_mid_NIRS_bold_no_money.txt',DESTINATION+'/su_'+folder+'/onsets_su_'+folder+'_se_midnirs_RewMoneyNo30.txt')
    except FileExistsError:
        pass
    
    