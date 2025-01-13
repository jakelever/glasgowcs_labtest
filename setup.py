#!/usr/bin/env python

from distutils.core import setup

from setuptools import setup,find_packages

setup(name='glasgowcs_labtest',
	version='1.1.3',
	description='Testing framework for Glasgow CS classes',
	url='https://github.com/jakelever/glasgowcs_labtest',
	author='Jake Lever',
	author_email='jake.lever@glasgow.ac.uk',
	license='MIT',
	packages=find_packages())
	
