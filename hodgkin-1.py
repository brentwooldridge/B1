# -*- coding: utf-8 -*-
"""
Created on Tue Dec 08 09:29:32 2015

@author: Brent
"""

import numpy as np
import scipy as sp
from scipy.integrate import odeint
import matplotlib.pyplot as plt
def HH(voltage, t):
# Vectors holding voltage and gating variable values
    V = voltage[0]
    n = voltage[1]
    m = voltage[2]
    h = voltage[3]    
# Reversal potential    
    Ena = 120
    Ek  = -12.0
    El  = 10.6
    
    
    Cm  = 1.0
#Conductance
    gna = 120.0
    gk  = 36.0
    gl  = 0.3
# Input Current/Stimulus
    Istim = 0.0    
# Parameters
    alphan = 0.01*(10.0-V)/(np.exp((10.0-V)/10.0)-1.0)
    alpham = 0.1*(25.0-V)/(np.exp((25.0-V)/10.0)-1.0)
    alphah = 0.07*np.exp(-V/20.0)
    betan  = 0.125*np.exp(-V/80.0)    
    betam  = 4.0*np.exp(-V/18.0)
    betah  = 1.0/(np.exp((30.0-V)/10)+1)
    
    
    V_dot = (-1.0/Cm)*(gk*n**4*(V-Ek)+gna*m**3*(V-Ena)+gl*(V-El)-Istim)
    
    n_dot = alphan*(1-n)-betan*n
    
    m_dot = alpham*(1-m)-betam*m
    
    h_dot = alphah*(1-h)-betah*h
    
    
    return[V_dot, n_dot, m_dot, h_dot]    
    
t = np.linspace(0, 1000, 100)

initial = [0.0, 0.0, 0.0, 0.0]

hodgehuxley = odeint(HH, initial, t)

V = [i[0] for i in hodgehuxley]
n = [i[1] for i in hodgehuxley]
m = [i[2] for i in hodgehuxley]
h = [i[3] for i in hodgehuxley]

plt.plot(V, n)