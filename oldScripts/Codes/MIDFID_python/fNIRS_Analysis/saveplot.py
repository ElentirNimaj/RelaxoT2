#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

# ============================================= #
# Save and plot
# B. Prigent
# v 1, 06-Jul-2023
# ============================================= #
"""
    Script to plot and saves values from fNIRS and fMRI acquisition
"""
import os
import matplotlib.pyplot as plt

def save_to_csv(hbo_norm,hbr_norm,hbt_norm,bold_norm,savepath,subject_id):
    try:
        os.makedirs(savepath)
    except FileExistsError:
        pass
    
    hbo_norm.to_csv(savepath+subject_id+'_hbo.csv')
    hbr_norm.to_csv(savepath+subject_id+'_hbr.csv')
    hbt_norm.to_csv(savepath+subject_id+'_hbt.csv')
    bold_norm.to_csv(savepath+subject_id+'_bold.csv')
    
    print(f"Dataframe save into csv in {savepath}")
    return 

def save_all_plot(hbo_norm,hbr_norm,hbt_norm,bold_norm,savepath,subject_id):
    savepath = str(savepath)
    for channel_bold,channel_hbo,channel_hbr in zip(
        bold_norm,hbo_norm,hbr_norm):
        fig,ax = plt.subplots(1,1)
        ax.plot(bold_norm[channel_bold], color='black',label='fMRI signal')
        ax.plot(hbo_norm[channel_hbo], color='red',label=r'$HbO_2$ signal')
        # ax.plot(hbr_norm[channel_hbr], color='blue',label=r'$Hbr$ signal')
        ax.set_title('Comparison Bold/HbO/HbR channel '+ channel_bold)
        ax.legend(loc='best')
        fig.set_size_inches(32, 18)
        fig.savefig(savepath +subject_id + '_' + channel_bold +'.png', 
                    bbox_inches='tight')
        plt.close()
    
    for channel_bold,channel_hbt in zip(
        bold_norm,hbt_norm):
        fig,ax = plt.subplots(1,1)
        ax.plot(bold_norm[channel_bold], color='black',label='fMRI signal')
        ax.plot(hbt_norm[channel_hbt], color='purple',label=r'$HbT$ signal')
        ax.set_title('Comparison Bold/HbT channel '+ channel_bold)
        ax.legend(loc='best')
        fig.set_size_inches(32, 18)
        fig.savefig(savepath +subject_id + '_HbT_' + channel_bold + '.png', 
                    bbox_inches='tight')
        plt.close()
        
    print(f"Plots saved in {savepath}")
    return


