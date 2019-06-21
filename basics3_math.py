# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 13:32:33 2018

@author: roppon
"""
import math
import matplotlib.pyplot as plt
import numpy as np


print('*'*40)
num1 = 2.5635
# Absolute value.
print(num1)
print('floor: ', math.floor(num1))
print('ceil: ', math.ceil(num1))
print('round: ', round(num1, 2))

x = np.arange(1, 10, 0.01)
y1 = [math.cos(n) for n in x]
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