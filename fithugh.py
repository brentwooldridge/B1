import scipy as sp
import numpy
from scipy.integrate import odeint
import matplotlib.pyplot as plt
def fitz(state,t):
  # unpack the state vector
  v = state[0]
  w = state[1]

  # these are our constants
#  veq = 0.07
  beta = 0.8
  eps = 0.01
  gam = 5
  alpha=0.1
  Istim = 0.0
  # compute state derivatives
  vdot = -v*(v-alpha)*(v-1)-w+Istim
  wdot = eps*(beta*v-w)

  # return the state derivatives
  return [vdot, wdot]

state0 = [0.2, 0.0]
t = sp.arange(0.0, 100.0, 0.01)

state = odeint(fitz, state0, t)
#fig=plt.figure()
#ax=fig
plt.plot(t,state[:,0],t,state[:,1])
#plt.show()
#plt.plot(state[:,1])