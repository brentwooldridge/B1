# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 01:46:36 2019

@author: Gamer
"""


import numpy as np
import scipy as sp
from scipy.integrate import odeint
import matplotlib.pyplot as plt
def EZ(enzyme, t):
# Vectors holding voltage and gating variable values
    s = enzyme[0]
    e = enzyme[1]
    c = enzyme[2]
    p = enzyme[3]    
# Reversal potential    
    kminus1 = 100
    k1  = 0.5
    k2  = 0.001
    Vmax = k2*initial[1]
    K1 = k1/kminus1
    sdot = kminus1*c - k1*s*e
    edot = (kminus1+k2)*c - k1*s*e
    cdot = k1*s*e -(k2 + kminus1)*c
#    pdot = Vmax*s/(K1+s)
    pdot = k2*c
    
    

    
    return[sdot, edot, cdot, pdot]    
    
t = np.linspace(0, 2000, 100000)

initial = [1.0, 1.0, 0.0, 0.0]

kinetics = odeint(EZ, initial, t)

s = [i[0] for i in kinetics]
e = [i[1] for i in kinetics]
c = [i[2] for i in kinetics]
p = [i[3] for i in kinetics]

plt.plot(t, p, t, c, t, s, t, e)