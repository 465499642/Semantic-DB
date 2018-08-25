#!/usr/bin/env python

from distutils.core import setup

setup(
    name='Semantic-DB',
    version='2.0',
    description='',
    author='Garry Morrison',
    author_email='garry@semantic-db.org',
    url='http://semantic-db.org/documentation/usage/index.html',
    packages=['semantic-db'],
    install_requires=[
        'parsley',
        'numpy',
        'matplotlib',
    ],
    extras_require={
        'Graph':  ["graphviz"],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
    ],
)