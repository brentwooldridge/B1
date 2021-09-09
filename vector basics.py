# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 18:05:23 2020

@author: Gamer
"""

height_weight_age = [70, #inches,
                     170, #pounds
                     40] #years

grades = [95, #exam1
          80, #exam2
          75, #exam3
          65] #exam4

def vector_add(v,w):
        return[v_i + w_i for v_i, w_i in zip(v,w)
        
    ]if len(v)==len(w) else "Uneven lengths"
    
y = vector_add(height_weight_age, grades)

print y
