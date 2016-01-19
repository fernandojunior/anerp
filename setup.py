#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from pip.req import parse_requirements as parse

# Parse a requirements file to string list
requirements = lambda f: [str(i.req) for i in parse(f, session=False)]

# Read the README file
with open("README.rst") as f:
    README = f.read()

# Manually extract the __about__
__about__ = {}
with open("anerp/__about__.py") as f:
    exec(f.read(), __about__)

setup(
    author=__about__['__author__'],
    author_email=__about__['__email__'],
    classifiers=[
        'Environment :: Web Environment',
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ' + __about__['__license__'],
        'Natural Language :: English',
        'Operating System :: OS Independent',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    description=__about__['__description__'],
    include_package_data=True,
    install_requires=requirements('requirements.txt'),
    license=__about__['__license__'],
    long_description=README,
    name=__about__['__slug__'],
    packages=find_packages(exclude=['tests']),
    platforms='any',
    url=__about__['__url__'],
    version=__about__['__version__'],
    zip_safe=False
)
