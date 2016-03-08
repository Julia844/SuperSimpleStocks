#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Super Simple Stocks
# https://github.com/tgorka/SuperSimpleStocks
#
# Copyright (C) 2016 Tomasz Gorka <http://tomasz.gorka.org.pl>
#
import sys
from optparse import OptionParser

import supersimplestocks


def check_argument(parser, arguments_count, arguments, api_fun):
    '''
    Check argument for correct len, call API function, or throw an error.

    :param parser: to throw an error
    :param arguments_count: count to match
    :param arguments: len to check and pass to api_fun
    :param api_fun: function to call
    :return:
    '''
    if len(arguments) != arguments_count:
        parser.error("Incorrect number of arguments. "
                     "For this action it should be %d." % arguments_count)

    return api_fun(*arguments)


def main(argv=None):
    '''
    The main function. Parse the command line parameters,
    call function from API.

    :param argv: arguments from the command line
    '''
    if argv is None:
        argv = sys.argv
    parser = OptionParser("usage: %prog [options] args. "
                          "Call %prog --help to see the options.")
    parser.add_option('-a', '--action', default='trade',
            help = "Set action to do. Possible actions: trade(by default), "
                   "load_dividends, load_dividend, price, pe, gbce.")
    options, arguments = parser.parse_args(argv[1:])

    undefined_action = lambda arguments: \
        parser.error("Incorrect action for --action/-a parameter.")

    result = {

        'trade': lambda arguments: check_argument(parser, 4, arguments,
                supersimplestocks.record_trade),

        'load_dividends': lambda arguments: check_argument(parser, 1, arguments,
                supersimplestocks.load_dividend_data),

        'load_dividend': lambda arguments: check_argument(parser, 5, arguments,
                supersimplestocks.record_dividend_data),

        'dividend': lambda arguments: check_argument(parser, 1, arguments,
                supersimplestocks.dividend_yield),

        'price': lambda arguments: check_argument(parser, 1, arguments,
                supersimplestocks.stock_price),

        'pe': lambda arguments: check_argument(parser, 1, arguments,
                supersimplestocks.p_e_ratio),

        'gbce': lambda arguments: check_argument(parser, 0, arguments,
                supersimplestocks.gbce),

    }.get(options.action, undefined_action)(arguments)

    if result is not None:
        print(result)

    return 0


if __name__ == '__main__':
    sys.exit(main())