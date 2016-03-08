#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Super Simple Stocks
# https://github.com/tgorka/SuperSimpleStocks
#
# Copyright (C) 2016 Tomasz Gorka <http://tomasz.gorka.org.pl>
#
import unittest

from tests import begin_date, trades, dividends
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


if __name__ == '__main__':
    unittest.main()