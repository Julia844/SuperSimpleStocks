#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Super Simple Stocks
# https://github.com/tgorka/SuperSimpleStocks
#
# Copyright (C) 2016 Tomasz Gorka <http://tomasz.gorka.org.pl>
#
import os, sys
from optparse import OptionParser

from supersimplestocks import tasks, load_dividend_data


def main(argv=None):
    '''
    The main function. Parse the command line parameters, call Stocs

    :param argv: arguments from the command line
    '''
    #app.start()
    if argv is None:
        argv = sys.argv
    parser = OptionParser("usage: %prog [options] data_scv_path")
    parser.add_option('-s', '--server', default=False,
            help = "Run distributed server by celery using command: celery -A supersimplestocks --server worker -l info")
    options, arguments = parser.parse_args(argv[1:])
    if len(arguments) != 1:
        parser.error("Incorrect number of arguments")
    data_path = os.path.abspath(arguments[0])

    if options.server:
        print('server')
        return 0
    else:
        print('not server')
        #return 0

    # load dividend data from csv
    load_dividend_data(data_path)

    for i in range(101):
        tasks.record_trade.delay('TEA', 'SELL', 100, 90)
    for i in range(9):
        tasks.record_trade.delay('TEA', 'BUY', 1000, 90)

    return 0


sys.exit(main())