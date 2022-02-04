# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 18:38:16 2018

@author: Admin
"""


def main():
    while True:
        name = input('enter your name: ')
        if name.isalpha():
            break
        print('please enter letters only.')

    print('your name is {}'.format(name))
    print('your name is {}'.format(name.rjust(20)))
    print('your name is {}'.format(name.ljust(30, '*')))
    print('your name is {}'.format(name.center(30, '*')))

    while True:
        age = input('enter your age: ')
        if age.isdecimal():
            break
        print('please enter numbers only.')

    while True:
        pw = input('enter your password: ')
        if pw.isalnum():
            break
        print('please enter numbers and letters.')

    print('{}'.format('Summary'.center(30, '*')))
    print('{} {}'.format('your name is'.ljust(30, '-'), name.rjust(30, '-')))
    print('{} {}'.format('your age is'.ljust(30, '-'), age.rjust(30, '-')))
    print('{} {}'.format('finally, your pw is'.ljust(30, '-'),
                         pw.rjust(30, '-')))

    print('*'*50)


if __name__ == '__main__':
    main()
