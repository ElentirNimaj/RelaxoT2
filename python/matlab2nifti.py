#!/usr/bin/env python3
# -*- coding: utf-8 -*- #
# ============================================= #
# Matlab2Nifti
# B. Prigent
# v 1, 17-Jul-2023
# ============================================= #
"""
    Transform matlab to nifti 
"""

import numpy as np
import nibabel as nib
import mat73 as mtp
import matplotlib.pyplot as plt
from scipy.io import loadmat

RESULTS_PATH = r"C:\Users\bprigent\MyDatas\TestFolder\ResultsTest\C0PI.t2parts.mat"
# RESULTS_PATH = r"C:\Users\bprigent\MyDatas\TestFolder\ResultsTest\C0PI.t2maps.mat"
# RESULTS_PATH = r"C:\Users\bprigent\MyProcess\SAME-ECOS\EPG_decay_library_32echo.mat"

# t2_maps = mtp.loadmat(RESULTS_PATH)
# t2_maps = mtp.loadmat(RESULTS_PATH)
t2_info = mtp.loadmat(RESULTS_PATH)
t2_prism = loadmat(r"C:\Users\bprigent\MyDatas\TestFolder\ProcessPRISM.mat")
# t2_short = t2_maps['sfr']

# t2_mid = t2_maps['mfr']
# t2_epg = t2_maps['decay']
# image = nib.Nifti1Image(t2_short,affine=np.eye(4))
# image2 = nib.Nifti1Image(t2_mid,affine=np.eye(4))
# nib.save(image,"C:\\Users\\bprigent\\Desktop\\test.nii.gz")
# nib.save(image2,"C:\\Users\\bprigent\\Desktop\\test2.nii.gz")
# nib.save(image,"C:\\Users\\bprigent\\Desktop\\DECAESshortC0.nii.gz")

ggm =nib.Nifti1Image(t2_info['sgm'],affine=np.eye(4))
# nib.save(ggm,"C:\\Users\\bprigent\\Desktop\\test2.nii.gz")
prism = nib.Nifti1Image(t2_prism['Image'],affine=np.eye(4))
nib.save(prism,"C:\\Users\\bprigent\\Desktop\\prism.nii.gz")
# print(type(ggm.get_fdata()))

# plt.imshow(ggm.get_fdata())
# plt.axis('off')
# plt.show()

# plt.plot(t2_info['ggm'])
# plt.show()