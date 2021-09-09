# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 15:05:16 2019

@author: Gamer
"""

import matplotlib.pyplot as plt
import numpy as np

X0 = np.linspace(-1.5, 1.5)
X1 = np.linspace(-12, 6, 100)
X2 = np.linspace(-12, 6, 100)
Y = [0 for x in X0]

X3 =  np.sqrt(9-((X1-1.5)**2))
X4 = -np.sqrt(9-((X1-1.5)**2))
X5 =  np.sqrt(9-((X1+1.5)**2))
X6 = -np.sqrt(9-((X1+1.5)**2))




plt.plot(X1, X3)
plt.plot(X1, X4)
plt.plot(X1, X5)
plt.plot(X1, X6)
plt.plot(X0, Y)
plt.xlim(-7, 7)
plt.ylim(-5, 5)
plt.show()