# -*- coding: utf-8 -*-
"""
Created on Thu Dec 03 19:14:06 2015

@author: Brent
"""
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import scipy as sp
import matplotlib.pyplot as plt
from scipy.integrate import odeint
outfile = "outputFile.txt"
#Parameters

alpha = 0.375
mu    = 0.81

#Shimizu-Morioka System

def shim(state, t):

    x = state[0] 
    y = state[1]
    z = state[2]

    x_dot = y

    y_dot = x-mu*y-x*z

    z_dot = -alpha*z + x**2
    
    return [x_dot, y_dot, z_dot]
    
state = [.1, 0, 0]

t = np.linspace(0, 250, 100000)

fhn_sol = odeint(shim, state, t)

x = [i[0] for i in fhn_sol]
y = [i[1] for i in fhn_sol]
z = [i[2] for i in fhn_sol]
#with open(outfile) as f1:
#    for x in fhn_sol:
#        f1.write

#plt.plot(t,x,t,y,t,z)
#plt.plot(x,z)
#fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot(x, y, z, '-b')
plt.show()
#plt.plot(t,x,t,y,t,z)
#plt.show()