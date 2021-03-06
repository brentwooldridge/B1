# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:45:26 2020

@author: Gamer
"""
import matplotlib.pyplot as plt

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

xs = [i + 0.1 for i, _ in enumerate(movies)]

plt.bar(xs, num_oscars)

plt.ylabel("# of Academy Awards")
plt.title("My Favorite Movies")    

plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)

plt.show()