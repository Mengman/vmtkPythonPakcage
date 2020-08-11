import os
from skbuild import setup, constants
from setuptools import find_packages
import shlex

setup(
    name='vmtk-infervision',
    version='1.4.0',
    author='vmtk author',
    packages=["vmtk"],
    package_dir={"vmtk": "vmtk"},
    cmake_args=shlex.split(os.environ.get('VMTK_CMAKE_ARGS', '')),
    description="vmtk",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: C++",
    ]
)
