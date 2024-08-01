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

In a Python script or a Jupyter notebook:

..  code:: python

  path_to_data = "/path/data/trajectory.xyz"

  from countoscope import Countoscope

  results = Countoscope(trajectory_file = path_to_data)
  results.run()

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
