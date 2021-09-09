# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 20:15:24 2020

@author: Gamer
"""
import matplotlib.pyplot as plt
from functools import partial


def square(x):
    return x ** 2

def derivative(x):
    return 2 * x


def difference_quotient(f, x, h):
    return (f(x+h) - f(x)) / h

derivative_estimate = partial(difference_quotient, square, h = 0.00001)

x = range(-10, 10)
plt.title("Actual Derivatives vs. Estimates")
plt.plot(x, map(derivative, x), 'rx', label = 'Actual')
plt.plot(x, map(derivative_estimate, x), 'b+', label = 'Estimate')
plt.legend(loc = 9)
plt.show()
