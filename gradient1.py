# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 20:39:47 2020

@author: Gamer
"""
import random
import math

def dot(v, w):
    return sum(v_i * w_i
               for v_i, w_i in zip(v, w))
def sum_of_squares(v):
    return dot(v, v)

def vector_subtract(v, w):
    return[v_i - w_i 
           for v_i, w_i in zip(v, w)]

def squared_distance(v, w):
    return sum_of_squares(vector_subtract(v,w))

def magnitude(v):
    return math.sqrt(squared_distance(v))

def distance(v, w):
    return math.sqrt(squared_distance(v, w))

def step(v, direction, step_size):
    return[v_i + step_size * direction_i
           for v_i, direction_i in zip(v, direction)]

def sum_of_squares_gradient(v):
    return[2 * v_i for v_i in v]

v = [random.randint(-10,10) for i in range(3)]

tolerance = 0.0000000001

while True:
    gradient = sum_of_squares_gradient(v)
    next_v = step(v, gradient, -0.01)
    if distance(next_v, v) < tolerance:
        break
    v = next_v
    

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
