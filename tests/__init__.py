#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Super Simple Stocks
# https://github.com/tgorka/SuperSimpleStocks
#
# Copyright (C) 2016 Tomasz Gorka <http://tomasz.gorka.org.pl>
#
__all__ = ['csv_path']

import os

def csv_path():
    # geting path to the csv file
    csv_path = os.path.abspath(__file__)
    csv_path = os.path.dirname(csv_path)
    csv_path = os.path.join(csv_path, '../example/data.csv')
    csv_path = os.path.abspath(csv_path)

    return csv_path