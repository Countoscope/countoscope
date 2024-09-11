from countoscope import Countoscope
import matplotlib.pyplot as plt
import numpy as np

"""
run this example from within the examples folder with
python example_xyz.py
"""

# this minimal working example currently uses a shortened copy of datasets/brownian-particles/2D-closed/trajectory.xyz

# set up the Countoscope
countoscope = Countoscope(
    trajectory_file  = 'trajectory2.xyz',
    box_size         = np.array([0.5, 0.5]),
    system_size      = np.array([10, 10]),
    symmetric_system = False,
)

# do the counting
countoscope.count()

# calcuate <dN^2(t)>
delta_N2 = countoscope.evaluate_deltaN2()

# plot
t = range(0, len(delta_N2))
plt.plot(t[1:], delta_N2[1:])
plt.loglog()
plt.savefig('example_xyz.png')
plt.show()


"""
In a Python script or a Jupyter Notebook, define the path to the data trajectory
file. For instance, using the `3D-closed` dataset provided in the `datasets`
repository:

..  code:: python

  path_to_data = "/mpath/datasets/datasets/3D-closed/trajectory.xyz"

Import the Countoscope as well as NumPy by typing:

..  code:: python

  from countoscope import Countoscope
  import numpy as np

The trajectory file `trajectory.xyz` corresponds to a system of 190 particles in
a :math:`(30 Å)^3` box. Let us define the system size as a NumPy array:

..  code:: python

    system_size = np.array([30, 30, 30])

Finally, let us choose a grid size for the Countoscope measurement:

..  code:: python

    box_size=np.array([10, 10, 10])

Then, launch the Countoscope calculation using *trajectory_file*, *system_size*,
and *box_size* as input parameters:

..  code:: python

    results = Countoscope(trajectory_file = path_to_data,
                        system_size=system_size,
                        box_size=box_size)
    results.run()

After the calculation is done, all the computed data can be obtained from the
`results`object. For instance, for :math:`<N>`, type:

..  code:: python

    print(np.round(results.mean_of_N,2))

which will return:

..  code:: bash

    0.84

To plot :math:`<\Delta N^2>`, let us import Pyplot first:

..  code:: python

    import matplotlib.pyplot as plt
    plt.loglog(results.delta_n2)
"""