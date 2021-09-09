import matplotlib.pyplot as plt
import numpy as np
from numpy import *
from scipy.integrate import odeint
import scipy
e = input('Istim=')

if e == 1:
    def lorenz_int(initial, t):  
        x = initial[0]
        y = initial[1]
    
        eps = 0.008
        alpha = 0.139
        beta = 8.0/3
        gam = 2.54
        Istim = e
        x_dot = x*(x-alpha)*(1-x)-y+Istim
        y_dot = eps*(x-gam*y)
    
        return [x_dot, y_dot]
elif (e == 1):
    def lorenz_int(initial, t):  
        x = initial[0]
        y = initial[1]
    
        eps = 0.008
        alpha = 0.139
        beta = 8.0/3
        gam = 2.54
        Istim = e
        x_dot = x*(x-alpha)*(1-x)-y+Istim
        y_dot = eps*(x-gam*y)
    
        return [x_dot, y_dot]
#initial conditions.
initial = [0.2, 0.0]
t = scipy.arange(0, 200, 0.01)
lorenz_sol = odeint(lorenz_int, initial, t)
x = [i[0] for i in lorenz_sol]
y = [i[1] for i in lorenz_sol]

DataOut = column_stack((x,y))
#savetxt(’out.dat’, DataOut)
plt.plot(t,x,t,y)