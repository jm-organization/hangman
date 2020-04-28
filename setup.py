#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages as packages

setup(
    name='Hangman',
    version='0.1.7.dev8',
    url='https://github.com/jm-organization/hangman',
    license='GPL-3.0',
    author='gromovjm',
    author_email='vany.58.98.2013@gmail.com',
    description='Python application framework',

    install_requires=[
        'pygame==2.0.0.dev6',
        'python_version>"3.8"'
    ],
    packages=['hangman', 'hangman.components'],

    classifiers=[
        "Programming Language :: Python :: 3.8.2",
        "License :: OSI Approved :: GNU General Public License",
        "Operating System :: OS Independent",
    ],
)
