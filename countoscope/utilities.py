#!/usr/bin/env python
# -*- Mode: python; tab-width: 4; indent-tabs-mode:nil; coding:utf-8 -*-
#
# Copyright (c) 2024 Authors and contributors
# (see the AUTHORS.rst file for the full list of names)
#
# Released under MIT Licence
"""Small helper and utilities functions that don't fit anywhere else."""
import os
import numpy as np

def autocorrelation_function(data):
    """Calculate autocorrelation of one arrays using FFT.

    **Parameters**

    data : numpy.ndarray

    **Returns**

    np.ndarray
        The autocorrelation function.
    """
    data_0 = np.append(data, np.zeros(2 ** int(np.ceil((np.log(len(data))
                                   / np.log(2)))) - len(data)), axis=0)
    data_1 = np.append(data_0, np.zeros(data_0.shape), axis=0)
    fra = np.fft.fft(data_1, axis=0)
    sf = np.conj(fra) * fra
    res = np.fft.ifft(sf, axis=0)
    return np.real(res[:len(data)]) / np.array(range(len(data), 0, -1))

def calculate_remaining_axis(dim):
    """Return a tuple with the 2 axes that are different from dim"""
    remaining_axis = ()
    for axis in [0, 1, 2]:
        if axis != dim:
            remaining_axis = remaining_axis + (axis,)
    return remaining_axis