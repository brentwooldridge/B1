# -*- coding: utf-8 -*-
"""
Created on Mon May  3 20:21:39 2021

@author: Gamer
"""

import numpy as np
import matplotlib.pyplot as plt

r = np.linspace(2.4, 4, 10000)
xn = 0

while xn<1:

    xn1 = r * xn*(1-xn)
xn = xn + .0001
plt.plot(r, xn1)