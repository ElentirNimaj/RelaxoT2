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
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

D01 = pan.read_excel("c:/users/bprigent/Documents/MIDFID/Few_test/d01_AnticipationAndReward/AllResults.xlsx",sheet_name='D01_AntRew')

SUBJECT = ["A01","A02","A03","A04","A05",
        "A06","A07","A08","A09","A10",
        "A11","A12","A13","A14","A15"]

CONDITIONS = ["""Ant Food High """,
"""Ant Food No """,
"""Ant Money High """,
"""Ant Money No """,
"""Ant Food HighvsNo """,
"""Ant Money HighvsNo """,
"""Rew Food High """,
"""Rew Food No """,
"""Rew Money High """,
"""Rew Money No """,
"""Rew Food HighvsNo """,
"""Rew Money HighvsNo """,
"""Ant FoodAndMoney High """,
"""Ant FoodAndMoney HighvsNo """,
"""Rew FoodAndMoney High """,
"""Rew FoodAndMoney HighvsNo """,
"""Ant FoodvsMoney High """,
"""Rew FoodvsMoney High """,
]

CONDITIONS_SIMPLE = ["C01","C02","C03","C04","C05",
        "C06","C07","C08","C09","C10",
        "C11","C12","C13","C14","C15",
        "C16","C17","C18"]

Acc = D01[(D01["ROI"]) == "ACC"] 
contrast_index = (Acc["Contrast index"])
Values = [0]*18
for contrast in range(0,18):
    contrast_punctual = Acc[Acc["Contrast index"] == contrast+1]
    contrast_value = contrast_punctual['Value']
    Values[contrast] = contrast_value



fig, ax1 = plt.subplots(figsize=(18,8))
fig.canvas.manager.set_window_title('Boxplots for each contrasts')
fig.subplots_adjust(left=0.075, right=0.95, top=0.9, bottom=0.25)

bp = ax1.boxplot(Values, notch=False, sym='+', vert=True, whis=1.5)
plt.setp(bp['boxes'], color='black')
plt.setp(bp['whiskers'], color='black')
plt.setp(bp['fliers'], color='red', marker='+')

# Add a horizontal grid to the plot, but make it very light in color
# so we can use it for reading data values but not be distracting
ax1.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
               alpha=0.5)

ax1.set(
    axisbelow=True,  # Hide the grid behind plot objects
    title='Boxplot for the ACC part with each contrast',
    xlabel='Contrasts',
    ylabel='Value',
)
ax1.set_xticklabels(CONDITIONS,
                    rotation=45, fontsize=8)

box_colors = ['darkkhaki', 'royalblue']
num_boxes = len(Values)
medians = np.empty(num_boxes)
for i in range(num_boxes):
    box = bp['boxes'][i]
    box_x = []
    box_y = []
    for j in range(5):
        box_x.append(box.get_xdata()[j])
        box_y.append(box.get_ydata()[j])
    box_coords = np.column_stack([box_x, box_y])
    # Alternate between Dark Khaki and Royal Blue
    ax1.add_patch(Polygon(box_coords, facecolor=box_colors[i % 2]))
    # Now draw the median lines back over what we just filled in
    med = bp['medians'][i]
    median_x = []
    median_y = []
    for j in range(2):
        median_x.append(med.get_xdata()[j])
        median_y.append(med.get_ydata()[j])
        ax1.plot(median_x, median_y, 'k')
    medians[i] = median_y[0]
    # Finally, overplot the sample averages, with horizontal alignment
    # in the center of each box
    ax1.plot(np.average(med.get_xdata()), np.average(Values[i]),
             color='w', marker='.', markeredgecolor='k')
fig.savefig('c:/users/bprigent/Documents/MIDFID/Few_test/d01_AnticipationAndReward/ACC_boxplot.png')
plt.show()

