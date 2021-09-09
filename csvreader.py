# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 14:53:17 2020

@author: Gamer
"""


import csv

with open('file.txt', 'rb') as f:
    reader = csv.DictReader(f, delimeter=':')
    for row in reader:
        date = row["date"]
        symbol = row["symbol"]
        closing_price = float(row["closing_price"])
        process(date, symbol. closing_price)