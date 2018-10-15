# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 11:13:02 2017

@author: Admin
"""

import datetime

now = datetime.datetime.now()
print('now:', now)
print ('date (yyyy mm dd): ', now.year, now.month, now.day)
print ('time (hh mm ss): ', now.hour, now.minute, now.second)
print(now.date().strftime('%A, %B %d, %Y'))

name = input('What is your name: ')
print(' '.join(['Hello there', name]))

while True:
    try:
        age = int(input("{}, enter your age: ".format(name)))
        if age > 0:
            break
    except:
        pass

year_turn_100 = 1
if age >= 100:
    print("you were born in " + str(now.year - age))
    print("you are old!")
else:
    year_turn_100 = now.year + (100 - age)
    print("you were born in " + str(now.year - age))
    print("you will turn 100 in the year " + str(year_turn_100))
    if age % 2 == 1:
        print("your age is an odd number!")
    else:
        print("your age is an even number!")
