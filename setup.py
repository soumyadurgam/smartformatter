
from setuptools import setup, find_packages

setup(
    name="smartformatter",
    version="0.1",
    packages=find_packages(),
    insatall_requires=["inflect"],
    author="Soumya",
    description="utility functions for smart formatting of names, phones, numbers.",
)

