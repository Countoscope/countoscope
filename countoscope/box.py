#!/usr/bin/env python
# -*- Mode: python; tab-width: 4; indent-tabs-mode:nil; coding:utf-8 -*-
#
# Copyright (c) 2024 Authors and contributors
# (see the AUTHORS.rst file for the full list of names)
#
# Released under MIT Licence
"""Module for preparing and cutting the box."""
from trajectory import Trajectory
import numpy as np


class Box(Trajectory):
    r"""Class providing options for dividing the system into small boxes.
    
    The box size can be provided as an integer or an array of same 
    size as the system dimension. 
    """

    def __init__(self,
                 box_size: None,
                 *args,
                 **kwargs
                 ):
        super().__init__(*args, **kwargs)
        self.box_size = box_size

    def run(self):
        self.import_trajectory()
        self.read_information_trajectory()
        self.detect_system_dimension()
        self.specify_box_size()

    def specify_box_size(self):
        """Calculate the measurement box size in all N dimensions"""
        if np.shape(self.box_size) == ():
            # Box size was provided as an integer, use its value to make a
            # cube or a square
            self.box_size = np.zeros(self.dimension)+self.box_size
        # make sure that the box size and the dimension of the system are consistent
        assert np.shape(self.box_size)[0] == self.dimension, \
            """ERROR: Inconsistent box size and system dimension."""

    def select_the_slices():
        assert len(l0_box) == dimensions, """WARNING: unexpected number of values in l0_box, give 3 (x, y, and z)"""
        bounds = []
        new_l0 = []
        for i, dir in zip(range(dimensions), ["x", "y", "z"]):
            lower_boundary, higher_boundary = domaine_boundaries[i]
            bounds_i = np.arange(lower_boundary, higher_boundary+l0_box[i], l0_box[i])
            if np.round(bounds_i[-1],3) > np.round(higher_boundary,3):
                print("WARNING -- Wrong slicing of the system in the direction", dir)
                print("\t The simulation box with boundaries:", lower_boundary, higher_boundary)
                print("\t can't be sliced by blocks of", l0_box[i])
                closer_n_slice = np.int32(((higher_boundary-lower_boundary))/l0_box[i])
                bounds_i = np.linspace(lower_boundary, higher_boundary, num=closer_n_slice)
                l0 = np.round(np.diff(bounds_i)[0],5)
                new_l0.append(l0)
                print("\t", l0, "is used instead")
            else:
                new_l0.append(l0_box[i])
            bounds.append(bounds_i)
        l0_box = np.array(new_l0)
        bounds = bounds
