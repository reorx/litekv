#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.6'

from setuptools import setup

with open('README.rst', 'r') as f:
    long_desc = f.read()

setup(
    name='litekv',
    version=__version__,
    author='reorx',
    url='http://github.com/reorx/litekv',
    description="Simple kv store for Python",
    long_description=long_desc,
    py_modules=['litekv']
)
