#!/usr/bin/env python
# coding=utf-8

from setuptools import setup

with open('README.md', 'r') as detailed_description:
    detailed_description = detailed_description.read()

setup(
    name='soigne',
    version='0.1.8b5',
    url='https://github.com/jm-organization/soigne',
    license='GPL-3.0',
    author='gromovjm',
    author_email='vany.58.98.2013@gmail.com',
    description='A Python application framework.',
    long_description=detailed_description,
    long_description_content_type="text/markdown",

    install_requires=[
        'pygame==2.0.0.dev6',
    ],
    packages=['soigne', 'soigne.components'],
    python_requires='>=3.8',

    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
