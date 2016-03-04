#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Super Simple Stocss
# https://github.com/tgorka/SuperSimpleStocks
#
# Copyright (C) 2016 Tomasz Gorka <http://tomasz.gorka.org.pl>
#
import os, sys
from optparse import OptionParser

import numpy

class Stocs:
    '''
    Stocs class for calculation algorithms over the stocs.
    @see README.md how to use it.
    '''
    pass

class Stock:

    def mean(self):
        a = [1,2,3,4]
        return numpy.mean(a)


def main(argv=None):
    '''
    The main function. Parse the command line parameters, call Stocs

    :param argv: arguments from the command line
    '''
    if argv is None:
        argv = sys.argv
    parser = OptionParser("usage: %prog [options] data_scv_path")
    parser.add_option('-f', '--force', default=False,
            help = "Force to import data even it was imported previously")
    options, arguments = parser.parse_args(argv[1:])
    if len(arguments) != 1:
        parser.error("Incorrect number of arguments")
    data_path = os.path.abspath(arguments[0])

    stocs = Stocs()
    ##TODO: implement me!
    print(data_path)


    return 0

if __name__ == 'main':
    sys.exit(main())