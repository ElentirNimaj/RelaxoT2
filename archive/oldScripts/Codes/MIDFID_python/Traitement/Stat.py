#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

# ============================================= #
# Automatization of task
# B. Prigent
# v 1, 15-May-2023
# ============================================= #
"""
    Script to make stat with resulsts from pyautomri
"""

import os
import shutil
import numpy as np
import scipy as sci
import pandas as pan

D01 = pan.read_excel("c:/users/bprigent/Documents/MIDFID/Few_test/d01_AnticipationAndReward/AllResults.xlsx",sheet_name='D01_AntRew')


conditions = ["""Contrast 0001 "Ant Food High" """,
"""Contrast 0001 "Ant Food High" """,
"""Contrast 0002 "Ant Food No" """,
"""Contrast 0003 "Ant Money High" """,
"""Contrast 0004 "Ant Money No" """,
"""Contrast 0005 "Ant Food HighvsNo" """,
"""Contrast 0006 "Ant Money HighvsNo" """,
"""Contrast 0007 "Rew Food High" """,
"""Contrast 0008 "Rew Food No" """,
"""Contrast 0009 "Rew Money High" """,
"""Contrast 0010 "Rew Money No" """,
"""Contrast 0011 "Rew Food HighvsNo" """,
"""Contrast 0012 "Rew Money HighvsNo" """,
"""Contrast 0013 "Ant FoodAndMoney High" """,
"""Contrast 0014 "Ant FoodAndMoney HighvsNo" """,
"""Contrast 0015 "Rew FoodAndMoney High" """,
"""Contrast 0016 "Rew FoodAndMoney HighvsNo" """,
"""Contrast 0017 "Ant FoodvsMoney High" """,
"""Contrast 0018 "Rew FoodvsMoney High" """,
]

Acc = D01[(D01["ROI"]) == "ACC"] 
df_ACC = pan.DataFrame(columns=['Condition','Moy','Med','q1','q3','max','Sub Max','min','Sub Min'])

contrast_index = (Acc["Contrast index"])
for contrast in range(1,19):
    contrast_punctual = Acc[Acc["Contrast index"] == contrast]
    contrast_value = contrast_punctual['Value']
    avg = np.average(contrast_value)
    med = np.median(contrast_value)
    q1 = np.percentile(contrast_value,25)
    q3 = np.percentile(contrast_value,75)
    maxi = max(contrast_value)
    mini = min(contrast_value)
    sub_max = Acc[Acc["Value"] == maxi]
    sub_max = sub_max.iat[0,2]
    sub_min = Acc[Acc["Value"] == mini]
    sub_min = sub_min.iat[0,2]
    df_ACC.loc[contrast] = [conditions[contrast],avg,med,q1,q3,maxi,sub_max,mini,sub_min]
    

NAcc = D01[(D01["ROI"]) == "Accumbens"] 
df_NAcc = pan.DataFrame(columns=['Condition','Moy','Med','q1','q3','max','Sub Max','min','Sub Min'])

contrast_index = (NAcc["Contrast index"])
for contrast in range(1,19):
    contrast_punctual = NAcc[NAcc["Contrast index"] == contrast]
    contrast_value = contrast_punctual['Value']
    avg = np.average(contrast_value)
    med = np.median(contrast_value)
    q1 = np.percentile(contrast_value,25)
    q3 = np.percentile(contrast_value,75)
    maxi = max(contrast_value)
    mini = min(contrast_value)
    sub_max = NAcc[NAcc["Value"] == maxi]
    sub_max = sub_max.iat[0,2]
    sub_min = NAcc[NAcc["Value"] == mini]
    sub_min = sub_min.iat[0,2]
    df_NAcc.loc[contrast] = [conditions[contrast],avg,med,q1,q3,maxi,sub_max,mini,sub_min]
    

Caude = D01[(D01["ROI"]) == "Caude"] 
df_Caude = pan.DataFrame(columns=['Condition','Moy','Med','q1','q3','max','Sub Max','min','Sub Min'])

