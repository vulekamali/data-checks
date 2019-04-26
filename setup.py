from setuptools import setup, find_packages


setup(
    name="data-checks",
    version="0.1",
    packages=find_packages(exclude=('tests',)),
)
