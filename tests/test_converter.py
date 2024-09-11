import numpy as np

# import countoscope
from countoscope import Countoscope, convert_homemade_format

info_trajectory = {
    "filename_xyz": "../datasets/"\
        +"brownian-particles/2D-homemade/example_dataset.xyz",
    "filename_txt": "../datasets/"\
        +"brownian-particles/2D-homemade/example_dataset.txt",
    "expected_mean_of_N": 5,}

def apply_converted():
    """Convert home-made TXT file into XYZ"""
    convert_homemade_format(info_trajectory["filename_txt"],
                                        info_trajectory["filename_xyz"])

def test_countoscope(box_size=np.array([10, 10]),
                      system_size = np.array([100, 100])):
    """Apply countoscope to the three sliding particles system"""
    # Call the converter and generate the xyz file
    apply_converted()
    # Test the generated file
    countoscope = Countoscope(
        trajectory_file = info_trajectory["filename_xyz"],
        box_size = box_size,
        system_size = system_size,
        dimension = 2,
        symmetric_system = False)
    countoscope.count()
    assert np.round(countoscope.mean_of_N, 3) == info_trajectory["expected_mean_of_N"]
