#!/usr/bin/env python
# -*- Mode: python; tab-width: 4; indent-tabs-mode:nil; coding:utf-8 -*-
#
# Copyright (c) 2024 Authors and contributors
# (see the AUTHORS.rst file for the full list of names)
#
# Released under MIT Licence
"""Module for counting the particles into the boxes."""
from box import Box
import numpy as np


class Sorting(Box):
    def __init__(self,
                 start = None,
                 stop = None,
                 *args,
                 **kwargs
                 ):
        super().__init__(*args, **kwargs)
        self.start = start
        self.stop = stop
        self.run_sorting()

    def run_sorting(self):
        self.prepare_run()
        self.store_particle_into_boxes()

    def prepare_run(self):
        """Detect starting and stopping frames for analysis."""
        if self.start is None:
            self.start = 0
        if self.stop is None:
            self.stop = self.nb_steps
        
    def store_particle_into_boxes(self):
        """Run over the trajectory and place the particles into number_matrix"""
        for i in np.arange(self.start, self.stop):
            frame = self.trajectory.read_step(i)
            #positions = frame.positions
            #if self.variable == "x":
            #    weights = None
            #elif self.variable == "v":
            #    weights = np.linalg.norm(self.atom_group.velocities, axis=1)
            #elif self.variable == "f":
            #    weights = np.linalg.norm(self.atom_group.forces, axis=1)
            # todo: allow atom selection
            if self.dimension == 2:
                H, _ = np.histogramdd(frame.positions[:,0:2],
                                      bins = (len(self.box_bounds[0])-1,
                                              len(self.box_bounds[1])-1,),
                                      range = ((np.min(self.box_bounds[0]),
                                                np.max(self.box_bounds[0])),
                                                (np.min(self.box_bounds[1]),
                                                 np.max(self.box_bounds[1]))))
                self.number_matrix[i, :, :] = H
            elif self.dimension == 3:
                H, _ = np.histogramdd(frame.positions,
                                    bins = (len(self.box_bounds[0])-1,
                                            len(self.box_bounds[1])-1,
                                            len(self.box_bounds[2])-1),
                                    range = ((np.min(self.box_bounds[0]),
                                            np.max(self.box_bounds[0])),
                                            (np.min(self.box_bounds[1]),
                                            np.max(self.box_bounds[1])),
                                            (np.min(self.box_bounds[2]),
                                            np.max(self.box_bounds[2]))))
                                    #weights=weights)
                self.number_matrix[i, :, :, :] = H