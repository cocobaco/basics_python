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


# parsing
dt_string = '12 apr 2013'
print(dt_string)
day0 = datetime.datetime.strptime(dt_string, '%d %b %Y')
print(day0)

day_uno = datetime.datetime(year=2011, month=6, day=16)

# formatting
print(day0.strftime('%Y/%m/%d'))
print(day_uno)


# time difference
print('time from', day_uno, 'to now:')
diff = now - day_uno
print(diff)
print(diff.days)
print('years = {:.2f}'.format(diff.days / 365.))
