# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 07:47:48 2019

@author: roppon
"""

import csv
import pandas as pd
import matplotlib.pyplot as plt


fin = 'data/sales-of-shampoo-3y.csv'


print('using csv reader:')
with open(fin) as myfile:
    csv_reader = csv.reader(myfile, delimiter=',')
    line_count = 0
    for row in csv_reader:
        line_count += 1
        # print(row)
                
print(f'there are {line_count} lines.')


print('using csv reader:')
with open(fin) as myfile:
    csv_reader = csv.DictReader(myfile)
    line_count = 0
    for row in csv_reader:
        line_count += 1
        print(row)
                

print('using pandas read_csv:')
df = pd.read_csv(fin)
df.columns = ['month', 'sales']
print(df.head())
print(df.shape)

df = df.reset_index()
f, ax = plt.subplots()
df.plot(kind='scatter', x='index', y='sales', ax=ax)
ax.set_xticklabels(df['month'])

plt.show()