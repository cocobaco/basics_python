# -*- coding: utf-8 -*-
"""
Created on Wed May  2 13:57:12 2018

@author: Admin
"""

dict1 = {'Health': [55,40,50,10,25,55,7,14,45,8,4,40,60,30], 
        'Procrastination': [44,13,27,25,20,14,32,19,22,15,35,3,44,12], 
        'Effort': [5,75,43,82,99,78,34,44,99,21,25,72,45,37], 
        'Pass': [0,1,0,0,1,1,0,0,1,0,0,1,0,0]}

print('keys:')
print(dict1.keys())

print('values:')
print(dict1.values())

print('items:')
print(dict1.items())

print('list of keys:')
print(list(dict1.keys()))

print('check key:')
print('Health in dict1.keys():', 'Health' in dict1.keys())
print('Strength in dict1.keys():', 'Strength' in dict1.keys())

print('use fallback value in case of non-existing key:')
print('Effort:', dict1.get('Effort','no such data'))
print('Luck:', dict1.get('Luck','no such data'))

print('*'*50)

# nested dict
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'sandwiches': 4, 'apples': 2},
             'Carol': {'cups': 4, 'apple pies': 1},
             'Doug': {'cups': 9, 'sandwiches': 2}}

print('Alice brings {} pretzels'.format(allGuests['Alice']['pretzels']))

def count_item(guests, item):
    ans = 0
    for g, v in guests.items():
#        ans += v[item]
        ans += v.get(item, 0)
    return ans

print('{:10s} {}'.format('apples', count_item(allGuests,'apples')))
print('{:10s} {}'.format('pretzels', count_item(allGuests,'pretzels')))
print('{:10s} {}'.format('cups', count_item(allGuests,'cups')))
print('{:10s} {}'.format('sandwiches', count_item(allGuests,'sandwiches')))


# merge dicts
x = {'a': 5, 'b': 3}
y = {'a': 4, 'b': 2, 'c': 7}

z = {**x, **y}  # match key, overwriting duplicates
print(z)