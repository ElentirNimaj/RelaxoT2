#!/usr/bin/env python3
# -*- coding: utf-8 -*- #
# ============================================= #
# Main application for using relaxometry with python
# B. Prigent
# v 1, 06-Jun-2024
# ============================================= #
"""
    Main script for anima
"""

import argparse
import extractConvertConcat
import configAnimaDir

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
    description="Computes the brain mask of images given in input by registering a known atlas on it. Their output is prefix_brainMask.nrrd and prefix_masked.nrrd")

    parser.add_argument('-L', '--large-fov', action='store_true',
                        help="Specify additional processing to handle large FOV of the input image (typically for babies)."
                            "The atlas must include in that case a large FOV T1w image named: Reference_T1_largeFOV.nrrd")
    parser.add_argument('-S', '--second-step', action='store_true',
                        help="Perform second step of atlas based cropping (might crop part of the external part of the brain)")

    parser.add_argument('-i', '--input', type=str, required=True, help='File to process')
    parser.add_argument('-a', '--atlas', type=str, help='Atlas folder (default: use the adult one in anima scripts data '
                                                        '- icc_atlas folder)')
    parser.add_argument('-m', '--mask', type=str, help='Output path of the brain mask (default is inputName_brainMask.nrrd)')
    parser.add_argument('-b', '--brain', type=str, help='Output path of the masked brain (default is inputName_masked.nrrd)')
    parser.add_argument('-K', '--keep-intermediate-folder', action='store_true',
                        help='Keep intermediate folder after script end')

    args = parser.parse_args()

    configPath = configAnimaDir.verify_configFile()
    animas = configAnimaDir.create_shortcut(args.atlas,configPath)
    del configPath


    print("""\n /* END OF SCRIPT *\ \n""")