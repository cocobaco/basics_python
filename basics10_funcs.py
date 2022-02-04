# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 11:35:34 2018

@author: Admin
"""
import numpy as np
import matplotlib.pyplot as plt


r = np.linspace(0, 10, num=50, endpoint=True)

# 1. use function: func(data)
def area(r):
    return np.pi * (r ** 2)

a = area(r)

fig, ax = plt.subplots()
ax.plot(r, a, lw=5)
ax.set_xlabel('r')
ax.set_ylabel('area')
plt.show()


def deltafun(x):
    if x==0:
        return 1
    else:
        return 0

for k in range(-3, 3):
    print(k, " ", deltafun(k))
    
x = np.arange(-10, 10)
y = np.array(list(map(deltafun, x)))

fig, ax = plt.subplots()
ax.plot(x, y, lw=3)
ax.set_xlabel('x')
ax.set_ylabel('area')
ax.set_title('delta function')
plt.show()


# 2. use map: map(func, data)
c_to_f = lambda c: (9/5) * c + 32
temp = np.linspace(-10, 120, num=50)
a2 = list(map(c_to_f, temp))

fig, ax = plt.subplots()
ax.plot(temp, a2, lw=5)
ax.set_xlabel('C')
ax.set_ylabel('F')

plt.show()


# 3. filter. like map, with conditional statement
dat = [20, 24, 29, 12, 39, 16, 32, 15]
print(dat)
avg = np.mean(dat)
print('avg = {}'.format(avg))
print(list(filter(lambda x: x > avg, dat)))

dat2 = ['', 'adrian', 'bobby', '', 'camden', 'dorothy']
print(dat2)
# use filter to remove missing data
print(list(filter(None, dat2)))
