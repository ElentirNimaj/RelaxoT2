#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

# ============================================= #
# 1st and 2nd Lvl
# B. Prigent
# v 1, 13-Apr-2023
# ============================================= #
"""
    Script to realize a first and second level analyzis by using fMRIPrep derivates
"""

# %% 0 - Library

import os 
import json
import nipype
from nipype.interfaces.spm import Level1Design, EstimateModel, EstimateContrast
from nipype.algorithms.modelgen import SpecifySPMModel
from nipype.interfaces.utility import Function, IdentityInterface
from nipype.interfaces.io import SelectFiles, DataSink
from nipype.interfaces.base import Bunch
from nipype import Workflow, Node
import panda as pd

# %% 1- Folders
EXPERIMENT_DIR = 'c:/users/bprigent/Documents/Pro/MIDFID_Expermiement/Data/BIDS/'
OUTPUT_DIR = 'c:/users/bprigent/Documents/Pro/MIDFID_Expermiement/Data/BIDS/GLM/'
WORKING_DIR = 'c:/users/bprigent/Documents/Pro/MIDFID_Expermiement/Data/BIDS/workdir/'

try:
    os.makedirs(EXPERIMENT_DIR)
except FileExistsError:
    pass
try:
    os.makedirs(OUTPUT_DIR)
except FileExistsError:
    pass
try:
    os.makedirs(WORKING_DIR)
except FileExistsError:
    pass



subject_list = ['A01','A02','A03','A04','A05','A06','A07','A08','A09','A10','A11','A12','A13','A14','A15']

with open(EXPERIMENT_DIR+'rawdata/derivates/sub-A01/func/sub-A01_task-midnirs_space-MNI152NLin2009cAsym_desc-preproc_bold.json','rt') as fp:
    task_info = json.load(fp)
TR = task_info['RepetitionTime']

fwhm = [4,8]

# %% 2- Nodes

# SpecifyModel - SPM-specific
modelspec = Node(SpecifySPMModel(concatenate_runs=False,
                                 input_units='secs',
                                 output_units='secs',
                                 time_repetition=TR,
                                 high_pass_filter_cutoff=128),
                 name="modelspec")

# 1Lvl design - design matrix
level1st = Node(Level1Design(bases={'htf': {'derivs':[0,0]}},
                             timing_units='secs',
                             interscan_interval=TR,
                             model_serialçcorrelations='FAST'),
                name="level1st")

# Estimate model - estimate parameters 
level1stestimate = Node(EstimateModel(estimation_method={"Classical":1}),
                        name="level1stestimate")

#EstimateContrast - estimates contrasts
level1conest = Node(EstimateContrast(),name="level1conest")

# %% 3- Conditions and Contrast

#Conditions

TASKNAME = ['AntFoodHigh','AntMoneyHigh','AntFoodNo','AntMoneyNo','AntFoodLow','AntMoneyLow', 'RewFoodHigh','RewMoneyHigh','RewFoodNo','RewMoneyNo','RewFoodLow','RewMoneyLow','RewFoodNo30','RewMoneyNo30']

#Contrasts

cont01 = ['Ant_Food_High',              'T',TASKNAME,[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
cont03 = ['Ant_Money_High',             'T',TASKNAME,[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
cont02 = ['Ant_Food_No',                'T',TASKNAME,[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
cont04 = ['Ant_Money_No',               'T',TASKNAME,[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]]

cont05 = ['Ant_Food_HighvsNo',          'T',TASKNAME,[1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]]
cont06 = ['Ant_Money_HighvsNo',         'T',TASKNAME,[0, 0, 0, 1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0,]]

cont07 = ['Rew_Food_Hig',               'T',TASKNAME,[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]]
cont08 = ['Rew_Food_No',                'T',TASKNAME,[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]
cont09 = ['Rew_Money_High',             'T',TASKNAME,[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]]
cont10 = ['Rew_Money_No',               'T',TASKNAME,[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]

cont11 = ['Rew_Food_HighvsNo',          'T',TASKNAME,[0, 0, 0, 0, 0, 0, 1, 0, -1, 0, 0, 0, 0, 0]]
cont12 = ['Rew_Money_HighvsNo',         'T',TASKNAME,[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, -1, 0, 0]]

cont13 = ['Ant_FoodAndMoney_High',      'T',TASKNAME,[1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
cont14 = ['Ant_FoodAndMoney_HighvsNo',  'T',TASKNAME,[1, 0, -1, 1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0]]
cont15 = ['Rew_FoodAndMoney_High',      'T',TASKNAME,[0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,]]
cont16 = ['Rew_FoodAndMoney_HighvsNo',  'T',TASKNAME,[0, 0, 0, 0, 0, 0, 1, 0, -1, 1, 0, -1, 0, 0,]]

cont17 = ['Ant_FoodvsMoney_High',       'T',TASKNAME,[1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
cont18 = ['Rew_FoodvsMoney_High',       'T',TASKNAME,[0, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, 0, 0, 0]]
cont19 = ['Ant_FoodvsMoney_HighvsNo',   'T',TASKNAME,[1, 0, -1, -1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]]
cont20 = ['Rew_FoodvsMoney_HighvsNo',   'T',TASKNAME,[0, 0, 0, 0, 0, 0, 1, 0, -1, -1, 0, 1, 0, 0]]

contrast_list = [cont01,cont02,cont03,cont04,cont05,cont06,cont07,cont08,cont09,cont10,cont11,
                 cont12,cont13,cont14,cont15,cont16,cont17,cont18,cont19,cont20]

def subjectinfo(subject_id):
    trialinfo = pd.read_table(EXPERIMENT_DIR+'rawdata/sub-'+subject_id+'/func/sub-'+subject_id+'_task-midnirs_events.tsv')
    trialinfo.head()
    task = []
    onsets = []
    durations=[]
    for group in trialinfo.groupby('trial_type'):
        task.append(group[0])
        onsets.append([group[1].onset])
        duration.append(group[1].duration.tolist())
        
    subject_info = [Bunch(task=task,
                          onsets=onsets,
                          durations=durations,
                        )]
    return subject_info

getsubjectinfo = Node(Function(input_names=['subject_id'],
                               output_names=['subject_info'],
                               function=subjectinfo),
                      name='getsubjectinfo')

# %% 3- Input & output stram

# Infosource - function freenode to iterate over the list of subject names
infosource = Node(IdentityInterface(fields=['subject_id',
                                            'fwhm_id',
                                            'contrasts'],
                                    contrasts=contrast_list),
                  name="infosource")