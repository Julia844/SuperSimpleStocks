#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Super Simple Stocks
# https://github.com/tgorka/SuperSimpleStocks
#
# Copyright (C) 2016 Tomasz Gorka <http://tomasz.gorka.org.pl>
#
__all__ = ['load_dividend_data', 'record_dividend_data', 'record_trade',
           'stock_price', 'dividend_yield', 'p_e_ratio', 'gbce']

from supersimplestocks.api import *

# for loading by celery system
from supersimplestocks.tasks import celery_app


# for loading by celery system
if __name__ == '__main__':
    celery_app.start()