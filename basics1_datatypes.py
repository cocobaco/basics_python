# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 20:09:54 2018

@author: rop
"""

import os

# Retrieve current working directory
cwd = os.getcwd()
print(cwd)

# Change directory
#os.chdir("/path/to/your/folder")

# List all files and directories in current directory
print(os.listdir('.'))

print('#########################################')
print('Data types')
print('#########################################')
      
print('There are 5 basic data types: int, float, str, boolean, and complex.')
x = 7
y = 4.2
z = 'hello world'
b = True
c = 1 + 2j
print(f'{type(x)}: {x}')
print(f'{type(y)}: {y}')
print(f'{type(z)}: {z}')
print(f'{type(b)}: {b}')
print(f'{type(c)}: {c}')

print('data type of a variable can be changed.')
var = 12
print('{} ({})'.format(var, type(var)))
var = "This is a string now"
print('{} ({})'.format(var, type(var)))
var = [2, 4, 6, 8]
print('{} ({})'.format(var, type(var)))


print('#########################################')
print('Math operations')
print('#########################################')
num1 = 25.
num2 = 4.
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)  # exact division
print(num1 % num2)  # remainder
print(num1 ** num2)
      

print('#########################################')
print('string operations')
print('#########################################')
string1 = 'Marcus Aurelius'
print(string1)
print(string1[1:4])
print(string1[::-1])  # reverse
print(len(string1))
print(string1.upper())
print(string1.lower())
print(string1.split())
print(string1.isdigit())
print(string1.isalpha())
print(string1.split()[0].isalpha())
print(string1.isprintable())
print(string1.index('r'))
print(string1.startswith('Z'))
string2 = string1.replace('M', 'Z')
print(string2)
print(string2.startswith('Z'))

print('*'*40)

print('tab and newline:')
print("Heya!\tHi!\nHello!\nWelcome!\nOla!")

print('---- string format ------')

string1 = 'c:\new folder\time'
print(string1)

# r prefix to indicate raw string, avoiding multiple escapes
string2 = r'c:\new folder\time'
print(string2)

name = 'Fred'
age = 45
# old way
print('He said his name is {} and he is {} years old.'.format(name, age))

# new way (use f prefix)
print(f'He said his name is {name} and he is {age} years old.')

print('#########################################')
print('Functions')
print('#########################################')
      
def high_and_low(numbers):
    num = [int(n) for n in numbers.split(' ')]
    return str(max(num)) + ' ' + str(min(num))

high_and_low('5 2 3 10 4 3 8')

def func():
    print('This is a function')

f = func

f()

# arbitrary number of arguments
def f2(*args):
    for i in args:
        print(i)

f2(2,5,9)

print('---- lambda function ------')
square = lambda x: x**2 # x is the argument
print(square(4))
tot = lambda x,y,z: x+y+2*z
print(tot(255,29,16))

print('------ lists, tuples, sets ------')
alpha = 'abracadabra'
print('string:', alpha)
lis1 = list(alpha)
tup1 = tuple(lis1)
set1 = set(alpha)

print('list:', lis1)
print('tuple:', tup1)
print('set:', set1)

print('---- dict ------')
dict1 = {}
for i, v in enumerate(alpha):
    dict1[i] = v
print(dict1.items())

def rundirect():
    print(os.path.basename(__file__), "is being run directly")

if __name__ == "__main__":
    rundirect()
else:
    print(os.path.basename(__file__), " is imported")
