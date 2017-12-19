from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='dask_parquet_integration',
    version='1.0.1',
    description='Files for integration testing parquet readers',
    url='https://github.com/dask/parquet_integration',
    author='Tom Augspurger',
    author_email='tom.w.augspurger@gmail.com',
    license="BSD",
    classifiers=[  # Optional
        'License :: OSI Approved :: BSD License'
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(),
    package_data={
        'dask_parquet_integration': ['data/*.parq',
                                     'data/*.parq/*'],
    },
)
