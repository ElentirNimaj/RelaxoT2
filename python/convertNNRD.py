#!/usr/bin/env python3
# -*- coding: utf-8 -*- #
# ============================================= #
# Conversion nii/nrrd
# B. Prigent
# v 1, 03-Jun-2024
# ============================================= #
"""
    Convert nnrd/nii
"""

import SimpleITK as stik

# img = stik.ReadImage('''C:\\d\\Anima-Scripts-Data-Public\\icc_atlas\\BrainMask.nrrd''')
# stik.WriteImage(img, '''C:\\d\\Anima-Scripts-Data-Public\\icc_atlas\\BrainMask.nii.gz''')

# img = stik.ReadImage('''C:\\d\\Anima-Scripts-Data-Public\\icc_atlas\\BrainMask_from_masked.nrrd''')
# stik.WriteImage(img, '''C:\\d\\Anima-Scripts-Data-Public\\icc_atlas\\BrainMask_from_masked.nii.gz''')

# img = stik.ReadImage('''C:\\d\\Anima-Scripts-Data-Public\\icc_atlas\\Reference_T1.nrrd''')
# stik.WriteImage(img, '''C:\\d\\Anima-Scripts-Data-Public\\icc_atlas\\Reference_T1.nii.gz''')

# img = stik.ReadImage('''C:\\d\\Anima-Scripts-Data-Public\\icc_atlas\\Reference_T1_from_masked.nrrd''')
# stik.WriteImage(img, '''C:\\d\\Anima-Scripts-Data-Public\\icc_atlas\\Reference_T1_from_masked.nii.gz''')

img = stik.ReadImage("C:\Users\bprigent\MyDatas\TestFolder\C0PIDCMCrop.nrrd")
stik.WriteImage(img, "C:\\Users\\bprigent\\MyDatas\\TestFolder\\pouetT1.nrrd")