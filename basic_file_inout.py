# -*- coding: utf-8 -*-
"""
Created on Wed May 17 11:03:28 2017

@author: roppon
"""
import time
import random

#my_list = [i**2 for i in range(1,11)]
#my_file = open("testoutput.txt","w")
#
#for item in my_list:
#    my_file.write(str(item) + "\n")
#
#my_file.close()
#
#my_file.open("testoutput.txt","r")
#print (my_file.read())
#my_file.close()

t1 = time.time()

print('a text file will be written!')

# file open modes:
# r  = read (default)
# w  = write, truncate
# r+ = read/write
# w+ = read/write, truncate
# a+ = read/append
fname = 'data/testtext.txt'
greets = ['Hi', 'Hola', 'Hello', 'Tchao', 'Ola', 'Obrigado', 'Ciao']

# open file for reading
with open(fname, 'r') as textfile:
    for i, line in enumerate(textfile):
        last_line = line
        pass
    print('there are {} lines in the file'.format(i + 1))
print('last line:', last_line)


# open file for reading and writing
with open(fname, 'a+') as textfile:
    greet = random.choice(greets)
    print(greet)
    textfile.write('\n' + random.choice(greets))

# check if file is closed
if not textfile.closed:
    textfile.close()

t2 = time.time()
print('time elapsed: {}'.format(t2 - t1))