import numpy as np
import os
import git

# detect the location of the Git repository
current_path = os.getcwd()
git_repo = git.Repo(current_path, search_parent_directories=True)
git_path = git_repo.git.rev_parse("--show-toplevel")

# import countoscope
from countoscope import Countoscope

# Known information about the "three_sliding_particles" simulation:
info_three_sliding_particles = {
    "expected_box_boundaries": [[0, 30.0], [0, 10.0], [0, 10.0]],
    "expected_bound_length": [4, 2, 2],
    "expected_matrix_size": [3, 1, 1],
    "expected_dimension": 3,
    "expected_mean_of_N": 1.0,
    "expected_mean_of_square_of_N": 1.0,
    "expected_mean_of_N_squared": 1.0,
    "expected_correlation_value": 1.0,
    "expected_delta_n2": 0.0,
    "filename_xyz": git_path+"/datasets/"\
        +"ideal-cases/three-sliding-particles/dump.xyz",
    "filename_lammpstrj": git_path+"/datasets/"\
        +"ideal-cases/three-sliding-particles/dump.lammpstrj"}

def apply_countoscope():
    """Apply countoscope to the three sliding particles system"""
    results = Countoscope(
        trajectory_file = info_three_sliding_particles["filename_lammpstrj"],
        box_size = np.array([10, 10, 10]),
        symmetric_system = False)
    results.run()
    return results

def test_detect_box_properties():
    """Make sure that the box properties are correctly detected."""
    results = apply_countoscope()
    assert results.dimension == info_three_sliding_particles["expected_dimension"], \
        """The dimension should be detected as 3"""
    for dim in [0, 1, 2]:
        assert info_three_sliding_particles["expected_box_boundaries"][dim][1] \
            == results.system_boundaries[dim][1], """Unexpected box boundaries"""
        assert info_three_sliding_particles["expected_bound_length"][dim] \
            == len(results.box_bounds[dim]), """Unexpected number of boxes"""
        assert info_three_sliding_particles["expected_matrix_size"][dim] \
            == np.shape(results.number_matrix)[dim+1], """Unexpected matrix size"""
        
def test_detect_particle_number():
    """Make sure that the averaged particle number is correct."""
    results = apply_countoscope()
    assert results.mean_of_N == info_three_sliding_particles["expected_mean_of_N"], \
        """The average number of particle in boxes is wrong"""
    assert results.mean_of_N_squared == info_three_sliding_particles["expected_mean_of_N_squared"], \
        """The average number of particle squared in boxes is wrong"""
    assert results.mean_of_square_of_N == info_three_sliding_particles["expected_mean_of_square_of_N"], \
        """The squared average number of particle is wrong"""
    assert results.correlation_function[0] == info_three_sliding_particles["expected_correlation_value"]
    assert results.delta_n2[0] == info_three_sliding_particles["expected_delta_n2"]
