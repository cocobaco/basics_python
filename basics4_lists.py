# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 10:00:14 2020

@author: Admin
"""

# https://campus.datacamp.com/courses/writing-efficient-python-code/


numbers = [2, 50, 4, 18, 6, 4, 3, 12, 18]
print('original list:', numbers)

print('remove: remove in-place the first element matching value')
numbers.remove(4)
print('remove 4:', numbers)

print('insert: insert in-place at specified location')
numbers.insert(1, 100)
print('insert at index 1 the value 100:', numbers)

print('del: remove element by index')
del numbers[2]
print('del the 3rd element:', numbers)


print('*' * 50)

first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# add two lists
full = first + second
print(full)


print('normal list call from range: ')
print(list(range(3, 6)))
print('list call from unpacking a list: ')
lim = [3, 6]
print(list(range(*lim)))


print('list comprehension:')
m = [i ** 3 for i in range(1,15) if i**3 % 4 == 0]

l = [i ** 2 for i in range(1, 14)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

mylist = list(range(1, 11))
outlist = [i if not (3 <= i <=8) else -i for i in mylist ]

print(outlist)
print (m)
print(l)
print(mylist)
print(outlist)


print('list slicing:')
#list[start:stop:stride]
print (m[::2])
print (l[::-1]) # reverse order
print (l[2:10:2])


print('string operation:')
person = ['jon', 'ingrid', 'arya', 'mountain', 'hulk']
person_up = [x.upper() for x in person]
print(person_up)
person_low = [x.lower() for x in person]
print(person_low)


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
