# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 14:10:47 2019

@author: Admin
"""

add_one = lambda x: x + 1
print(add_one(5))


full_name = lambda first, last: first + ' ' + last
print(full_name('leo', 'messi'))


raise_power = lambda x, y, n: n * x - y**n
print(raise_power(2, 3, 4))


add_values_minus_5 = lambda *x: sum(x) - 5
print(add_values_minus_5(1, 2, 7, 5, 6))