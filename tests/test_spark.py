#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Super Simple Stocks
# https://github.com/tgorka/SuperSimpleStocks
#
# Copyright (C) 2016 Tomasz Gorka <http://tomasz.gorka.org.pl>
#
import unittest

from tests import begin_date, now, trades, dividends
from supersimplestocks import spark as sp


class SparkTestCase(unittest.TestCase):

    # spark object for distributed calculations
    spark = sp.Spark()

    def test_stock_price(self):
        stock_price = self.spark.stock_price('STS', begin_date, trades)
        print('\n Stock price for STS: %f' % stock_price)
        assert stock_price == 0.274625, 'Stock price for STS should be 0.274625'

        stock_price = self.spark.stock_price('STS1', begin_date, trades)
        print('\n Stock price for STS1: %f' % stock_price)
        assert stock_price == 0.65, 'Stock price for STS1 should be 0.65'

    def test_gbce(self):
        gbce = self.spark.gbce(begin_date, trades)
        print('\n GBCE: %f' % gbce)
        assert gbce == 0.4225, 'GBCE should be 0.4225'

    def test_compatible_trades(self):
        compatible_trades = self.spark.compatible_trades({
            'id': '6279b4d5-3e26-4eb7-bf95-1e4e7a6f56f0',
            'datetime': now,
            'symbol': 'STS',
            'type': 'BUY',
            'quantity': 1000,
            'price': 0.274625,
            'open_quantity': 1000,
            'registered': []
        }, trades)
        print('\n Compatible trades:', compatible_trades)
        assert len(compatible_trades) == 1 and \
               compatible_trades[0]['id'] == trades[0]['id'], \
            'There is only one compatible trade'

    def test_last_dividend(self):
        last_dividend = self.spark.last_dividend('STS', dividends)
        print('\n Last dividend:', last_dividend)
        assert last_dividend is not None and \
               last_dividend['symbol'] == dividends[0]['symbol'], \
            'Compatible dividend'

        last_dividend = self.spark.last_dividend('STSX', dividends)
        assert last_dividend is None, 'There shouldn\'t be divident STSX'


if __name__ == '__main__':
    unittest.main()