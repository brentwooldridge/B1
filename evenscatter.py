# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 18:02:07 2020

@author: Gamer
"""

import matplotlib.pyplot as plt

test_1_grades = [99, 90, 85, 97, 80]
test_2_grades = [100, 85, 60, 90, 70]

plt.scatter(test_1_grades, test_2_grades)
plt.title("Axes Aren't Comparable")
plt.xlabel("test 1 grade")
plt.ylabel("test 2 grade")
plt.axis("equal")

plt.show()