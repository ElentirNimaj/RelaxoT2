# -*- coding: utf-8 -*- #

# ============================================= #
# BIDS Folder
# B. Prigent
# v 2, 16--2Jun023
# ============================================= #
"""
    Script to create global onset file
"""

# %% 0 - Library
import os
import pandas as pan
import shutil
import numpy as np
import tkinter as tk
from tkinter.filedialog import askdirectory
import LibraryjsAndtsv as lib
# %% 1 - read and sort data

BIDSpath = "C:/Users/bprigent/Documents/Pro/MIDFID_Experiment/Data/"
MIDFIDDIR = "C:/Users/bprigent/Code/Python_files/MIDFID_python/"
BIDS = BIDSpath+"BIDS/"
ONSETPATH = "C:/Users/bprigent/Documents/Pro/MIDFID_Experiment/Data/onsets/"
ONSETSUBJECT = os.listdir(ONSETPATH)
ONSETAUTOMRI_PATH = "C:/Users/bprigent/Documents/Pro/MIDFID_Experiment/MIDFID_AutoMRI/onsets/"

def rm_old_tsv():
    for onset_index in ONSETSUBJECT:
        try:
            os.remove(ONSETPATH+onset_index+'/onsets_su_'+onset_index+'_se_mid_NIRS_bold_ant_no_rew_food.txt')
        except FileNotFoundError:
            pass
        try:
            os.remove(ONSETPATH+onset_index+'/onsets_su_'+onset_index+'_se_mid_NIRS_bold_ant_no_rew_money.txt')
        except FileNotFoundError:
            pass 
        try:
            os.remove(ONSETPATH+onset_index+'/onsets_su_'+onset_index+'_se_mid_NIRS_bold_ant_rew_food.txt')
        except FileNotFoundError:
            pass
        try:
            os.remove(ONSETPATH+onset_index+'/onsets_su_'+onset_index+'_se_mid_NIRS_bold_ant_rew_money.txt')
        except FileNotFoundError:
            pass
        try:
            os.remove(ONSETPATH+onset_index+'/onsets_su_'+onset_index+'_se_mid_NIRS_bold_no_rew_food.txt')
        except FileNotFoundError:
            pass
        try:
            os.remove(ONSETPATH+onset_index+'/onsets_su_'+onset_index+'_se_mid_NIRS_bold_no_rew_money.txt')
        except FileNotFoundError:
            pass
        try:
            os.remove(ONSETPATH+onset_index+'/onsets_su_'+onset_index+'_se_mid_NIRS_bold_rew_food.txt')
        except FileNotFoundError:
            pass
        try:
            os.remove(ONSETPATH+onset_index+'/onsets_su_'+onset_index+'_se_mid_NIRS_bold_rew_money.txt')
        except FileNotFoundError:
            pass
    return

def concatenate_onset():
    for onset_index in ONSETSUBJECT:
        TASKNAME = ['AntFoodHigh','AntMoneyHigh','AntFoodNo','AntMoneyNo','AntFoodLow','AntMoneyLow', 'RewFoodHigh','RewMoneyHigh','RewFoodNo','RewMoneyNo','RewFoodLow','RewMoneyLow','RewFoodNo30','RewMoneyNo30']
        onset = os.listdir(ONSETPATH+onset_index)
        onset_base = pan.read_csv(ONSETPATH+onset_index+'/onsets_su_'+onset_index+'_se_mid_NIRS_bold_ant_high_food.txt',header=None)
        onset_base.columns = ['onset']
        onset_base['duration'] = 3.7
        onset_base['trial_type'] = TASKNAME[0]
        onset_number = 1
        print(onset_base)
        for onset_txt in onset[1:14]:
            onset_punctual = pan.read_csv(ONSETPATH+onset_index+'/'+onset_txt,header=None)
            onset_punctual.columns = ['onset']
            if onset_txt.find('ant',30) != -1:
                onset_punctual['duration'] = 3.7
            else:
                onset_punctual['duration'] = 1.5
            onset_punctual['trial_type'] = TASKNAME[onset_number]
            onset_base = pan.concat([onset_base, onset_punctual], axis="rows",ignore_index=True)
            onset_number += 1
        onset_base.sort_values(by=['onset'],inplace=True)
        try:
            onset_base.to_csv(BIDS+"rawdata/sub-"+onset_index+'/func/sub-'+onset_index+'_task-midnirs_events.tsv', sep = "\t",index=False)
        except FileExistsError:
            os.remove(BIDS+"rawdata/sub-"+onset_index+'/func/sub-'+onset_index+'_task-midnirs_events.tsv') 
            onset_base.to_csv(BIDS+"rawdata/sub-"+onset_index+'/func/sub-'+onset_index+'_task-midnirs_events.tsv', sep = "\t",index=False)
        try:
            with open(BIDS+"rawdata/sub-"+onset_index+'/func/sub-'+onset_index+'_task-midnirs_events.json','w') as ejson:
                ejson.write(lib.event_json)
        except FileExistsError:
            os.remove(BIDS+"rawdata/sub-"+onset_index+'/func/sub-'+onset_index+'_task-midnirs_events.json') 
            with open(BIDS+"rawdata/sub-"+onset_index+'/func/sub-'+onset_index+'_task-midnirs_events.json','w') as ejson:
                ejson.write(lib.event_json)
    return

def onset_AutoMRI():
    TASKNAME = ['AntFoodHigh','AntMoneyHigh','AntFoodNo','AntMoneyNo','AntFoodLow','AntMoneyLow', 'RewFoodHigh','RewMoneyHigh','RewFoodNo','RewMoneyNo','RewFoodLow','RewMoneyLow','RewFoodNo30','RewMoneyNo30']
    try:
        os.makedirs(ONSETAUTOMRI_PATH)
    except FileExistsError:
        pass
    for onset_index in ONSETSUBJECT:
        onset = os.listdir(ONSETPATH+onset_index)
        try:
            os.makedirs(ONSETAUTOMRI_PATH+'su_'+onset_index)
        except FileExistsError:
            pass
        for onset_txt in range(0,14):
            try:
                os.link(ONSETPATH+onset_index+'/'+onset[onset_txt],ONSETAUTOMRI_PATH+'su_'+onset_index+'/'+'onsets_su_'+onset_index+'_se_midnirs_'+TASKNAME[onset_txt]+'.txt')
            except FileExistsError:
                pass
            
concatenate_onset()