# -*- coding: utf-8 -*-
"""
Created on Sat Jul 09 20:58:05 2016

@author: Brent
"""
	


import numpy as np
import pylab as pl

with open("fort.11") as f:
    data = f.read()

data = data.split('\n')

pl.plot(data[:,0], data[:,1], ’ro’)
pl.xlabel(’x’)
pl.ylabel(’y’)
pl.xlim(0.0, 10.)
pl.show()


state =[ -0.824202E+02,
       0.1150018250460492E-00,
       0.12995E+04,
        0.112684E+02,
       0.125290E+03,
       0.12995E+04,
      0.115001E+00,
       0.930308E-18,
       0.9938760E+00,
      0.124216E-3,
      0.578679E-8,
      0.119816E-12,
     0.497923E-18,
      0.345847E-13,
     0.185106E-13,
       0.999871E+00,
     0.1677403E-03,
      0.149102E-04,
      0.951726E-10,
      0.624646E+00,
       0.20752E-01,
       0.279132E-03,
       0.142371E+06,
       0.14372015E+07,
       0.265563E-02,
       0.999977E+00,
      0.262753E-03,
      0.417069E-03,
       0.998543E+00,
      0.998159E+00,
      0.992513E-03,
       0.641229E-03,
      0.175298E-03,
      0.319129E-04,
       0.417069E-03,
       1.0E+00,
       0.713483E-06,
        0.153176E-03,
     0.673345E-06,
       0.157787E-08,
        0.113879E-01,
      0.342780E+00,
       0.417069E-03,
       0.0,
       0.998543E+00]