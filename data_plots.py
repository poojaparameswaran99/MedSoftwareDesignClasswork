#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 12:51:16 2023

@author: poojap
"""

import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 10, 0.2)
y = np.sin(t)

plt.plot(t, y)
plt.show()

data = np.loadtxt("overall_data.dat", delimiter=",", dtype=int)
