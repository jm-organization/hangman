#!/usr/bin/env python
# coding=utf-8

from setuptools import setup

setup(
    name='soigne',
    version='0.1.8.b3',
    url='https://github.com/jm-organization/soigne',
    license='GPL-3.0',
    author='gromovjm',
    author_email='vany.58.98.2013@gmail.com',
    description='A Python application framework.',

    install_requires=[
        'pygame==2.0.0.dev6',
        'python_version>"3.8"'
    ],
    packages=['soigne', 'soigne.components'],

    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
