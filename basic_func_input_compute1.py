# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 08:33:40 2017

@author: roppon
"""

def age_in_sec(age):
    if type(age) not in [int,float]:
        raise TypeError('must use a number')
    return(age*365*24*60*60)

def age_type(age):
    if type(age) not in [int,float]:
        raise TypeError('must use a number')
    if age < 5:
        return "baby"
    elif age < 13:
        return "kid"
    elif age < 20:
        return "teenager"
    elif age < 40:
        return "young adult"
    elif age < 66:
        return "middle age"
    else:
        return "senior"

while True:
    yrage = int(input("How old are you (in y)?: "))
    if yrage > 0:
        break

print('I guess you will be ' + str(yrage+5) + ' in 5 years.')
print(f'You are {age_type(yrage)}, who is {age_in_sec(yrage):,d} seconds old.')

