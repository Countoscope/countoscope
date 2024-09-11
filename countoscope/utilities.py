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

def convert_homemade_format(input_file, output_file):
    """Convert homemade format into xyz format compatible with Chemfile.
    todo: allow other particle type
    """
    # read input file
    file = open(input_file, "r")
    array = np.loadtxt(file)
    if np.shape(array)[1] == 3 or np.shape(array)[1] == 4: # format is x y t or x y t id
        type = "2D"
        ids_frames = array[:,2]
        coordinates = array[:,0:2]
    else:
        print("unexpected number of columns")
    # write output file
    f = open(output_file, "w")
    for id_frame in np.unique(ids_frames):
        frame_coordinate = coordinates[ids_frames==id_frame]
        atom_per_frame = np.shape(frame_coordinate)[0]
        f.write("{}\n".format(atom_per_frame))
        f.write("Atoms. Timestep: {}\n".format(np.int32(id_frame)))
        for coordinate in frame_coordinate:
            if type == "2D":
                x, y = coordinate
                f.write("1 {} {} 0\n".format(x, y))
            elif type == "3D":
                x, y, z = coordinate
                f.write("1 {} {} {}\n".format(x, y, z))
    f.close()