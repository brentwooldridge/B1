# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:38:52 2019

@author: Gamer
"""

import scipy as sp
import numpy
from scipy.integrate import odeint
import matplotlib.pyplot as plt
def alpha(state,t):
# STATE VECTORS
  v = state[0]
  w = state[1]

# PARAMETERS
#  veq = 0.07
  beta = 0.8
  eps = 0.01
  gam = 5
  alpha=0.1
  Istim = 0.0
#ODES
  vdot = -v*(v-alpha)*(v-1)-w+Istim
  wdot = eps*(beta*v-w)

#SOLUTIONS
  return [vdot, wdot]
#INITIAL CONDITIONS
state0 = [0.2, 0.0]
#PERIOD
t = sp.arange(0.0, 100.0, 0.01)

state = odeint(alpha, state0, t)
#fig=plt.figure()
#ax=fig
plt.plot(t,state[:,0],t,state[:,1])
#plt.show()
#plt.plot(state[:,1])