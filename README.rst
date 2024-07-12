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

Go to the test/ repository, then type:

..  code::

    pytest .

Note that the repository must have been cloned with its submodules for the tests to work.

To-do list
----------

- have the GitHub runners automatically launch the tests. Currently it doesn't, probably because the repo is private
- allow the user to input his/her own grid
- allow group selection
- test if numba helps
