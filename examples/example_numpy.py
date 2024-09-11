from countoscope import Countoscope
import matplotlib.pyplot as plt
import numpy as np

"""
run this example from within the examples folder with
python example_numpy.py
"""

# load dataset
# this example is an array of rows of (x, y, t) - eg from Trackpy
data = np.load('example_dataset.npy')
column_labels = ['x', 'y', 't']

# set up the Countoscope
countoscope = Countoscope(
    trajectory_array  = data,
    trajectory_labels = column_labels, # the column labels
    box_size          = np.array([0.5, 0.5]),
)

# do the counting
countoscope.count()

# calcuate <dN^2(t)>
delta_N2 = countoscope.evaluate_deltaN2()

# plot
t = range(0, len(delta_N2))
plt.plot(t[1:], delta_N2[1:])
plt.loglog()
plt.savefig('example_numpy.png')
plt.show()