NAcc = D01[(D01["ROI"]) == "Accumbens"] 
contrast_index = (NAcc["Contrast index"])
Values = [0]*18
for contrast in range(0,18):
    contrast_punctual = NAcc[NAcc["Contrast index"] == contrast +1]
    contrast_value = contrast_punctual['Value']
    Values[contrast] = contrast_value



fig, ax2 = plt.subplots(figsize=(18,8))
fig.canvas.manager.set_window_title('Boxplots for each contrasts')
fig.subplots_adjust(left=0.075, right=0.95, top=0.9, bottom=0.25)

bp = ax2.boxplot(Values, notch=False, sym='+', vert=True, whis=1.5)
plt.setp(bp['boxes'], color='black')
plt.setp(bp['whiskers'], color='black')
plt.setp(bp['fliers'], color='red', marker='+')

# Add a horizontal grid to the plot, but make it very light in color
# so we can use it for reading data values but not be distracting
ax2.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
               alpha=0.5)

ax2.set(
    axisbelow=True,  # Hide the grid behind plot objects
    title='Boxplot for the Accumbes part with each contrast',
    xlabel='Contrasts',
    ylabel='Value',
)
ax2.set_xticklabels(CONDITIONS,
                    rotation=45, fontsize=8)


for i in range(num_boxes):
    box = bp['boxes'][i]
    box_x = []
    box_y = []
    for j in range(5):
        box_x.append(box.get_xdata()[j])
        box_y.append(box.get_ydata()[j])
    box_coords = np.column_stack([box_x, box_y])
    # Alternate between Dark Khaki and Royal Blue
    ax2.add_patch(Polygon(box_coords, facecolor=box_colors[i % 2]))
    # Now draw the median lines back over what we just filled in
    med = bp['medians'][i]
    median_x = []
    median_y = []
    for j in range(2):
        median_x.append(med.get_xdata()[j])
        median_y.append(med.get_ydata()[j])
        ax2.plot(median_x, median_y, 'k')
    medians[i] = median_y[0]
    # Finally, overplot the sample averages, with horizontal alignment
    # in the center of each box
    ax2.plot(np.average(med.get_xdata()), np.average(Values[i]),
             color='w', marker='.', markeredgecolor='k')
fig.savefig('c:/users/bprigent/Documents/MIDFID/Few_test/d01_AnticipationAndReward/Nacc_boxplot.png')
plt.show()

Caude = D01[(D01["ROI"]) == "Caude"] 
contrast_index = (Caude["Contrast index"])
Values = [0]*18
for contrast in range(0,18):
    contrast_punctual = Caude[Caude["Contrast index"] == contrast +1]
    contrast_value = contrast_punctual['Value']
    Values[contrast] = contrast_value



fig, ax3 = plt.subplots(figsize=(18,8))
fig.canvas.manager.set_window_title('Boxplots for each contrasts')
fig.subplots_adjust(left=0.075, right=0.95, top=0.9, bottom=0.25)

bp = ax3.boxplot(Values, notch=False, sym='+', vert=True, whis=1.5)
plt.setp(bp['boxes'], color='black')
plt.setp(bp['whiskers'], color='black')
plt.setp(bp['fliers'], color='red', marker='+')

# Add a horizontal grid to the plot, but make it very light in color
# so we can use it for reading data values but not be distracting
ax3.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
               alpha=0.5)

ax3.set(
    axisbelow=True,  # Hide the grid behind plot objects
    title='Boxplot for the Caude part with each contrast',
    xlabel='Contrasts',
    ylabel='Value',
)
ax3.set_xticklabels(CONDITIONS,
                    rotation=45, fontsize=8)


