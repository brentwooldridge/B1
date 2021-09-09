# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 19:42:26 2020

@author: Gamer
"""
import math
def estimated_parameters(N,n):
    p = n/N
    sigma = math.sqrt(p*(1-p)/N)
    return p, sigma


def a_b_test_statistic(N_A, n_A, N_B, n_B):
    p_A, sigma_A = estimated_parameters(N_A, n_A)
    p_B, sigma_B = estimated_parameters(N_B, n_B)
    return (p_B - p_A) / math.sqrt(sigma_A ** 2 + sigma_B ** 2)

z = a_b_test_statistic(1000, 200, 1000, 180)