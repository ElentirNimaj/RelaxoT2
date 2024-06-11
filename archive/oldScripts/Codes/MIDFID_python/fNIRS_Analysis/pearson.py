#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

# ============================================= #
# Pearson for fnirs
# B. Prigent
# v 1, 17-Jul-2023
# ============================================= #
"""
    Script to retrieve Pearson correlation and plot points
"""
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

def compute_pearson(hbo,hbr,hbt,bold):
    """
    Compute Pearson for each column of dataframe for bold vs hbo, 
    bold vs hbr, bold vs hbt
    """
    
    colortest = ['firebrick','saddlebrown','darkorange','gold',
             'yellowgreen','darkcyan','dodgerblue','royalblue',
             'blue','azure','blueviolet','orchid',
             'pink','darkred','lightsalmon','darkgoldenrod',
             'slategrey']
    
    pearson_bold_hbo = pd.DataFrame(columns=[
        'S1D1','S1D2','S2D3','S3D1','S3D4',
        'S4D2','S4D4','S4D5','S5D4','S5D6',
        'S6D4','S6D6','S6D7','S7D5','S7D7',
        'S8D6','S8D7'])
    
    pearson_bold_hbr = pearson_bold_hbo.copy()
    pearson_bold_hbt = pearson_bold_hbo.copy()
    
    for chan_bold,chan_hbo,chan_hbr,chan_hbt in zip(bold,hbo,hbr,hbt):
        pearson_bold_hbo[chan_bold] = pearsonr(bold[chan_bold],hbo[chan_hbo])
        pearson_bold_hbr[chan_bold] = pearsonr(bold[chan_bold],hbr[chan_hbr])
        pearson_bold_hbt[chan_bold] = pearsonr(bold[chan_bold],hbt[chan_hbt])
    
    print(pearson_bold_hbo)
    print(pearson_bold_hbr)
    print(pearson_bold_hbt)
    # for chan_bold,chan_hbt in zip(bold,hbt):
    # fig, ax = plt.subplots(figsize=(15, 15))
    # for chan_hbt,chan_bold,col in zip(hbt,bold,colortest):
        # ax.scatter(hbt[chan_hbt],bold[chan_bold],c=col,label=chan_bold)
        # ax.legend(loc='best')
        # plt.annotate('Pearsonr coeff = %0.3f'% pearson_bold_hbo.at[0,chan_bold],(0,1) )   
    # plt.show()
    # plt.savefig('c:/users/bprigent/Desktop/test_1/'+chan_bold+'.png')
    # plt.close()
    return