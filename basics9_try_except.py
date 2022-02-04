# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 13:25:11 2018

@author: roppon
"""

x = int(input('x: '))
y = int(input('y: '))

try:
    print('x*y = {}'.format(x * y))
    print('x/y = {}'.format(x / y))
except:
    print('there is an error.')