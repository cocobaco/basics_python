# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 10:17:41 2018

@author: Admin
"""

import matplotlib.pyplot as plt
from collections import Counter
import random

# -------- numbers from file --------------
def num_from_file(filepath):
    with open(filepath) as f:
        c = [float(line.replace(',','').strip()) for line in f]
    return c

dat = num_from_file('data/world_population.txt')


f, ax = plt.subplots()
ax.plot(dat)
ax.set_ylabel('population')
plt.show()


# ----------lines of text from file --------
def text_from_file(filepath):
    with open(filepath, encoding='utf-8') as f:
        c = [line.strip() for line in f]
    return c


fname = 'data/myst_affair_styles.txt'
dat2 = text_from_file(fname)

print(f'{len(dat2)} lines found in {fname}')


#-------- words from file --------
def words_from_file(filepath):
    with open(filepath, encoding='utf-8') as myfile:
        msg = myfile.read()
        words = msg.split()
    return words


words = words_from_file(fname)
print(f'{len(words)} words found in {fname}')
wcount = Counter(words)
print(f'{len(wcount)} unique words found in {fname}')

print('sample words:')
print(random.sample(words, 20))

print('most frequent words:')
sorted_wcount = sorted(wcount, key=wcount.get, reverse=True)
top10_words = sorted_wcount[:10]
for w in top10_words:
    print(w, wcount[w])


x = top10_words
y = [wcount[w] for w in x]

f, ax = plt.subplots()
ax.bar(x, y)
ax.set_title(f'most frequent words in {fname}')

plt.show()
plt.close()