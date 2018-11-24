# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 20:09:54 2018

@author: rop
"""

import os

print('hello world')

var = 12
var = "This is a string now"
var = [2, 4, 6, 8]
print(var)
var.insert(1,7)
print(var)

def func():
    print('This is a function')
 
f = func

f()

def f2(*args):
    for i in args:
        print(i)

f2(2,5,9)

# lambda function
square = lambda x: x**2 # x is the argument
print(square(4))
tot = lambda x,y,z: x+y+2*z
print(tot(255,29,16))

def rundirect():
    print(os.path.basename(__file__), " is being run directly")

if __name__ == "__main__":
    rundirect()
else:
    print(os.path.basename(__file__), " is imported")