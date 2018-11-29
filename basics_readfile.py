# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 10:17:41 2018

@author: Admin
"""

import matplotlib.pyplot as plt

def content_from_text(filepath):
    with open(filepath) as f:
        c = [float(line.strip().strip(',')) for line in f]
    return c

pop = content_from_text('data/world_population.txt')


f, ax = plt.subplots()
ax.plot(pop)
ax.set_ylabel('population')
plt.show()