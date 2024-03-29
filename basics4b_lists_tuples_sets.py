# -*- coding: utf-8 -*-
"""
Created on Sat May  6 20:48:23 2017

@author: Admin
"""
import time
import timeit
import matplotlib.pyplot as plt
from collections import Counter
from collections import namedtuple


numbers = [1, 2, 4, 4, 8]

list1 = []
for k in numbers:
    list1.append(k**2)
print(numbers)
print(list1)
print(Counter(list1))


print('*' * 50)

list_a = [1.74, 1.68, 1.55, 1.82, 1.94]
list_b = [64.2, 62.5, 55.4, 102.3, 145.7]
zipped = zip(list_a,list_b)

print('zip lists:')
for x, y in zipped:
    print(x, y)
    
list_a.append(1.55)
list_a.append(1.68)
list_b_sorted = sorted(list_b,reverse=False)
list_b_sorted_str = ', '.join(map(str,list_b_sorted))

print('list_a:')
print(list_a)
print(list_a.index(1.55))
print(list_a.count(1.68))
print(len(list_a))

print('list2 sorted:')
print(list_b_sorted)
print(list_b_sorted_str)

list_c = [[1,2,5],[4,5,6],[7,8,9]]
print('list_c:')
print(list_c)

print('*'*50)

to_one_hundred = range(101)
backwards_by_tens = to_one_hundred[::-10]
print (backwards_by_tens)

to_21 = range(1,22)
odds = to_21[::2]
middle_third = to_21[7:14:1]
print (odds)
print (middle_third)

print('*'*50)

print('remove item from list:')
list2 = ['a', 'b', 'b', 'c']
print(list2)
list2.remove('b')
print('removed b:')  # if multiple matches, only first one is removed
print(list2)


print('*'*50)

print('compare time generator vs list:')
LARGE_NUM = int(5e5)

tic = time.process_time()
xyz = (i for i in range(LARGE_NUM)) #generator
#print(list(xyz)[:5])
toc = time.process_time()
print('generator:', toc-tic)

tic = time.process_time()
xyz = [i for i in range(LARGE_NUM)]
#print(xyz[:5])
toc = time.process_time()
print('list:', toc-tic)

print('timeit:')
ti1=timeit.timeit('"-".join(str(n) for n in range(100))', number=LARGE_NUM)
print(ti1)
ti2=timeit.timeit('"-".join([str(n) for n in range(100)])', number=LARGE_NUM)
print(ti2)
ti3=timeit.timeit('"-".join(map(str, range(100)))', number=LARGE_NUM)
print(ti3)

xplot = [1, 2, 3]
xlabels = ['join', 'join[]', 'join(map)']
plt.figure()
plt.bar(x=xplot, height=[ti1, ti2, ti3])
plt.xticks(xplot, xlabels)
plt.margins(0.2)

plt.show()

print('*'*50)

def square(x):
        return (x**2)

value = map(square, list1)
print(list(value))

print('*' * 50)
print('Tuples:')
print('tuples are similar to lists but their elements cannot be changed')

tup = (1, 4, 'hello', 5.24)
print('tuple:')
for i, v in enumerate(tup):
    print(i, v)
print('len(tup):', len(tup))

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])

tup3 = tup1 + tup2
print('tup3:', tup3)
print('3*(tup3): ', 3*(tup3))

tup4 = (15,252,6363,242,236)
print('tup4:', tup4)
del tup4


print('namedtuple:')
Point = namedtuple('Point', ['x', 'y'])
p = Point(4, 7)
print(p.x)
print(p.y)
print(p)

print('*' * 50)
print('Sets:')
print('sets are used to build sequence of unique items')
a = set([1, 2, 3, 4])
b = set([3, 4, 5, 6])
print(a)
print(b)
# union
print(a | b)
# intersection
print(a & b)
# subset
print(a < b)
# difference
print(a - b)
# symmetric difference
print(a ^ b)

fruits = ['apple','lychee', 'apple', 'longan','mango','pineapple','longan']
fruits_set = set(fruits)
print('set:')
print(fruits_set)
print('is longan in fruits_set? ', ('longan' in fruits_set))
print('is banana in fruits_set? ', ('banana' in fruits_set))

mySet = set((x,y) for x in range(1,3) for y in range(-2,1))
print(mySet)