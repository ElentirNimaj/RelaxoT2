#!/usr/bin/env python3
# -*- coding: utf-8 -*- #
# ============================================= #
# Comparison fNIRS fMRI
# B. Prigent
# v 1, 17-Jul-2023
# ============================================= #
"""
    Main script for the comparison between fNIRS and fMRI 
"""

import matlab2python
from collect_normalize import collect_timeseries
from collect_normalize import normalize_timeseries
from pearson import compute_pearson
import saveplot
import argparse
    
if __name__ == '__main__' :
    parser = argparse.ArgumentParser(
                    prog='main_comparison',
                    description='Takes datas from time series and give the'
                    +' plot, the pearson coefficient and the plots.',
                    epilog='Good luck !')

    parser.add_argument('-n',
                        type=str,help='the path for the fNIRS file')           
    parser.add_argument('-m',
                        type=str,help='the path for the fMRI directory')
    parser.add_argument('-s',
                        type=str,help='the path for saving the output')      
    parser.add_argument('-S',type=str,help='Name of the subject')
    args = parser.parse_args()
    
    hbo_coll,hbr_coll,hbt_coll,bold_coll = collect_timeseries(args.n,args.m)
    hbo_norm,hbr_norm,hbt_norm,bold_norm = normalize_timeseries(
        hbo_coll,hbr_coll,hbt_coll,bold_coll)
    saveplot.save_to_csv(hbo_norm,hbr_norm,hbt_norm,bold_norm,args.s,args.S)
    saveplot.save_all_plot(hbo_norm,hbr_norm,hbt_norm,bold_norm,args.s,args.S)
    compute_pearson(hbo_norm,hbr_norm,hbt_norm,bold_norm)
    print(""" /* END OF SCRIPT *\ \n""")
    