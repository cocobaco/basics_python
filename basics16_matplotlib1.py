# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 13:11:22 2020

@author: PC1
"""
import matplotlib.pyplot as plt
import numpy as np


x = np.arange(1, 10, 0.1)
y1 = np.cos(x)
y2 = np.log(x)

# stateful way
plt.figure()
plt.plot(x, y1, 'o', label='cos')
plt.plot(x, y2, 'x', label='log')
plt.title('This is a plot (plt)')
plt.legend()


# object oriented way
f = plt.figure()
ax = plt.subplot(111)
ax.plot(x, y1, 'o', label='cos')
ax.plot(x, y2, 'x', label='log')
ax.set_title('This is a plot (ax)')
ax.legend()

plt.show()