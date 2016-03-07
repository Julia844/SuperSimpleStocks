#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Super Simple Stocks
# https://github.com/tgorka/SuperSimpleStocks
#
# Copyright (C) 2016 Tomasz Gorka <http://tomasz.gorka.org.pl>
#
from __future__ import absolute_import

import datetime
import uuid
from celery import Celery
from supersimplestocks import spark

# Initialize celery connection with RabbitMQ
celery_app = Celery('supersimplestocs',
        broker='amqp://guest@localhost//',
        backend='amqp://guest@localhost//')

# Optional configuration, see the application user guide.
celery_app.conf.update(
        CELERY_TASK_RESULT_EXPIRES=3600,
)

# information kept. Store it in the DB.
trades = []
dividends = []

# timedelta for calculating trades: 15min
trandes_delta = datetime.timedelta(minutes=15)


@celery_app.task
def record_dividend_data(symbol, type, last, fixed, value):
    '''
    Record new dividend
    :param symbol: of the stock
    :param type: Common, Preferred
    :param last: dividend value
    :param fixed: percentage value in format 0.01
    :param value: par value
    '''
    dividends.append({
        'symbol': symbol,
        'type': type,
        'last': last,
        'fixed': fixed,
        'value': value
    })


@celery_app.task
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
    now = datetime.datetime.now()
    trade = {
        'id': str(uuid.uuid4()),
        'datetime': now,
        'symbol': symbol,
        'type': type,
        'quantity': quantity,
        'price': price,
        'open_quantity': quantity,
        'registered': []
    }
    # register in the queue
    trades.append(trade)
    # get compatible trades
    compatible_trades = spark.compatible_trades(trade, trades)
    # make the trade to fill the needs
    index = 0
    while index < len(compatible_trades) and trade['open_quantity'] > 0:
        compatible_trade = compatible_trades[index]
        trade_quantity = min(trade['open_quantity'],
                compatible_trade['open_quantity'])

        trade['registered'].append((compatible_trade['id'], trade_quantity))
        compatible_trade['registered'].append((trade['id'], trade_quantity))
        trade['open_quantity'] -= trade_quantity
        compatible_trade['open_quantity'] -= trade_quantity

        index += 1


@celery_app.task
def stock_price(symbol):
    '''
    Calculate stock price for given stock based on trades from last 15 min.
    :param symbol: of the stock
    :return: value
    '''
    now = datetime.datetime.now()
    return spark.stock_price(symbol, now - trandes_delta, trades)


@celery_app.task
def dividend_yield(symbol, price=None):
    '''
    Calculate dividend yield for given stock.
    The initial data about the dividends are static taken from csv file.
    :param symbol: of the stock
    :param price: OPTIONAL stock price for the dividend calculation.
            By default calculate stock price based on the task.
    :return: value or throw a ValueError if symbol not registered
            in last dividents.
    '''
    last_dividend = spark.last_dividend(symbol, dividends)
    s_price = price if price is not None else stock_price(symbol)
    if (last_dividend['type'] == 'Preferred'):
        return last_dividend['fixed'] * float(last_dividend['value']) / s_price
    else:
        return float(last_dividend['last']) / s_price


@celery_app.task
def p_e_ratio(symbol):
    '''
    Calculate P/E Ratio for given stock.
    The initial data about the dividends are static taken from csv file.
    :param symbol: of the stock
    :return: value
    '''
    s_price = stock_price(symbol)
    return s_price / dividend_yield(symbol, price=s_price)


@celery_app.task
def gbce():
    '''
    Calculate the GBCE All Share Index using the geometric mean of prices
    for all stocks.
    :return: value
    '''
    now = datetime.datetime.now()
    return spark.gbce(now - trandes_delta, trades)