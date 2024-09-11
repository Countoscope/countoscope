from countoscope import Countoscope
import numpy as np

def test_load_numpy_trajs():
    trajs = np.array([
    #    x    y    t
        [0.0, 0.0, 0],
        [1.0, 0.0, 0],
        [0.0, 1.0, 1],
        [1.0, 1.0, 1],
    ])

    countoscope = Countoscope(
        box_size          = np.array([0.5, 0.5]),
        trajectory_array  = trajs,
        trajectory_labels = ['x', 'y', 't'],
    )
    assert countoscope.nb_steps == 2
    assert np.all(countoscope.trajectory.read_step(0).positions == [[0.0, 0.0], [1.0, 0.0]])

    countoscope.count()
    assert np.all(countoscope.number_matrix == [
        [[1, 0],
         [1, 0]],
        [[0, 1],
         [0, 1]],
    ])

def test_load_numpy_trajs_3D():
    trajs = np.array([
    #    x    y    z    t
        [0.0, 0.0, 1.0, 0],
        [1.0, 0.0, 0.5, 0],
        [0.0, 1.0, 0.5, 1],
        [1.0, 1.0, 0.0, 1],
    ])

    countoscope = Countoscope(
        box_size          = np.array([0.5, 0.5, 0.5]),
        trajectory_array  = trajs,
        trajectory_labels = ['x', 'y', 'z', 't'],
    )
    countoscope.count()
