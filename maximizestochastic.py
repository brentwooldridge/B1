# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 10:37:34 2020

@author: Gamer
"""

def maximize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha=0.01):
    return minimize_stochastic(negate(target_fn),
                               negate_all(gradient_fn),
                               x, y, theta_0, alpha_0)