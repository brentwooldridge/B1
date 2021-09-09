# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 13:23:31 2020

@author: Gamer
"""



def accuracy(tp, fp, fn, tn):
    correct = tp + tn
    total = tp + fp + fn + tn
    return correct / total
print accuracy(70.0, 4930, 13930, 981070)

def precision(tp, fp, fn, tn):
    return tp / (tp + fp)
print precision(70.0, 4930, 13930, 981070)

def recall(tp, fp, fn, tn):
    return tp / (tp + fn)
print recall(70.0, 4930, 13930, 981070)

def f1_score(tp, fp, fn, tn):
    p = precision(tp, fp, fn, tn)
    r = recall(tp, fp, fn, tn)
    
    return 2. * p * r / (p + r)