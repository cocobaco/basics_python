# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 07:47:48 2019

@author: roppon
"""

import csv


fin = 'data/sales-of-shampoo-3y.csv'

with open(fin) as myfile:
    csv_reader = csv.reader(myfile, delimiter=',')
    line_count = 0
    for row in csv_reader:
        line_count += 1
        
        
print(f'there are {line_count} lines.')


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(fin)
df.columns = ['month', 'sales']
print(df)


df = df.reset_index()
f, ax = plt.subplots()
df.plot(kind='scatter', x='index', y='sales', ax=ax)
ax.set_xticklabels(df['month'])

plt.show()