from skbuild import setup
from setuptools import find_packages

setup(
    name='vmtk-infervision',
    version='1.4.0',
    author='vmtk author',
    packages=find_packages(),
    description="vmtk",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: C++",
    ]
)