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
        self.run_box()

    def run_box(self):
        self.run_trajectory()
        self.specify_measurement_box_size()
        self.select_the_slices()
        self.allocate_memory()

    def specify_measurement_box_size(self):
        """Calculate the measurement box size in all N dimensions."""
        if np.shape(self.box_size) == ():
            # Box size was provided as an integer, use its value to make a
            # cube or a square
            self.box_size = np.zeros(self.dimension)+self.box_size
        # make sure that the box size and the dimension of the system are consistent
        assert np.shape(self.box_size)[0] == self.dimension, \
            """ERROR: Inconsistent box size and system dimension."""

    def select_the_slices(self):
        """Select the edged positions of the measurement boxes.

        If possible, i.e. if the system size can be divided into an even number of
        measurement boxes, the box_size provided by the user is used. Otherwise,
        the box_size is recalculated to allow for a slicing in evenly-sized boxes.
        """
        box_bounds = []
        new_l0 = []
        for i, dir in zip(range(self.dimension), ["x", "y", "z"]):
            lower_boundary, higher_boundary = self.system_boundaries[i]
            box_bounds_i = np.arange(lower_boundary, higher_boundary+self.box_size[i], self.box_size[i])
            if np.round(box_bounds_i[-1],3) > np.round(higher_boundary,3):
                closer_n_slice = np.int32(((higher_boundary-lower_boundary))/self.box_size[i])
                box_bounds_i = np.linspace(lower_boundary, higher_boundary, num=closer_n_slice)
                l0 = np.round(np.diff(box_bounds_i)[0],5)
                new_l0.append(l0)
                nb_box = np.int32(self.system_size[i]/self.box_size[i])
                print("INFO -- Incompatible box size along", dir)
                print("     -- The system with lateral size {0:0.2f}".format(self.system_size[i]), \
                      "can't be divided evenly by measurement boxes of size {0:0.2f}. \n".format(self.box_size[i]), \
                      f"    -- A number {nb_box} of boxes with size {l0:0.2f} will be used instead")
            else:
                new_l0.append(self.box_size[i])
            box_bounds.append(box_bounds_i)
        self.box_size = np.array(new_l0)
        self.box_bounds = box_bounds

    def allocate_memory(self):
        """Create empty array for the particle counting."""
        if self.dimension == 2:
            number_matrix = np.zeros((self.nb_steps,
                                      len(self.box_bounds[0])-1,
                                      len(self.box_bounds[1])-1))
        elif self.dimension == 3:
            number_matrix = np.zeros((self.nb_steps,
                                      len(self.box_bounds[0])-1,
                                      len(self.box_bounds[1])-1,
                                      len(self.box_bounds[2])-1))
        self.number_matrix = number_matrix