Py-Countoscope
##############

This is the repository containing the Python code of the countoscope.

Clone the repository using:

..  code:: bash

  git clone https://github.com/Countoscope/countoscope.git

Optionally, clone the repository with its submodule using:

..  code:: bash

  git clone https://github.com/Countoscope/countoscope.git --recurse-submodules

Installation
------------

Install all the required Python packages using:

..  code:: bash

    pip install -r requirements.txt

Then, type:

..  code:: bash

    pip install .

Use
---

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

Run the tests
-------------

Go to the tests/ repository, then type:

..  code:: bash

    pytest .

Note that the repository must have been cloned with its submodules for the tests to work.

To-do list
----------

- allow the user to input his/her own grid with specific box ?
- allow group selection (for trajectory with different type of particles)
- test if numba helps making the code faster
- allow for inputing data in a numpy array
- allow for inputing data pandas dataframe,
- make an extra tool for converting automatically data into a regular format (like XYZ) --> done, see tools.py
- re-add the features from countoscope_old, like the automated system-size detection
- allow for cross correlation between neighbor boxes

When the repository is public:

- have the GitHub runners automatically launch the tests
- integrate the python modules into the public documentation
- have branch protection
