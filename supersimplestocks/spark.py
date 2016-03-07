#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Super Simple Stocks
# https://github.com/tgorka/SuperSimpleStocks
#
# Copyright (C) 2016 Tomasz Gorka <http://tomasz.gorka.org.pl>
#
from pyspark import SparkContext, SparkConf

class Spark():
    # private spark context variable
    __spart_context = None

    @property
    def spark_context(self):
        '''
        Get spark context if needed and initialize it on first run
        :return: spark context
        '''
        if self.__spart_context is None:
            conf = SparkConf().setAppName('supersimplestocs')
            self.__spart_context = SparkContext('local[2]', conf=conf)

        return self.__spart_context


    def compatible_trades(self, trade_offer, trades):
        '''
        Get compatible trades (according to price, oposite type,
        have open quantities.
        :param trade_offer: to get copmatible trades
        :param trades: to filter
        :return: list of compatible trades
        '''
        try_type = 'SELL' if trade_offer['type'] == 'BUY' else 'BUY'
        return self.spark_context.parallelize(trades). \
            filter(lambda offer: offer['type'] == try_type and
                                 offer['price'] == trade_offer['price'] and
                                 offer['open_quantity'] > 0). \
            sortBy(lambda offer: offer['datetime']). \
            collect()


    def stock_price(self, symbol, begin_datetime, trades):
        '''
        Get stock price based on the realized trades since the given time
        for given stock symbol.
        Algorithm: Sum(trade_price*trade_quantity) / Sum(trade_quantity)
        :param symbol: symbol of stock
        :param begin_datetime: begin date since to analyze
        :param trades: to analyze
        :return: calculated value
        '''
        def mapFun(trade):
            quantity = trade['quantity'] - trade['open_quantity']
            return trade['price'] * float(quantity), quantity

        filteredRdd = self.spark_context.parallelize(trades). \
            filter(lambda trade: trade['symbol'] == symbol and
                                 trade['datetime'] >= begin_datetime and
                                 trade['open_quantity'] < trade['quantity'])
        if filteredRdd.isEmpty():
            return None

        price, quantity = filteredRdd. \
            map(mapFun). \
            reduce(lambda price_quantity1, price_quantity2:
                    (price_quantity1[0] + price_quantity2[0],
                     price_quantity1[1] + price_quantity2[1]))

        return price / float(quantity) if quantity > 0 else None


    def last_dividend(self, symbol, dividents):
        '''
        Get last dividend from the list based on given symbol.
        :param symbol: symbol of stock
        :param dividents: to analyze
        :return: last dividend from the list or throw a ValueError if not exists
        '''
        filteredRdd  =  self.spark_context.parallelize(dividents). \
            filter(lambda divident: divident['symbol'] == symbol)

        return None if filteredRdd.isEmpty() else filteredRdd.first()


    def gbce(self, begin_datetime, trades):
        filteredRdd  = self.spark_context.parallelize(trades). \
            filter(lambda trade: trade['datetime'] >= begin_datetime and
                                 trade['open_quantity'] < trade['quantity'])
        if filteredRdd.isEmpty():
            return None

        count, p = filteredRdd. \
            map(lambda trade: (1, trade['price'])). \
            reduce(lambda count_p1, count_p2: (count_p1[0] + count_p2[0],
                                               count_p1[1] * count_p2[1]))

        # count is always > 0 because filteredRdd is not empty
        return p ** (1.0 / float(count))
