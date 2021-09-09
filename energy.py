# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:29:29 2019

@author: Gamer
"""
import numpy as np

k = 1
x = np.linspace(0, 6, 0.01)
def energy(x):
    return np.exp(k*x)+ np.exp(-k*x)


y = energy(x)
print(y)
