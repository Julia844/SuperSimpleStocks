#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Super Simple Stocks
# https://github.com/tgorka/SuperSimpleStocks
#
# Copyright (C) 2016 Tomasz Gorka <http://tomasz.gorka.org.pl>
#
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

requires = [
    #'pyspark==1.6.0', # use PYTHONPATH pointing to this egg
    'py4j==0.9', # dependency of pyspark==1.6.0
]

setup(name='supersimplestocks',
        version='0.0.1',
        description='Super Simple Stocs',
        long_description=README,
        classifiers=[
            'Environment :: Console',
            'Programming Language :: Python',
            'Operating System :: POSIX',
            'Framework :: Celery',
            'Framework :: Spark',
            'Library :: Numpy',
            'Topic :: Stock :: Analyses :: Application',
            'Intended Audience :: Developers',
            'License :: MIT',
        ],
        author='Tomasz Gorka',
        author_email='tomasz@gorka.org.pl',
        url='http://tomasz.gorka.org.pl',
        keywords='python celegry stock numpy',
        packages=find_packages(),
        include_package_data=True,
        zip_safe=False,
        install_requires = requires,
        tests_require = requires,
        test_suite='supersimplestocks',
        license='MIT',
)

