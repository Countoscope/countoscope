
.. 
  # TO UNCOMMENT WHEN YOU HAVE A DOI
  .. image:: https://zenodo.org/badge/443812727.svg
     :target: https://zenodo.org/doi/10.5281/zenodo.13354423
     :alt: DOI

.. image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://opensource.org/licenses/MIT

.. image:: https://github.com/Countoscope/countoscope/actions/workflows/python-app.yml/badge.svg
   :target: https://github.com/Countoscope/countoscope/actions/workflows/python-app.yml

Countoscope (Python)
####################

This is the repository containing the Python code of the Countoscope.

Installation (users)
--------------------
Clone the repository using:

..  code:: bash

  git clone https://github.com/Countoscope/countoscope.git

Install all the required Python packages using:

..  code:: bash

    pip install -r requirements.txt

Then, type:

..  code:: bash

    pip install .

Installation (developers)
-------------------------
Clone the repository with its submodule (containing datasets for testing) using:

..  code:: bash

  git clone https://github.com/Countoscope/countoscope.git --recurse-submodules

You will need Git LFS installed (https://git-lfs.com/)

Install all the required Python packages using:

..  code:: bash

    pip install -r requirements.txt

Then, type:

..  code:: bash

    pip install -e .

Use
---

See examples/example_xyz.py

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
