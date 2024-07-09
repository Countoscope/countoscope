# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='countoscope',
    version='0.0.1',
    description='A code to count particles in boxes',
    long_description=readme,
    author='See the AUTHORS.rst file',
    author_email='',
    url='https://github.com/countoscope/',
    license=license,
    packages=find_packages(exclude=('tests'))
)

