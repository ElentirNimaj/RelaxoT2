#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

# ============================================= #
# Matlab to python
# B. Prigent
# v 1, 17-Jul-2023
# ============================================= #
"""
    Script to read and transform matlab file
"""

# %% Library

import numpy as np
from scipy.io import loadmat
from scipy.io import matlab

# %% Load mat


def load_mat(filename):
    """
    Take .mat file and return dictionnary type data
    """

    def check_mat_vars(mat_obj):
        """
        Check the type of object in mat_obj, if it's a struct then it call 
        to dict to transform into dict, else transform into array
        
        Args:
        mat_obj (mat): Matlab file
        """
        for key in mat_obj:
            if isinstance(mat_obj[key], matlab.mat_struct):
                mat_obj[key] = to_dict(mat_obj[key])
            elif isinstance(mat_obj[key], np.ndarray):
                mat_obj[key] = to_array(mat_obj[key])
        return mat_obj

    def to_dict(struct):
        """
        Transform struct type object into dictionnary recursively
        """
        mat_obj = {}
        for strg in struct._fieldnames:
            elem = struct.__dict__[strg]
            if isinstance(elem, matlab.mat_struct):
                mat_obj[strg] = to_dict(elem)
            elif isinstance(elem, np.ndarray):
                mat_obj[strg] = to_array(elem)
            else:
                mat_obj[strg] = elem
        return mat_obj

    def to_array(ndarray):
        """
        Transform other datas type object into numpy array recursively
        """
        if ndarray.dtype != 'float64':
            elem_list = []
            for sub_elem in ndarray:
                if isinstance(sub_elem, matlab.mat_struct):
                    elem_list.append(to_dict(sub_elem))
                elif isinstance(sub_elem, np.ndarray):
                    elem_list.append(to_array(sub_elem))
                else:
                    elem_list.append(sub_elem)
            return np.array(elem_list)
        else:
            return ndarray

    data = loadmat(filename, struct_as_record=False, squeeze_me=True)
    return check_mat_vars(data)
