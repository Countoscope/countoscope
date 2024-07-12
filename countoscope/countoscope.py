#!/usr/bin/env python
# -*- Mode: python; tab-width: 4; indent-tabs-mode:nil; coding:utf-8 -*-
#
# Copyright (c) 2024 Authors and contributors
# (see the AUTHORS.rst file for the full list of names)
#
# Released under MIT Licence
"""Module for sorting the particles in boxes."""
from .sorting import Sorting
from .utilities import autocorrelation_function, calculate_remaining_axis
import numpy as np


class Countoscope(Sorting):
    def __init__(self,
                 *args,
                 **kwargs
                 ):
        super().__init__(*args, **kwargs)

    def run(self):
        self.evaluate_correlation()
        self.evaluate_mean_particle_number()
        self.evaluate_deltan2()

    def evaluate_correlation(self):
        """Evaluate the correlation function."""
        per_box_correlation_functions = []
        for ix in np.arange(np.shape(self.number_matrix)[1]):
            per_box_correlation_functions.append([])
            for iy in np.arange(np.shape(self.number_matrix)[2]):
                if self.dimension == 3:
                    per_box_correlation_functions[ix].append([])
                    for iz in np.arange(np.shape(self.number_matrix)[3]):
                        correlation_function = autocorrelation_function(self.number_matrix[:, ix, iy, iz])
                        per_box_correlation_functions[ix][iy].append(correlation_function)
                else:
                    correlation_function = autocorrelation_function(self.number_matrix[:, ix, iy])
                    per_box_correlation_functions[ix].append(correlation_function)
        self.per_box_correlation_functions = per_box_correlation_functions
        # Calculate the average correlation function
        remaining_axis = calculate_remaining_axis(self.dimension)
        nb_boxes = np.prod(np.shape(self.per_box_correlation_functions)[:-1])
        self.correlation_function = np.mean(per_box_correlation_functions,
                                            axis = remaining_axis)
        self.err_correlation_function = np.std(per_box_correlation_functions,
                                               axis = remaining_axis)/np.sqrt(nb_boxes)
        

    def evaluate_mean_particle_number(self):
        """Evaluate <N> <N>^2 and <N^2>."""
        per_box_mean_of_N = []
        per_box_mean_of_square_of_N = []
        per_box_mean_of_N_squared = []
        for ix in np.arange(np.shape(self.number_matrix)[1]):
            per_box_mean_of_N.append([])
            per_box_mean_of_square_of_N.append([])
            per_box_mean_of_N_squared.append([])
            for iy in np.arange(np.shape(self.number_matrix)[2]):
                if self.dimension == 3:
                    per_box_mean_of_N[ix].append([])
                    per_box_mean_of_square_of_N[ix].append([])
                    per_box_mean_of_N_squared[ix].append([])
                    for iz in np.arange(np.shape(self.number_matrix)[3]):
                        per_box_mean_of_N[ix][iy].append(np.mean(self.number_matrix[:, ix, iy, iz]))
                        per_box_mean_of_square_of_N[ix][iy].append(np.mean(self.number_matrix[:, ix, iy, iz]**2))
                        per_box_mean_of_N_squared[ix][iy].append(np.mean(self.number_matrix[:, ix, iy, iz])**2)
                else:
                    per_box_mean_of_N[ix].append(np.mean(self.number_matrix[:, ix, iy]))
                    per_box_mean_of_square_of_N[ix].append(np.mean(self.number_matrix[:, ix, iy]**2))
                    per_box_mean_of_N_squared[ix].append(np.mean(self.number_matrix[:, ix, iy])**2)       
        self.per_box_mean_of_N = per_box_mean_of_N
        self.per_box_mean_of_square_of_N = per_box_mean_of_square_of_N
        self.per_box_mean_of_N_squared = per_box_mean_of_N_squared
        # Average <N> <N>^2 and <N^2> for the entire systems
        remaining_axis = calculate_remaining_axis(self.dimension)
        self.mean_of_N = np.mean(self.per_box_mean_of_N,
                                 axis = remaining_axis)
        self.mean_of_square_of_N = np.mean(self.per_box_mean_of_square_of_N,
                                           axis = remaining_axis)
        self.mean_of_N_squared = np.mean(self.per_box_mean_of_N_squared,
                                         axis = remaining_axis)

    def evaluate_deltan2(self):
        """Evaluate <deltan2>"""
        self.delta_n2 = 2*(self.mean_of_square_of_N-self.mean_of_N_squared) \
            - 2*(self.correlation_function - self.mean_of_N_squared)
