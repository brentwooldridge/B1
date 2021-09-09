# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 14:17:14 2020

@author: Gamer
"""

import matplotlib.pyplot as plt



cities = [([-122.3, 47.53], "Python"),
          ([-96.85, 32.85], "Java"),
          ([-89.33, 43.13], "R"),
          ]

plots = {"Java" : ([], []), "Python" : ([], []), "R" : ([],[])}

markers = {"Java" : "o", "Python" : "s", "R" : "^"}
colors  = {"Java" : "r", "Python" : "b", "R" : "g"}

for (longitude, latitude), language in cities:
    plots[language][0].append(longitude)
    plots[language][1].append(latitude)

for language, (x, y) in plots.iteritems():
    plt.scatter(x, y, color=colors[language], marker = markers[language],
                label=language, zorder=10)
#plot state borders as exercise
#plot_state_borders(plt)

plt.legend(loc=0)
plt.xis([-130, -60, 20, 55])

plt.title("Favorite Programming Languages")
plt.show()