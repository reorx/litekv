#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.5'

from setuptools import setup

with open('README.rst', 'r') as f:
    desc = f.read()

setup(
    name='litekv',
    version=__version__,
    author='reorx',
    url='http://github.com/reorx/litekv',
    description=desc,
    py_modules=['litekv']
)
