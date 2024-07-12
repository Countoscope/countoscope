Py-Countoscope
##############

This is the repository containing the Python code of the countoscope.

Clone the repository using:

..  code::

  git clone https://github.com/Countoscope/countoscope.git

Optionally, clone the repository with its submodule using:

..  code::

  git clone https://github.com/Countoscope/countoscope.git --recurse-submodules

Installation
------------

Install all the required Python packages using:

..  code::

    pip install -r requirements.txt

Then, type:

..  code::

    pip install .

Run the tests
-------------

Go to the tests/ repository, then type:

..  code::

    pytest .

Note that the repository must have been cloned with its submodules for the tests to work.

To-do list
----------

- allow the user to input his/her own grid with specific box ?
- allow group selection (for trajectory with different type of particles)
- test if numba helps making the code faster
- allow for inputing data in a numpy array
- allow for inputing data pandas dataframe,
_ make an extra too for converting automatically data into a regular format (like XYZ)

When the repository is public:

- have the GitHub runners automatically launch the tests
- integrate the python modules into the public documentation
