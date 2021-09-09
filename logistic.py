# -*- coding: utf-8 -*-
"""
Created on Sat Jan 09 15:14:03 2016

@author: Brent
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

r = 2 
while r <=4:

    xn = np.linspace(0, 1, 1000)
#    xnn = np.linspace(0.5, 1, 1000)
    xn1 = r*xn*(1-xn)
#    xn2 = r*(1-xnn)

    plt.plot(xn, xn1)
    
    r = r+0.5
    
        
y = xn

plt.plot(xn, y)

