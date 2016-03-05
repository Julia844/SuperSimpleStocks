#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2016 LUXIA SAS
#
import os, sys
from optparse import OptionParser

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

    #stocs = Stocs()
    print('Hello world')
    import pyspark
    print('pyspark' in sys.modules)

    ##TODO: implement me!
    print(data_path)


    return 0

sys.exit(main())