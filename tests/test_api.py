#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Super Simple Stocks
# https://github.com/tgorka/SuperSimpleStocks
#
# Copyright (C) 2016 Tomasz Gorka <http://tomasz.gorka.org.pl>
#
import os
import random
import unittest

import supersimplestocks


class ApiTestCase(unittest.TestCase):

    symbols = ['TEA', 'POP', 'ALE', 'GIN', 'JOE']
    types = ['SELL', 'BUY']
    quantities = range(0, 1000, 5)
    prices = [10, 10000, 73, 29, 1, 923, 0]

    @classmethod
    def setUpClass(cls):
        # geting path to the csv file
        csv_path = os.path.abspath(__file__)
        csv_path = os.path.dirname(csv_path)
        csv_path = os.path.join(csv_path, '../example/data.csv')
        csv_path = os.path.abspath(csv_path)
        # load dividents data from csv
        supersimplestocks.load_dividend_data(csv_path)
        # load samte trades
        cls._record_trade()

    @classmethod
    def _record_trade(cls):
        print('\n')
        for i in range(1000):
            args = [
                random.choice(cls.symbols),
                random.choice(cls.types),
                random.choice(cls.quantities),
                random.choice(cls.prices)
            ]
            supersimplestocks.record_trade(*args)

            print('trading:', 'SYMBOL:', args[0], 'TYPE:', args[1],
                  'QUANTITY:', args[2], 'PRICE:', args[3])

    def test_stock_price(self):
        print('\n')
        for symbol in self.symbols:
            print('Stock price for %s:' % symbol,
                  supersimplestocks.stock_price(symbol))

    def test_dividend_yield(self):
        print('\n')
        for symbol in self.symbols:
            print('Dividend yield for %s:' % symbol,
                  supersimplestocks.dividend_yield(symbol))

    def test_p_e_ratio(self):
        print('\n')
        for symbol in self.symbols:
            print('P/E Ratio for %s:' % symbol,
                  supersimplestocks.p_e_ratio(symbol))

    def test_gbce(self):
        print('\n')
        print('GBCE:', supersimplestocks.gbce())


if __name__ == '__main__':
    unittest.main()
