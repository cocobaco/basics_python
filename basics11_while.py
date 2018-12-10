# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 07:08:44 2018

@author: Admin
"""

n = 0 

while n < 10:
    print(n)
    n += 1
    
    
a = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
while a:
    print(a.pop(-1))
    
    
# break / continue
#  break takes you out of current loop and go to next statement
#  continues ends the current loop iteration, and go to the top of the loop
  
print('continue example:')
x = 5
while x > 0:
    x -= 1
    if x == 2:
        continue
    print(x)
print('Loop ended')


print('break example:')
x = 5
while x > 0:
    x -= 1
    if x == 2:
        break
    print(x)
print('Loop ended')