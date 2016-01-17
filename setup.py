#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages
from pip.req import parse_requirements as parse
import anerp as package

# Gives the relative path of a file from the setup.py
relpath = lambda filename: os.path.join(os.path.dirname(__file__), filename)

# Parse a requirements file to string list
requirements = lambda f: [str(i.req) for i in parse(relpath(f), session=False)]

# Read the README file
with open("README.rst") as f:
    README = f.read()

setup(
    author=package.__author__,
    author_email=package.__email__,
    classifiers=[
        'Environment :: Web Environment',
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ' + package.__license__,
        'Natural Language :: English',
        'Operating System :: OS Independent',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],  # see more: https://pypi.python.org/pypi?%3Aaction=list_classifiers
    description='An ERP',
    include_package_data=True,
    install_requires=requirements('requirements.txt'),
    keywords='anerp',
    license=package.__license__,
    long_description=README,
    name='anerp',
    packages=find_packages(exclude=['tests']),
    platforms='any',
    url='https://github.com/fernandojunior/anerp',
    version=package.__version__,
    zip_safe=False
)