for i in range(num_boxes):
    box = bp['boxes'][i]
    box_x = []
    box_y = []
    for j in range(5):
        box_x.append(box.get_xdata()[j])
        box_y.append(box.get_ydata()[j])
    box_coords = np.column_stack([box_x, box_y])
    # Alternate between Dark Khaki and Royal Blue
    ax3.add_patch(Polygon(box_coords, facecolor=box_colors[i % 2]))
    # Now draw the median lines back over what we just filled in
    med = bp['medians'][i]
    median_x = []
    median_y = []
    for j in range(2):
        median_x.append(med.get_xdata()[j])
        median_y.append(med.get_ydata()[j])
        ax3.plot(median_x, median_y, 'k')
    medians[i] = median_y[0]
    # Finally, overplot the sample averages, with horizontal alignment
    # in the center of each box
    ax3.plot(np.average(med.get_xdata()), np.average(Values[i]),
             color='w', marker='.', markeredgecolor='k')
fig.savefig('c:/users/bprigent/Documents/MIDFID/Few_test/d01_AnticipationAndReward/Caude_boxplot.png')
plt.show()

Putamen = D01[(D01["ROI"]) == "Putamen"] 
contrast_index = (Putamen["Contrast index"])
Values = [0]*18
for contrast in range(0,18):
    contrast_punctual = Putamen[Putamen["Contrast index"] == contrast +1]
    contrast_value = contrast_punctual['Value']
    Values[contrast] = contrast_value



fig, ax4 = plt.subplots(figsize=(18,8))
fig.canvas.manager.set_window_title('Boxplots for each contrasts')
fig.subplots_adjust(left=0.075, right=0.95, top=0.9, bottom=0.25)

bp = ax4.boxplot(Values, notch=False, sym='+', vert=True, whis=1.5)
plt.setp(bp['boxes'], color='black')
plt.setp(bp['whiskers'], color='black')
plt.setp(bp['fliers'], color='red', marker='+')

# Add a horizontal grid to the plot, but make it very light in color
# so we can use it for reading data values but not be distracting
ax4.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
               alpha=0.5)

ax4.set(
    axisbelow=True,  # Hide the grid behind plot objects
    title='Boxplot for the Putamen part with each contrast',
    xlabel='Contrasts',
    ylabel='Value',
)
ax4.set_xticklabels(CONDITIONS,
                    rotation=45, fontsize=8)


for i in range(num_boxes):
    box = bp['boxes'][i]
    box_x = []
    box_y = []
    for j in range(5):
        box_x.append(box.get_xdata()[j])
        box_y.append(box.get_ydata()[j])
    box_coords = np.column_stack([box_x, box_y])
    # Alternate between Dark Khaki and Royal Blue
    ax4.add_patch(Polygon(box_coords, facecolor=box_colors[i % 2]))
    # Now draw the median lines back over what we just filled in
    med = bp['medians'][i]
    median_x = []
    median_y = []
    for j in range(2):
        median_x.append(med.get_xdata()[j])
        median_y.append(med.get_ydata()[j])
        ax4.plot(median_x, median_y, 'k')
    medians[i] = median_y[0]
    # Finally, overplot the sample averages, with horizontal alignment
    # in the center of each box
    ax4.plot(np.average(med.get_xdata()), np.average(Values[i]),
             color='w', marker='.', markeredgecolor='k')
fig.savefig('c:/users/bprigent/Documents/MIDFID/Few_test/d01_AnticipationAndReward/Putamen_boxplot.png')
plt.show()


VTA = D01[(D01["ROI"]) == "VTA"] 
contrast_index = (VTA["Contrast index"])
Values = [0]*18
for contrast in range(0,18):
    contrast_punctual = VTA[VTA["Contrast index"] == contrast +1]
    contrast_value = contrast_punctual['Value']
    Values[contrast] = contrast_value



fig, ax5 = plt.subplots(figsize=(18,8))
fig.canvas.manager.set_window_title('Boxplots for each contrasts')
fig.subplots_adjust(left=0.075, right=0.95, top=0.9, bottom=0.25)

bp = ax5.boxplot(Values, notch=False, sym='+', vert=True, whis=1.5)
plt.setp(bp['boxes'], color='black')
plt.setp(bp['whiskers'], color='black')
plt.setp(bp['fliers'], color='red', marker='+')

