#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='gofedresources',
    version='0.0.1',
    description='Gofed resources',
    long_description=''.join(open('README.md').readlines()),
    keywords='gofed,resources',
    author='Jan Chaloupka',
    author_email='jchaloup@redhat.com',
    url='https://github.com/gofed/resources',
    license='GPL',
    packages=['gofedresources', 'gofedresources.config'],
    install_requires=open('requirements.txt').read().splitlines()
)
