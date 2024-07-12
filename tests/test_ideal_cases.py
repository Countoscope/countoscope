import numpy as np
# detect the location of the Git repository
import os
import git
current_path = os.getcwd()
git_repo = git.Repo(current_path, search_parent_directories=True)
git_path = git_repo.git.rev_parse("--show-toplevel")
filename_xyz = git_path+"/datasets/"\
    +"ideal-cases/three-sliding-particles/dump.xyz"
filename_lammpstrj = git_path+"/datasets/"\
    +"ideal-cases/three-sliding-particles/dump.lammpstrj"

from countoscope import Countoscope

expected_box_boundaries = [[0, 30.0], [0, 10.0], [0, 10.0]]
expected_bound_length = [4, 2, 2]
expected_matrix_size = [3, 1, 1]
expected_dimension = 3

def test_detect_box_properties():
    """Make sure that the box properties are correctly detected."""

    results = Countoscope(trajectory_file = filename_lammpstrj,
        box_size = np.array([10, 10, 10]),
        symmetric_system = False)
    results.run()

    assert results.dimension == expected_dimension, \
        """The dimension should be detected as 3"""
    for dim in [0, 1, 2]:
        assert expected_box_boundaries[dim][1] \
            == results.system_boundaries[dim][1], """Unexpected box boundaries"""
        assert expected_bound_length[dim] \
            == len(results.box_bounds[dim]), """Unexpected number of boxes"""
        assert expected_matrix_size[dim] \
            == np.shape(results.number_matrix)[dim+1], """Unexpected matrix size"""