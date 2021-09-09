# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 21:06:05 2020

@author: Gamer
"""

step_sizes = [100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001]


def safe(f):
    def safe_f(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            return float('inf')
        return safe_f
    
def minimize_batch(target_fn, gradient_fn, theta_0, tolerance = 0.000001):
    step_sizes = [100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001]
    theta = theta_0
    target_fn = safe(target_fn)
    value = target_fn(theta)
    while True:
        gradient = gradent_fn(theta)
        next_thetas = [step(theta, gradient, -step_size)
                       for step_size in step_sizes]
        
        next_theta = min(next_thetas, key = target_fn)
        next_value = target_fn(next_theta)
        
        if abs(value - next_value) < tolerance:
            return theta
        else:
            theta, value = next_theta, next_value