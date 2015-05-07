import os
import multiprocessing
from setuptools import setup
from os.path import join as pjoin

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pyselfcal",
    version = "0.0.1",
    author = "Nicolas Vilchez",
    author_email = "vilchez@astron.nl",
    description = ("A tool to run the selfcal cycle for lofar images, "
                   "using the LOFAR software stack (DPPP, BBS, awimager."),
    packages=['pyselfcal'],
    scripts=[pjoin('bin','selfcal.py'), pjoin('bin','old_selfcal.py'), pjoin('bin','mergeSB.py')],
    install_requires=['pyvo>=0.1','LSMTool'],
    dependency_links=['https://github.com/darafferty/LSMTool/tarball/master#egg=LSMTool-1.0.0',
                      'https://github.com/pyvirtobs/pyvo/tarball/master#egg=pyvo-0.1' ],
)
