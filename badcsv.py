# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 15:07:53 2020

@author: Gamer
"""

results = [["test1", "success", "Monday"],
           ["test2", "success, kind of", "Tuesday"],
           ["test3", "failure, kind of", "Wednesday"],
           ["test4", "failure, utter", "Thursday"]]

with open('bad_csv.txt', 'wb') as f:
    for row in results:
        f.write(",".join(map(str, row)))
        f.write("\n")
    


