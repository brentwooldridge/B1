# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 14:44:02 2020

@author: Gamer
"""

import csv

with open('datestock.txt', 'rb') as f:
    reader = csv.reader(f, delimeter='\t')
    for row in reader:
        date = row[0]
        symbol = row[1]
        closing_price = float(row[2])
        process(date, symbol, closing_price)
        
#process is arbitrary