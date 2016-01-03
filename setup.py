#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages
import anerp as package

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
packages = find_packages(exclude=['*.tests', '*.tests.*', 'tests.*', 'tests'])

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
    install_requires=[],
    keywords='anerp',
    license=package.__license__,
    long_description=README,
    name='anerp',
    packages=packages,
    platforms='any',
    test_suite='tests',
    tests_require=[],
    url='https://github.com/fernandojunior/anerp',
    version=package.__version__,
    zip_safe=False
)
