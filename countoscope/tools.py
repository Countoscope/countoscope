#!/usr/bin/env python
# -*- Mode: python; tab-width: 4; indent-tabs-mode:nil; coding:utf-8 -*-
#
# Copyright (c) 2024 Authors and contributors
# (see the AUTHORS.rst file for the full list of names)
#
# Released under MIT Licence
"""Convert homemade format into xyz format compatible with Chemfile."""
import numpy as np


def convert_homemade_format(input_file, output_file):
    """Convert homemade format."""
    # read input file
    file = open(input_file, "r")
    array = np.loadtxt(file)
    if np.shape(array)[1] == 3: # format is X Y N
        type = "2D"
        ids_frames = array[:,2]
        coordinates = array[:,0:2]
    elif np.shape(array)[1] == 4: # format if X Y Z N
        type = "3D"
        ids_frames = array[:,3]
        coordinates = array[:,0:3]
    else:
        print("unexpected number of columns")
    # write output file
    f = open(output_file, "w")
    for id_frame in np.unique(ids_frames):
        frame_coordinate = coordinates[ids_frames==id_frame]
        atom_per_frame = np.shape(frame_coordinate)[0]
        f.write("{}\n".format(atom_per_frame))
        f.write("Atoms. Timestep: {}\n".format(id_frame))
        for coordinate in frame_coordinate:
            if type == "2D":
                x, y = coordinate
                f.write("{} {}\n".format(x, y))
            elif type == "3D":
                x, y, z = coordinate
                f.write("{} {} {}\n".format(x, y, z))
    f.close()