contrast_index = (Caude["Contrast index"])
for contrast in range(1,19):
    contrast_punctual = Caude[Caude["Contrast index"] == contrast]
    contrast_value = contrast_punctual['Value']
    avg = np.average(contrast_value)
    med = np.median(contrast_value)
    q1 = np.percentile(contrast_value,25)
    q3 = np.percentile(contrast_value,75)
    maxi = max(contrast_value)
    mini = min(contrast_value)
    sub_max = Caude[Caude["Value"] == maxi]
    sub_max = sub_max.iat[0,2]
    sub_min = Caude[Caude["Value"] == mini]
    sub_min = sub_min.iat[0,2]
    df_Caude.loc[contrast] = [conditions[contrast],avg,med,q1,q3,maxi,sub_max,mini,sub_min]
    

Putamen = D01[(D01["ROI"]) == "Putamen"] 
df_Putamen = pan.DataFrame(columns=['Condition','Moy','Med','q1','q3','max','Sub Max','min','Sub Min'])

contrast_index = (Putamen["Contrast index"])
for contrast in range(1,19):
    contrast_punctual = Putamen[Putamen["Contrast index"] == contrast]
    contrast_value = contrast_punctual['Value']
    avg = np.average(contrast_value)
    med = np.median(contrast_value)
    q1 = np.percentile(contrast_value,25)
    q3 = np.percentile(contrast_value,75)
    maxi = max(contrast_value)
    mini = min(contrast_value)
    sub_max = Putamen[Putamen["Value"] == maxi]
    sub_max = sub_max.iat[0,2]
    sub_min = Putamen[Putamen["Value"] == mini]
    sub_min = sub_min.iat[0,2]
    df_Putamen.loc[contrast] = [conditions[contrast],avg,med,q1,q3,maxi,sub_max,mini,sub_min]
    
    
Thal = D01[(D01["ROI"]) == "Thalamus"] 
df_Thal = pan.DataFrame(columns=['Condition','Moy','Med','q1','q3','max','Sub Max','min','Sub Min'])

contrast_index = (Thal["Contrast index"])
for contrast in range(1,19):
    contrast_punctual = Thal[Thal["Contrast index"] == contrast]
    contrast_value = contrast_punctual['Value']
    avg = np.average(contrast_value)
    med = np.median(contrast_value)
    q1 = np.percentile(contrast_value,25)
    q3 = np.percentile(contrast_value,75)
    maxi = max(contrast_value)
    mini = min(contrast_value)
    sub_max = Thal[Thal["Value"] == maxi]
    sub_max = sub_max.iat[0,2]
    sub_min = Thal[Thal["Value"] == mini]
    sub_min = sub_min.iat[0,2]
    df_Thal.loc[contrast] = [conditions[contrast],avg,med,q1,q3,maxi,sub_max,mini,sub_min]
    
    
VTA = D01[(D01["ROI"]) == "VTA"] 
df_VTA = pan.DataFrame(columns=['Condition','Moy','Med','q1','q3','max','Sub Max','min','Sub Min'])

contrast_index = (VTA["Contrast index"])
for contrast in range(1,19):
    contrast_punctual = VTA[VTA["Contrast index"] == contrast]
    contrast_value = contrast_punctual['Value']
    avg = np.average(contrast_value)
    med = np.median(contrast_value)
    q1 = np.percentile(contrast_value,25)
    q3 = np.percentile(contrast_value,75)
    maxi = max(contrast_value)
    mini = min(contrast_value)
    sub_max = VTA[VTA["Value"] == maxi]
    sub_max = sub_max.iat[0,2]
    sub_min = VTA[VTA["Value"] == mini]
    sub_min = sub_min.iat[0,2]
    df_VTA.loc[contrast] = [conditions[contrast],avg,med,q1,q3,maxi,sub_max,mini,sub_min]
    
    
with pan.ExcelWriter("c:/users/bprigent/Documents/MIDFID/Few_test/d01_AnticipationAndReward/AllResults_Stat.xlsx") as writer:
    df_ACC.to_excel(writer, sheet_name="ACC", index=False)
    df_NAcc.to_excel(writer, sheet_name="Accumbens", index=False)
    df_Caude.to_excel(writer, sheet_name="Caude", index=False)
    df_Putamen.to_excel(writer, sheet_name="Putamen", index=False)
    df_Thal.to_excel(writer, sheet_name="Thalamus", index=False)
    df_VTA.to_excel(writer, sheet_name="VTA", index=False)
    