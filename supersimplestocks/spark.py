#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Super Simple Stocks
# https://github.com/tgorka/SuperSimpleStocks
#
# Copyright (C) 2016 Tomasz Gorka <http://tomasz.gorka.org.pl>
#
from pyspark import SparkContext, SparkConf

# initialize spark
conf = SparkConf().setAppName('supersimplestocs')
spark_context = SparkContext('local[2]', conf=conf)


def compatible_trades(trade_offer, trades):
    '''
    Get compatible trades (according to price, oposite type,
    have open quantities.
    :param trade_offer: to get copmatible trades
    :param trades: to filter
    :return: list of compatible trades
    '''
    try_type = 'SELL' if trade_offer['type'] == 'BUY' else 'BUY'
    return spark_context.parallelize(trades). \
        filter(lambda offer: offer['type'] == try_type and
                             offer['price'] == trade_offer['price'] and
                             offer['open_quantity'] > 0). \
        collect()


def stock_price(symbol, begin_datetime, trades):
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

    price, quantity = spark_context.parallelize(trades). \
        filter(lambda trade: trade['symbol'] == symbol and
                             trade['datetime'] >= begin_datetime and
                             trade['open_quantity'] < trade['quantity']). \
        map(mapFun). \
        reduce(lambda price_quantity1, price_quantity2:
                (price_quantity1[0] + price_quantity2[0],
                 price_quantity1[1] + price_quantity2[1]))

    return price / float(quantity)


def last_dividend(symbol, dividents):
    '''
    Get last dividend from the list based on given symbol.
    :param symbol: symbol of stock
    :param dividents: to analyze
    :return: last dividend from the list or throw a ValueError if not exists
    '''
    return spark_context.parallelize(dividents). \
        filter(lambda divident: divident['symbol'] == symbol). \
        first()


def gbce(begin_datetime, trades):
    count, p = spark_context.parallelize(trades). \
        filter(lambda trade: trade['datetime'] >= begin_datetime and
                             trade['open_quantity'] < trade['quantity']). \
        map(lambda trade: (1, trade['price'])). \
        reduce(lambda count_p1, count_p2: (count_p1[0] + count_p2[0],
                                           count_p1[1] * count_p2[1]))

    return p ** (1.0 / float(count))
