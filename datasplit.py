# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 13:05:47 2020

@author: Gamer
"""
import random


def split_data(data, prob):
    results = [], []
    for row in data:
        results[0 if random.random() < prob else 1].append(row)
    return results