# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 19:52:30 2020

@author: Gamer
"""
import math
def B(alpha, beta):
    return math.gamma(alpha) * math.gamma(beta / math.gamma(alpha + beta))


def beta_pdf(x, alpha, beta):
    if x < 0 or x > 1:
        return 0
    return x ** (alpha -1) * (1-x) ** (beta - 1)/B(alpha, beta)