# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 10:19:05 2020

@author: Gamer
"""

def negate(f):
    return lambda *args, **kwargs: -f(*args, **kwargs)

def negate_all(f):
    return lambda *args, **kwargs: [-y for y in f(*args, **kwargs)]

def maximize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
    return minimize_batch(negate(target_fn), 
                          negate_all(gradient_fn), 
                          theta_0, 
                          tolerance)