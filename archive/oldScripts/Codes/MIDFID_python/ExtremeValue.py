# ============================================== #
#Extreme value - MIDFID
#B.Prigent
#v 0, 29-Jun-2023
# ============================================== #

# %% 0- Library 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os 

TABLE = 'C:/Users/bprigent/Documents/Pro/MIDFID_Experiment/BILAN_AUTOMRI/D01Avg_ROI.xlsx'
ROI = ['Accumbens','VTA','ACC','Caude','Putamen','Thalamus']
CONTRAST = [
'Contrast 0001 "Ant Food High"',
'Contrast 0002 "Ant Food No"',
'Contrast 0003 "Ant Money High"',
'Contrast 0004 "Ant Money No"',
'Contrast 0005 "Ant Food HighvsNo"',
'Contrast 0006 "Ant Money HighvsNo"',
'Contrast 0007 "Rew Food High"',
'Contrast 0008 "Rew Food No"',
'Contrast 0009 "Rew Money High"',
'Contrast 0010 "Rew Money No"',
'Contrast 0011 "Rew Food HighvsNo"',
'Contrast 0012 "Rew Money HighvsNo"',
'Contrast 0013 "Ant FoodAndMoney High"',
'Contrast 0014 "Ant FoodAndMoney HighvsNo"',
'Contrast 0015 "Rew FoodAndMoney High"',
'Contrast 0016 "Rew FoodAndMoney HighvsNo"',
'Contrast 0017 "Ant FoodvsMoney High"',
'Contrast 0018 "Rew FoodvsMoney High"',
'Contrast 0019 "Ant FoodvsMoney HighvsNo"',
'Contrast 0020 "Rew FoodvsMoney HighvsNo"'
]

ExcelTable = pd.read_excel(TABLE)


# %% Create filter and table
def filtertable (table=ExcelTable):
    ExtremeValue = pd.DataFrame.from_dict({'ROI':[],'Contrast':[],'Highest subject':[],'1st vs 2nd up':[],'Genre up':[],'Age up':[],'Lowest subject':[],'1st vs 2nd down':[],'Genre down':[],'Age down':[]})
    for region in ROI:
        for conditions in CONTRAST:
            mask_roi = ExcelTable[ExcelTable.values == region]
            mask_contrast = mask_roi[mask_roi.values == conditions]
            sorted_table = mask_contrast.sort_values(by=['Value'],ascending=False,ignore_index=True)
            diff_up = sorted_table.loc[0,'Value'] - sorted_table.loc[1,'Value']
            diff_down = sorted_table.loc[14,'Value'] - sorted_table.loc[13,'Value']
            subject_up = sorted_table.loc[0,'Subject']
            subject_down = sorted_table.loc[14,'Subject']
            genre_up = sorted_table.loc[0,'Genre']
            genre_down = sorted_table.loc[14,'Genre']
            age_up = sorted_table.loc[0,'Age']
            age_down = sorted_table.loc[14,'Age']
            ExtremeValue = ExtremeValue.append({'ROI':region,'Contrast':conditions,'Highest subject':subject_up,'1st vs 2nd up':diff_up,'Genre up':genre_up,'Age up':age_up,'Lowest subject':subject_down,'1st vs 2nd down':diff_down,'Genre down':genre_down,'Age down':age_down},ignore_index=True)
    return ExtremeValue

Output_table = filtertable()
Output_table.to_excel('c:/users/bprigent/Documents/Pro/MIDFID_Experiment/BILAN_AUTOMRI/ExtremeValueCompare.xlsx')
print(""" /* END OF THE SCRIPT *\ """)