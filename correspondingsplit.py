# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 13:08:29 2020

@author: Gamer
"""



import random


def split_data(data, prob):
    results = [], []
    for row in data:
        results[0 if random.random() < prob else 1].append(row)
    return results

def train_test_split(x, y, test_pct):
    data = zip(x, y)
    train, test = split_data(data, 1- test_pct)
    x_train, y_train = zip(*train)
    x_test, y_test = zip(*test)
    return x-train, x_test, y_train, y_test

model = SomeKindOfModel()
x_train, x_test, y_train, y_test = train_test_split(xs, ys, 0.33)
model.train(x_train, y_train)
performance = model.test(x_test, y_test)