# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 14:58:55 2020

@author: Gamer
"""

import csv

today_prices = {'AAPL' : 90.91, 'MSFT' : 41.68, 'FB' : 64.5}

with open('datestock.txt', 'wb') as f:
    writer = csv.writer(f, delimiter = ',')
    for stock, price in today_prices.items():
        writer.writerow([stock, price])