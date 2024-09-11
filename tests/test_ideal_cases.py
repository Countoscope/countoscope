import numpy as np

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
    "filename_xyz": "../datasets/"\
        +"ideal-cases/three-sliding-particles/dump.xyz",
    "filename_lammpstrj": "../datasets/"\
        +"ideal-cases/three-sliding-particles/dump.lammpstrj"}

def apply_countoscope(box_size=np.array([10, 10, 10])):
    """Apply countoscope to the three sliding particles system"""
    countoscope = Countoscope(
        trajectory_file = info_three_sliding_particles["filename_lammpstrj"],
        box_size = box_size,
        symmetric_system = False)
    countoscope.count()
    return countoscope

def test_detect_box_properties():
    """Make sure that the box properties are correctly detected."""
    countoscope = apply_countoscope()
    assert countoscope.dimension == info_three_sliding_particles["expected_dimension"], \
        """The dimension should be detected as 3"""
    for dim in [0, 1, 2]:
        assert info_three_sliding_particles["expected_box_boundaries"][dim][1] \
            == countoscope.system_boundaries[dim][1], """Unexpected box boundaries"""
        assert info_three_sliding_particles["expected_bound_length"][dim] \
            == len(countoscope.box_bounds[dim]), """Unexpected number of boxes"""
        assert info_three_sliding_particles["expected_matrix_size"][dim] \
            == np.shape(countoscope.number_matrix)[dim+1], """Unexpected matrix size"""
        
def test_detect_particle_number():
    """Make sure that the averaged particle number is correct."""
    countoscope = apply_countoscope()
    countoscope.evaluate_deltaN2()
    assert countoscope.mean_of_N == info_three_sliding_particles["expected_mean_of_N"], \
        """The average number of particle in boxes is wrong"""
    assert countoscope.mean_of_N_squared == info_three_sliding_particles["expected_mean_of_N_squared"], \
        """The average number of particle squared in boxes is wrong"""
    assert countoscope.mean_of_square_of_N == info_three_sliding_particles["expected_mean_of_square_of_N"], \
        """The squared average number of particle is wrong"""
    assert countoscope.correlation_function[0] == info_three_sliding_particles["expected_correlation_value"]
    assert countoscope.delta_n2[0] == info_three_sliding_particles["expected_delta_n2"]

def test_detect_particle_number_different_size():
    """Make sure cutting the box in different way give consistent particle number."""
    for factor in [0.25, 0.5, 0.75, 1]:
        countoscope = apply_countoscope(box_size=np.array([10*factor, 10, 10]))
        assert np.round(countoscope.mean_of_N,3) \
            == np.round(factor*info_three_sliding_particles["expected_mean_of_N"], 3)
        assert np.round(countoscope.mean_of_N,3) \
            == np.round(factor*info_three_sliding_particles["expected_mean_of_square_of_N"], 3)
        assert np.round(countoscope.mean_of_N_squared,2) \
            == np.round((factor*info_three_sliding_particles["expected_mean_of_N"])**2, 2)
        
# put a test like that if we decide to keep the automatic division
#def test_uncompatible_slicing():
#    """Try to divide the box with an impossible value"""
#    u, group = import_universe(folder="three-sliding-particles/",
#        single_frame = False)
#    cts = COUNTOSCOPE(u, group, [2.8, 10, 10])
#    cts.run()
#    print(cts.l0_box[0])
#    assert cts.l0_box[0] == 3.28