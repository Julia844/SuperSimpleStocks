#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Super Simple Stocks
# https://github.com/tgorka/SuperSimpleStocks
#
# Copyright (C) 2016 Tomasz Gorka <http://tomasz.gorka.org.pl>
#
import unittest

from tests import csv_path

from supersimplestocks import __main__ as main


class MainTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # load initial data
        cls._load_divident_data()
        # load data for MTS
        cls._load_single_divident_data()
        # trade
        cls._record_trade()

    @classmethod
    def _load_divident_data(cls):
        main.main(['supersimplestocks', '--action=load_dividends', csv_path()])

    @classmethod
    def _load_single_divident_data(cls):
        main.main(['supersimplestocks', '--action=load_dividend', 'MTS',
                   'Preferred', '10', '2%', '100'])
        main.main(['supersimplestocks', '-a' , 'load_dividend', 'MTS1',
                   'Common', '10', '', '100'])

    @classmethod
    def _record_trade(cls):
        for symbol in ['MTS', 'MTS1']:
            main.main(['supersimplestocks', '--action=trade', symbol,
                       'SELL', '1000', '10.5'])
            main.main(['supersimplestocks', '-a', 'trade', symbol,
                       'BUY', '100', '10.5'])
            main.main(['supersimplestocks', symbol, 'BUY', '50', '10.5'])

    def test_help(self):
        with self.assertRaises(SystemExit):
            print('\n')
            main.main(['supersimplestocks', '--help'])

    def test_help_short(self):
        with self.assertRaises(SystemExit):
            print('\n')
            main.main(['supersimplestocks', '-h'])

    def test_stock_price(self):
        print('\n Stock price for MTS:')
        main.main(['supersimplestocks', '--action=price', 'MTS'])
        main.main(['supersimplestocks', '-a', 'price', 'MTS'])

    def test_dividend_yield(self):
        print('\n Dividend yield for MTS / MTS1:')
        main.main(['supersimplestocks', '--action=dividend', 'MTS'])
        main.main(['supersimplestocks', '-a', 'dividend', 'MTS1'])

    def test_p_e_ratio(self):
        print('\n P\E Rato for MTS / MTS1:')
        main.main(['supersimplestocks', '--action=pe', 'MTS'])
        main.main(['supersimplestocks', '-a', 'pe', 'MTS1'])

    def test_gbce(self):
        print('\n GBCE:')
        main.main(['supersimplestocks', '--action=gbce'])
        main.main(['supersimplestocks', '-a', 'gbce'])


if __name__ == '__main__':
    unittest.main()