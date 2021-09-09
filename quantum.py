# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 15:04:36 2019

@author: Gamer
"""
import numpy as np
m = 1

L = 1

hbar = 6.62607015e-34/np.pi
n = 3

for n in range (0, n+1):
    x = (hbar*n*np.pi/L)**2/(2*m)
    print(x)