# Add a horizontal grid to the plot, but make it very light in color
# so we can use it for reading data values but not be distracting
ax5.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
               alpha=0.5)

ax5.set(
    axisbelow=True,  # Hide the grid behind plot objects
    title='Boxplot for the VTA part with each contrast',
    xlabel='Contrasts',
    ylabel='Value',
)
ax5.set_xticklabels(CONDITIONS,
                    rotation=45, fontsize=8)


for i in range(num_boxes):
    box = bp['boxes'][i]
    box_x = []
    box_y = []
    for j in range(5):
        box_x.append(box.get_xdata()[j])
        box_y.append(box.get_ydata()[j])
    box_coords = np.column_stack([box_x, box_y])
    # Alternate between Dark Khaki and Royal Blue
    ax5.add_patch(Polygon(box_coords, facecolor=box_colors[i % 2]))
    # Now draw the median lines back over what we just filled in
    med = bp['medians'][i]
    median_x = []
    median_y = []
    for j in range(2):
        median_x.append(med.get_xdata()[j])
        median_y.append(med.get_ydata()[j])
        ax5.plot(median_x, median_y, 'k')
    medians[i] = median_y[0]
    # Finally, overplot the sample averages, with horizontal alignment
    # in the center of each box
    ax5.plot(np.average(med.get_xdata()), np.average(Values[i]),
             color='w', marker='.', markeredgecolor='k')
fig.savefig('c:/users/bprigent/Documents/MIDFID/Few_test/d01_AnticipationAndReward/VTA_boxplot.png')
plt.show()

Thal = D01[(D01["ROI"]) == "Thalamus"] 
contrast_index = (Thal["Contrast index"])
Values = [0]*18
for contrast in range(0,18):
    contrast_punctual = Thal[Thal["Contrast index"] == contrast +1]
    contrast_value = contrast_punctual['Value']
    Values[contrast] = contrast_value



fig, ax6 = plt.subplots(figsize=(18,8))
fig.canvas.manager.set_window_title('Boxplots for each contrasts')
fig.subplots_adjust(left=0.075, right=0.95, top=0.9, bottom=0.25)

bp = ax6.boxplot(Values, notch=False, sym='+', vert=True, whis=1.5)
plt.setp(bp['boxes'], color='black')
plt.setp(bp['whiskers'], color='black')
plt.setp(bp['fliers'], color='red', marker='+')

# Add a horizontal grid to the plot, but make it very light in color
# so we can use it for reading data values but not be distracting
ax6.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
               alpha=0.5)

ax6.set(
    axisbelow=True,  # Hide the grid behind plot objects
    title='Boxplot for the Thal part with each contrast',
    xlabel='Contrasts',
    ylabel='Value',
)
ax6.set_xticklabels(CONDITIONS,
                    rotation=45, fontsize=8)


for i in range(num_boxes):
    box = bp['boxes'][i]
    box_x = []
    box_y = []
    for j in range(5):
        box_x.append(box.get_xdata()[j])
        box_y.append(box.get_ydata()[j])
    box_coords = np.column_stack([box_x, box_y])
    # Alternate between Dark Khaki and Royal Blue
    ax6.add_patch(Polygon(box_coords, facecolor=box_colors[i % 2]))
    # Now draw the median lines back over what we just filled in
    med = bp['medians'][i]
    median_x = []
    median_y = []
    for j in range(2):
        median_x.append(med.get_xdata()[j])
        median_y.append(med.get_ydata()[j])
        ax6.plot(median_x, median_y, 'k')
    medians[i] = median_y[0]
    # Finally, overplot the sample averages, with horizontal alignment
    # in the center of each box
    ax6.plot(np.average(med.get_xdata()), np.average(Values[i]),
             color='w', marker='.', markeredgecolor='k')
fig.savefig('c:/users/bprigent/Documents/MIDFID/Few_test/d01_AnticipationAndReward/Thal_boxplot.png')
plt.show()
