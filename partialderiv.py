# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 20:34:38 2020

@author: Gamer
"""



def partial_difference_quotient(f, v, i, h):
    w = [v_j + (h if j == i else 0)
         for j, v_j in enumerate(v)]
    return (f(w) - f(v) / h)

def estimate_gradient(f, v, h=0.00001):
    return[partial_difference_quotient(f, v, i, h)
           for i, _ in enumerate(v)]