import numpy as np

class NumpyFrame():
    def __init__(self, positions):
        assert len(positions.shape) == 2
        self.positions = positions

class NumpyTrajectory:
    """a class that performs like a chemfiles trajectory"""
    def __init__(self, array, column_labels):
        self.array = array

        self.x_column = None
        self.y_column = None
        self.z_column = None
        self.t_column = None
        self.dimension = 2

        for column_index, column_header in enumerate(column_labels):
            if column_header == 'x':
                self.x_column = column_index
            if column_header == 'y':
                self.y_column = column_index
            if column_header == 'z':
                self.z_column = column_index
                self.dimension = 3
            if column_header == 't':
                self.t_column = column_index
        
        assert self.t_column is not None, 'column_headers must include "t"'
        assert self.x_column is not None, 'column_headers must include "x"'
        assert self.y_column is not None, 'column_headers must include "y"'

        # ensure timestep is zero-based
        self.array[:, self.t_column] -= self.array[:, self.t_column].min()
        self.nsteps = int(self.array[:, self.t_column].max() + 1)

    def get_system_size(self):
        if self.dimension == 2:
            return np.array([
                self.array[:, self.x_column].max(),
                self.array[:, self.y_column].max(),
            ])
        elif self.dimension == 3:
            return np.array([
                self.array[:, self.x_column].max(),
                self.array[:, self.y_column].max(),
                self.array[:, self.z_column].max(),
            ])

    def read_step(self, timestep):
        row_indices_at_timestep = self.array[:, self.t_column] == timestep
        array_at_timestep = self.array[row_indices_at_timestep, :]
        
        if self.dimension == 2:
            return NumpyFrame(array_at_timestep[:, [self.x_column, self.y_column]])
        elif self.dimension == 3:
            return NumpyFrame(array_at_timestep[:, [self.x_column, self.y_column, self.z_column]])