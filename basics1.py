# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 20:09:54 2018

@author: rop
"""

import os


# print something
print('hello world')

# define variables
var = 12
print(var)
var = "This is a string now"
print(var)
var = [2, 4, 6, 8]
print(var)


# enumerate
print('enumerate list:')
for index, item in enumerate(var):
    print (index, item)


# define function
def func():
    print('This is a function')

    
# call function
f = func
f()


# function with arguments
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
