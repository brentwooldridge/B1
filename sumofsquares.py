# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 20:11:11 2020

@author: Gamer
"""
v = [1, 2]


def sum_of_squares(v):
    return sum(v_i ** 2 for v_i in v)

y = sum_of_squares(v)

print y