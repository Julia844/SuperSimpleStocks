#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Super Simple Stocks
# https://github.com/tgorka/SuperSimpleStocks
#
# Copyright (C) 2016 Tomasz Gorka <http://tomasz.gorka.org.pl>
#
__all__ = ['load_dividend_data']

# for loading by celery system
from supersimplestocks.tasks import celery_app

import csv
from supersimplestocks import tasks


def load_dividend_data(csv_path):
    '''
    Load dividend data from csv file and registed each value to the celery task.
    :param csv_path: path to the file
    '''
    with open(csv_path, 'r') as csvfile:
        for index,stock in enumerate(csv.reader(csvfile, delimiter=';')):
            if index > 0:
                stock_data = {
                    'symbol': stock[0],
                    'type': stock[1],
                    'last': float(stock[2]),
                    'fixed': None,
                    'value': int(stock[4])
                }
                # if it's like 2% or 0.02
                if stock[3].endswith('%'):
                    stock_data['fixed'] = float(stock[3][:-1]) / 100.0
                elif len(stock[3]) > 0:
                    stock_data['fixed'] = float(stock[3])

                tasks.record_dividend_data.delay(**stock_data)


# for loading by celery system
if __name__ == '__main__':
    celery_app.start()