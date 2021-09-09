# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 19:29:57 2019

@author: Gamer
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

x0 =0.5

xn = np.linspace(0, 1, 1000)
#y1 = xn
#y2 = xn*(1-xn)
#y3 = xn*(1+xn)
#y4 = 0.5*xn
#y5 = np.sin(xn)
y6 = -xn
plt.plot(xn, y6)
