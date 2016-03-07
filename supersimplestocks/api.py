#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Super Simple Stocks
# https://github.com/tgorka/SuperSimpleStocks
#
# Copyright (C) 2016 Tomasz Gorka <http://tomasz.gorka.org.pl>
#
import os
import csv
from supersimplestocks import tasks


def load_dividend_data(csv_path):
    '''
    Load dividend data from csv file and registed each value to the celery task.
    :param csv_path: path to the file
    '''
    with open(os.path.abspath(csv_path), 'r') as csvfile:
        for index,stock in enumerate(csv.reader(csvfile, delimiter=';')):
            if index > 0:
                record_dividend_data(*stock[:5])


def record_dividend_data(symbol, type, last, fixed, value):
    '''
    Record new dividend
    :param symbol: of the stock
    :param type: Common, Preferred
    :param last: dividend value
    :param fixed: percentage value in format 0.01
    :param value: par value
    '''
    # if it's like 2% or 0.02
    if fixed is not None and fixed.endswith('%'):
        fixed = float(fixed[:-1]) / 100.0
    elif fixed is not None and len(fixed) > 0:
        fixed = float(fixed)
    else:
        fixed = None

    tasks.record_dividend_data.delay(
            symbol, type, float(last), fixed, int(value))


def record_trade(symbol, type, quantity, price):
    '''
    Record a new trade in the stock.
    Check the trades and try fo finalize the trade.
    If not possible to finalize for all quantities
    the rest will wait in the queue.
    :param symbol: of the stock
    :param type: SELL, BUY
    :param quantity: to trade
    :param price: of the trade
    '''
    tasks.record_trade.delay(symbol, type, int(quantity), float(price))


def stock_price(symbol):
    '''
    Calculate stock price for given stock based on trades from last 15 min.
    :param symbol: of the stock
    :return: value
    '''
    return tasks.stock_price.delay(symbol).get(timeout=300)


def dividend_yield(symbol):
    '''
    Calculate dividend yield for given stock.
    The initial data about the dividends are static taken from csv file.
    :param symbol: of the stock
    :return: value or throw a ValueError if symbol not registered
            in last dividents.
    '''
    return tasks.dividend_yield.delay(symbol).get(timeout=300)


def p_e_ratio(symbol):
    '''
    Calculate P/E Ratio for given stock.
    The initial data about the dividends are static taken from csv file.
    :param symbol: of the stock
    :return: value
    '''
    return tasks.p_e_ratio.delay(symbol).get(timeout=300)


def gbce():
    '''
    Calculate the GBCE All Share Index using the geometric mean of prices
    for all stocks.
    :return: value
    '''
    return tasks.gbce.delay().get(timeout=300)

