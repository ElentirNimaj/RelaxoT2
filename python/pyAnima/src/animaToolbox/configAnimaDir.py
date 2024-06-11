#!/usr/bin/env python3
# -*- coding: utf-8 -*- #
# ============================================= #
# anima Directory
# B. Prigent
# v 1, 06-Jun-2024
# ============================================= #
"""
    Script to create anima path and to rename them
"""

import sys
import argparse
import glob
import os
from shutil import copyfile, rmtree
from subprocess import call, check_output, run
import uuid

if sys.version_info[0] > 2:
    import configparser as ConfParser
else:
    import ConfigParser as ConfParser

def verify_configFile():
    """
    Verify that the anima config file exist. 
    """
    try:
        configFilePath = os.path.join(os.path.expanduser("~"), ".anima",  "config.txt")
    except FileNotFoundError:
        print("Please create a configuration file for Anima python scripts. Refer to the README")
        sys.exit(1)

    return configFilePath

def create_shortcut(atlas,configFilePath):
    """
    Create shortcut name for the scripts
    """
    configParser = ConfParser.RawConfigParser()
    configParser.read(configFilePath)
    animaDir = configParser.get("anima-scripts", 'anima')
    animaExtraDataDir = configParser.get("anima-scripts", 'extra-data-root')
    atlasDir = os.path.join(animaExtraDataDir,"icc_atlas")
    if atlas:
        atlasDir = atlas

    SHORTCUT = {
    "animaPyramidalBMRegistration" : os.path.join(animaDir, "animaPyramidalBMRegistration.exe"),
    "animaDenseSVFBMRegistration" : os.path.join(animaDir, "animaDenseSVFBMRegistration.exe"),
    "animaTransformSerieXmlGenerator" : os.path.join(animaDir, "animaTransformSerieXmlGenerator.exe"),
    "animaApplyTransformSerie" : os.path.join(animaDir, "animaApplyTransformSerie.exe"),
    "animaConvertImage" : os.path.join(animaDir, "animaConvertImage.exe"),
    "animaMaskImage" : os.path.join(animaDir, "animaMaskImage.exe"),
    "animaCreateImage" : os.path.join(animaDir, "animaCreateImage.exe"),
    "animaMorphologicalOperations" : os.path.join(animaDir, "animaMorphologicalOperations.exe"),
    "atlasDir" : os.path.join(animaExtraDataDir,"icc_atlas"),
    "atlasImage" : os.path.join(atlasDir,"Reference_T1.nrrd"),
    "atlasLargeFOVImage" : os.path.join(atlasDir,"Reference_T1_largeFOV.nrrd"),
    "atlasLargeFOVHeadMask" : os.path.join(atlasDir,"Reference_T1_HeadMask.nrrd"),
    "atlasImageFromMasked" : os.path.join(atlasDir,"Reference_T1_from_masked.nrrd"),
    "iccImage" : os.path.join(atlasDir,"BrainMask.nrrd"),
    "iccImageFromMasked" : os.path.join(atlasDir,"BrainMask_from_masked.nrrd")
    }

    return SHORTCUT

if __name__=="__main__":
    configpath= verify_configFile()
    anima = create_shortcut(configpath)