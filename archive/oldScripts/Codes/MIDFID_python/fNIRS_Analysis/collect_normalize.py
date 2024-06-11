#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

# ============================================= #
# Treatment and normalization
# B. Prigent
# v 1, 06-Jul-2023
# ============================================= #
"""
    Script to normalize hbo and bold times series and return a file
"""
import pandas as pd
import numpy as np
import os
import glob
from matlab2python import load_mat
from nilearn.signal import clean
from scipy import signal as sig



def collect_timeseries(
    hb_filepath,
    bold_dirpath
    ):
    
    """
    Collect time_series from the csv files and matlab, transform into
    a dataframe for fNIRS and fMRI.
    
    Args:
        hbo_filepath (str): Path to hbo timeseries csv file.
    Returns:
        hbo_no_normalize (dataframe): dataframe of the different 
    """
    print("Collecting Timeseries")
    hb_data = pd.read_csv(hb_filepath)
    hb_data.columns = [
        'S1D1_hbo','S1D1_hbr','S1D2_hbo','S1D2_hbr','S2D3_hbo','S2D3_hbr',
        'S3D1_hbo','S3D1_hbr','S3D4_hbo','S3D4_hbr','S4D2_hbo','S4D2_hbr',
        'S4D4_hbo','S4D4_hbr','S4D5_hbo','S4D5_hbr','S5D4_hbo','S5D4_hbr',
        'S5D6_hbo','S5D6_hbr','S6D4_hbo','S6D4_hbr','S6D6_hbo','S6D6_hbr',
        'S6D7_hbo','S6D7_hbr','S7D5_hbo','S7D5_hbr','S7D7_hbo','S7D7_hbr',
        'S8D6_hbo','S8D6_hbr','S8D7_hbo','S8D7_hbr'
        ]
    
    hbt_data = pd.DataFrame(columns=['S1D1_hbt','S1D2_hbt','S2D3_hbt',
                                     'S3D1_hbt','S3D4_hbt','S4D2_hbt',
                                     'S4D4_hbt','S4D5_hbt','S5D4_hbt',
                                     'S5D6_hbt','S6D4_hbt','S6D6_hbt',
                                     'S6D7_hbt','S7D5_hbt','S7D7_hbt',
                                     'S8D6_hbt','S8D7_hbt'])
    
    bold_data = pd.DataFrame(columns=['S1D1','S1D2','S2D3','S3D1','S3D4',
                                      'S4D2','S4D4','S4D5','S5D4','S5D6',
                                      'S6D4','S6D6','S6D7','S7D5','S7D7',
                                      'S8D6','S8D7'])
    
    bold_listdir = glob.glob(bold_dirpath +'*_mres.mat')
    for channel,bold_name in zip(bold_listdir,bold_data):
        chan_bold = load_mat(channel)
        bold_data[bold_name] = chan_bold['SPM']['marsY']['Yvar']
        
    hbo_data = hb_data[['S1D1_hbo','S1D2_hbo','S2D3_hbo','S3D1_hbo',
                        'S3D4_hbo','S4D2_hbo','S4D4_hbo','S4D5_hbo',
                        'S5D4_hbo','S5D6_hbo','S6D4_hbo','S6D6_hbo',
                        'S6D7_hbo','S7D5_hbo','S7D7_hbo','S8D6_hbo',
                        'S8D7_hbo']].copy()
    hbr_data = hb_data[['S1D1_hbr','S1D2_hbr','S2D3_hbr','S3D1_hbr',
                        'S3D4_hbr','S4D2_hbr','S4D4_hbr','S4D5_hbr',
                        'S5D4_hbr','S5D6_hbr','S6D4_hbr','S6D6_hbr',
                        'S6D7_hbr','S7D5_hbr','S7D7_hbr','S8D6_hbr',
                        'S8D7_hbr']].copy()
    
    for chan_hbt,chan_hbo,chan_hbr in zip(
        hbt_data,
        hbo_data,
        hbr_data
    ):
        hbt_data[chan_hbt] = hbo_data[chan_hbo] - hbr_data[chan_hbr]
        
    print("Timeseries Collected")
    return [hbo_data,hbr_data,hbt_data,bold_data]



def normalize_timeseries(hbo_data,hbr_data,hbt_data,bold_data):
    
    print("Normalized and resample timeseries")
    hbo_final = pd.DataFrame()
    hbr_final = pd.DataFrame()
    hbt_final = pd.DataFrame()
    bold_final = pd.DataFrame()
    
    for channel in hbo_data:
        hbo = hbo_data[channel]
        hbo_resampled = sig.resample(hbo,len(bold_data.index))
        hbo_norm = hbo_resampled / np.max(hbo_resampled)
        hbo_final[channel] = hbo_norm
        
    for channel in hbr_data:
        hbr = hbr_data[channel]
        hbr_resampled = sig.resample(hbr,len(bold_data.index))
        hbr_norm = hbr_resampled / np.max(hbr_resampled)
        hbr_final[channel] = hbr_norm        
    
    for channel in hbt_data:
        hbt = hbt_data[channel]
        hbt_resampled = sig.resample(hbt,len(bold_data.index))
        hbt_norm = hbt_resampled / np.max(hbt_resampled)
        hbt_final[channel] = hbt_norm    
        
    for channel in bold_data:
        bold = bold_data[channel]
        bold = bold.to_numpy()
        bold = np.reshape(bold,(len(bold_data.index),1))
        bold_clean = clean(bold, detrend=True,
                          filter='butterworth', low_pass=0.09, 
                          high_pass=0.01, t_r=1.224)
        bold_norm = bold_clean / np.max(bold_clean)
        bold_final[channel] = [b[0] for b in bold_norm]
        
    print("Timeseries resampled and corrected")
    return [hbo_final,hbr_final,hbt_final,bold_final]