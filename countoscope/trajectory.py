#!/usr/bin/env python
# -*- Mode: python; tab-width: 4; indent-tabs-mode:nil; coding:utf-8 -*-
#
# Copyright (c) 2024 Authors and contributors
# (see the AUTHORS.rst file for the full list of names)
#
# Released under MIT Licence
"""Module for preparing the trajectories."""
import os
import numpy as np
import MDAnalysis as mda
from chemfiles import Trajectory as chem_traj


class Trajectory:
    r"""Class providing options for importing the trajectory."""

    def __init__(self,
                 trajectory_file: str,
                 topology_file: str = None,
                 system_size: np.array = None,
                 dimension: int = None,
                 symmetric_system: bool = False,
                 *args,
                 **kwargs
                 ):
        super().__init__(*args, **kwargs)
        self.trajectory_file = trajectory_file
        self.topology_file = topology_file
        self.system_size = system_size
        self.dimension = dimension
        self.symmetric_system = symmetric_system
        self.run_trajectory()

    def run_trajectory(self):
        self.import_trajectory()
        self.read_information_trajectory()
        self.detect_system_dimension()
        self.detect_system_size()

    def import_trajectory(self):
        """Import trajectory file using Chemfiles"""
        # Make sure that the trajectory file exists.
        assert os.path.exists(self.trajectory_file),  \
            """Error: Trajectory not found."""
        # Import the trajectory file using Chemfiles.
        self.trajectory = chem_traj(self.trajectory_file)
        # If provided, add the topology to the trajectory.
        if self.topology_file is not None:
            self.trajectory.set_topology(self.topology_file)

    def read_information_trajectory(self):
        """Read basic information from trajectory"""
        self.nb_steps = self.trajectory.nsteps
        # If box_size was not provided, try reading it from trajectory.
        if self.system_size is None:
            self.system_size = np.array(self.trajectory.read_step(0).cell.lengths)
        # If box_size is 0, return a warning
        assert np.sum(np.array(self.system_size)) > 0, \
            """Error: No box size in trajectory, provide system_size"""
        
    def detect_system_dimension(self):
        """Attempt to guess the dimension from the trajectory.
        
        In case the dimension was entered by the user, make sure its value is
        consistent.
        """
        if self.dimension is None:
            # Measure the number of column of the particle positions
            number_columns = np.shape(self.trajectory.read_step(0).positions)[1]
            if number_columns == 2:
                # This may not be a possibility.
                dimension = 2
            elif number_columns == 3:
                if np.sum(self.trajectory.read_step(0).positions[:,2]**2) == 0:
                    # All the z-coordinate are 0, then its assumed that the simulation is 2D
                    dimension = 2
                    print("INFO: the trajectory was detected as 2D. If it is "
                        "a mistake, provide dimension.")
                else:
                    dimension = 3
            else:
                print("Wrong number of coordinate in the trajectory."
                      "Must be 2 or 3.")
            self.dimension = dimension
        elif self.dimension == 3:
            if np.sum(self.trajectory.read_step(0).positions[:,2]**2) == 0:
                print("INFO: the selected dimension is 3 "
                    "but the particule coordinates seem to be 0 along z.")
        else:
            assert (self.dimension == 2) | (self.dimension == 3), \
                """ERROR: Unsuported dimension. Must be 2 or 3."""
            
    def detect_system_size(self):
        """From the box size, estimate the system lower and higher coordinate."""
        system_boundaries = []
        for system_length in self.system_size:
            if self.symmetric_system:
                system_boundaries.append([-system_length/2, system_length/2])
            else:
                system_boundaries.append([0, system_length])
        self.system_boundaries = np.array(system_boundaries)