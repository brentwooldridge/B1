# -*- coding: utf-8 -*-
"""
Created on Tue Dec 08 12:47:32 2015

@author: Brent
"""

import numpy as np
import scipy as sp
from scipy.integrate import odeint
import matplotlib.pyplot as plt

It = np.pi

def thetan(theta, t):
    
    V = theta[0]
    
    
    V_dot = 1-np.cos(V)+(1+np.cos(V))*It

    return [V_dot]
    
t = np.linspace(0, 2*np.pi, 100)
initial = [0]
theneu = odeint(thetan, initial, t)

V = [i[0] for i in theneu]
plt.plot(t, V)