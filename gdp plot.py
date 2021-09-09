# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:38:10 2020

@author: Gamer
"""

import matplotlib.pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]


plt.plot(years, gdp, color = 'blue', marker ='o', linestyle = 'solid')

plt.title("Nominal GDP")

plt.ylabel("Billions of $")
plt.show()