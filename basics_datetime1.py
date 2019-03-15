# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:27:40 2019

@author: Admin
"""

from datetime import datetime as dt

now = dt.now()

print("Current date and time: " , now)

print(now.strftime("%y-%m-%d-%H-%M"))

print(now.year)
print(now.strftime("%A"))
print(now.strftime("%B"))

day1 = dt(2019, 3, 15)
print(day1)