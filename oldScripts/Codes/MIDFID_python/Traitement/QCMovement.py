# -*- coding: utf-8 -*-
"""
Created on Wed Apr 05 13:45:38 2024

@author: B.Prigent

Script to create plot for QC the movement of the patient's head

Input: data obtain with autoThePlot: rp_*.txt file, rc1_*.nii.gz, rc2_*.nii.gz rc3_*.nii.gz
Output: plot with displacement in mm
"""

# %% 0- Library

import matplotlib.pyplot as plt
import numpy as np
import pyautomri

# %% 1- Import data

movx,movy,movz = np.loadtxt('*.txt', delimiter=" ", unpack=True)
printf(movx)
time = np.linspace(1,700,length(movx))

# %% 2- Plot displacement
fig, ax = plt.subplots()
ax.grid('on')
ax.plot(time,movx,label=r"$X$",color='blue')
ax.plot(time,movy,label=r"$Y$",color='green')
ax.plot(time,movz,label=r"$Z$",color='red')
ax.set_xlabel('Time in s')
ax.set_ylabel('Displacement in mm')
ax.set_title("Plot of the movement of the patient's head during an fMRI session")
ax.legend(loc='best')

plt.show()

