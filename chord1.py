# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 23:58:11 2016

@author: Brent
"""
import matplotlib.pyplot as plt

import numpy as np

x1 = np.linspace(0, 0.05, 1000)
a = 2**(0.0/12)
b = 2.0**(4.0/12)
c = 2.0**(7.0/12)
d = 2.0**(12/12.0)


y1 = np.sin(2*np.pi*440*a*x1)

y2 = 0.5*np.sin((2*np.pi*440*b*x1))

y3 = np.sin(2*np.pi*440*c*x1)

y4 = np.sin(2*np.pi*440*d*x1)

y = y1+y2+y3+y4

plt.plot(x1, y)