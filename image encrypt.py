# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 18:03:56 2021

@author: Teacher
"""
import keygen as kg
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
#% matplotlib inline

image = Image.open("3dlorenz.png")

#image.show()
#plt.imshow(image)
print(image.size)
print(image.format)
print(image.mode)

image.save("3dlorenz1.png")

