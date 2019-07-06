# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 08:29:46 2019

@author: roppon
"""

# https://campus.datacamp.com/courses/writing-efficient-python-code/
# list_comprehension
import numpy as np


print('basic:')
mylist = list(range(1, 11))

outlist = [i if not (3 <= i <=8) else -i for i in mylist ]
print(outlist)


print('*' * 50)
print('word tokenization:')
sentences = ["a new world record was set", 
             "in the holy city of ayodhya", 
             "on the eve of diwali on tuesday", 
             "with over three lakh diya or earthen lamps", 
             "lit up simultaneously on the banks of the sarayu river"]

stopwords = ['for', 'a', 'of', 'the', 'and', 'to', 'in', 'on', 'with']

result = [w for sen in sentences for w in sen.split() 
                if w in sen and w not in stopwords]
print(result)


print('*' * 50)
print('advanced:')
# Create a list of arrival times
arrival_times = [*range(10,60,10)]

names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

# Convert arrival_times to an array and update the times
arrival_times_np = np.array(arrival_times)
new_times = arrival_times_np - 3

# Use list comprehension and enumerate to pair guests to new times
guest_arrivals = [(names[i],time) for i, time in enumerate(new_times)]

print(guest_arrivals)


def welcome_guest(x):
    return 'Welcome to Festivus {}... You\'re {} min late.'.format(*x) 


# Map the welcome_guest function to each (guest,time) pair
welcome_map = map(welcome_guest, guest_arrivals)

guest_welcomes = [*welcome_map]
print(*guest_welcomes, sep='\n')