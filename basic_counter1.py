# -*- coding: utf-8 -*-
"""
Created on Thu May 23 10:51:54 2019

@author: Admin
"""

from collections import Counter

# initilization (same result)
print(Counter(['a', 'b', 'c', 'a', 'b', 'b']))

print(Counter({'a':2, 'b':3, 'c':1}))

print(Counter(a=2, b=3, c=1))

print(Counter('hello world'))