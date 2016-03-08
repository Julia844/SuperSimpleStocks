#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Super Simple Stocks
# https://github.com/tgorka/SuperSimpleStocks
#
# Copyright (C) 2016 Tomasz Gorka <http://tomasz.gorka.org.pl>
#
__all__ = ['csv_path', 'begin_date', 'trades', 'dividends']

import datetime
import os

def csv_path():
    # geting path to the csv file
    csv_path = os.path.abspath(__file__)
    csv_path = os.path.dirname(csv_path)
    csv_path = os.path.join(csv_path, '../example/data.csv')
    csv_path = os.path.abspath(csv_path)

    return csv_path


# timedelta for calculating trades: 15min
now = datetime.datetime.now()
trandes_delta = datetime.timedelta(minutes=15)
begin_date = now - trandes_delta
# information kept. Store it in the DB.
trades = [
    {
        'id': '4166a4db-e02d-4525-b440-c06882d96699',
        'datetime': now,
        'symbol': 'STS',
        'type': 'SELL',
        'quantity': 1000,
        'price': 0.274625,
        'open_quantity': 850,
        'registered': [
            ('ad1a890d-74c8-47a1-9592-d7f941eb4b0d', 100),
            ('13c212f7-6bae-4280-abd5-bf836fdaf4f4', 50)
        ]
    }, {
        'id': 'ad1a890d-74c8-47a1-9592-d7f941eb4b0d',
        'datetime': now,
        'symbol': 'STS',
        'type': 'BUY',
        'quantity': 100,
        'price': 0.274625,
        'open_quantity': 0,
        'registered': [
            ('4166a4db-e02d-4525-b440-c06882d96699', 100)
        ]
    }, {
        'id': '13c212f7-6bae-4280-abd5-bf836fdaf4f4',
        'datetime': now,
        'symbol': 'STS',
        'type': 'BUY',
        'quantity': 50,
        'price': 0.274625,
        'open_quantity': 0,
        'registered': [
            ('4166a4db-e02d-4525-b440-c06882d96699', 50)
        ]
    }, {
        'id': 'f9056a7b-b341-4a99-a7a1-698391e2c7e2',
        'datetime': now,
        'symbol': 'STS1',
        'type': 'BUY',
        'quantity': 70,
        'price': 0.5,
        'open_quantity': 0,
        'registered': [
            ('e2cc8f0e-c8d0-467a-b427-f083b69c208b', 70)
        ]
    }, {
        'id': '1a091eac-79d9-47d5-86eb-acc24ae4ef3a',
        'datetime': now,
        'symbol': 'STS1',
        'type': 'BUY',
        'quantity': 30,
        'price': 1,
        'open_quantity': 0,
        'registered': [
            ('5b4ad999-c429-4dde-aa17-6ec65ad1afef', 30)
        ]
    }, {
        'id': '5b4ad999-c429-4dde-aa17-6ec65ad1afef',
        'datetime': now,
        'symbol': 'STS1',
        'type': 'SELL',
        'quantity': 30,
        'price': 1,
        'open_quantity': 0,
        'registered': [
            ('1a091eac-79d9-47d5-86eb-acc24ae4ef3a', 30)
        ]
    }, {
        'id': 'e2cc8f0e-c8d0-467a-b427-f083b69c208b',
        'datetime': now,
        'symbol': 'STS1',
        'type': 'SELL',
        'quantity': 70,
        'price': 0.5,
        'open_quantity': 0,
        'registered': [
            ('f9056a7b-b341-4a99-a7a1-698391e2c7e2', 70)
        ]
    }
]
dividends = []