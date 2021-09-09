# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 18:55:11 2020

@author: Gamer
"""
import matplotlib.pyplot as plt
import collections
num_friends = [100, 49, 41, 40, 25]
friend_counts = Counter(num_friends)
xs = range(101)
ys = [friend_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()