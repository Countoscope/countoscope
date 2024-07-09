#!/usr/bin/env python
# -*- Mode: python; tab-width: 4; indent-tabs-mode:nil; coding:utf-8 -*-
#
# Copyright (c) 2024 Authors and contributors
# (see the AUTHORS.rst file for the full list of names)
#
# Released under MIT Licence
"""Module for preparing the trajectories."""
import numpy as np
import MDAnalysis as mda


class Trajectory:
    def __init__(self,
                 trajectory: np.ndarray = None,
                 universe: mda.Universe = None,
                 *args,
                 **kwargs
                 ):
        super().__init__(*args, **kwargs)
        self.trajectory = trajectory,
        self.universe = universe,
    def run(self):
        print(self.trajectory)
        print(self.universe)