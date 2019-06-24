# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:27:40 2019

@author: Admin
"""

import datetime

now = datetime.datetime.now()

print("Current date and time:" , now)

print(now.strftime("%y-%m-%d-%H-%M"))

print(now.year)
print(now.strftime("%A"))
print(now.strftime("%B"))

# time difference
day1 = datetime.datetime(2011, 6, 16)
print(day1)

print('time from', day1, 'to now:')
diff = now - day1
print(diff)
print(diff.days)
print('years =', diff.days / 365.)
