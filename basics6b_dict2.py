# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 13:17:26 2019

@author: Admin
"""

import random


spanish_conjunc = {'que': 'that, who, which, than',
                'y':  'and',
                'o': 'or',
                'como': 'as, like', 
                'pero': 'but',
                'si': 'if',
                'porque': 'because',
                'cuando': 'when',
                'ni': 'nor, neither',
                'donde': 'where',
                'e': 'and',
                'aunque': 'although, even though',
                'sino': 'but, except',
                'mientras': 'while',
                'pero': 'but', 
                'ya que': 'since', 
                'siempre que': 'as long as', 
                }


for k, v in spanish_conjunc.items():
    print('{:<12s} {}'.format(k, v))
    
    
print('*' * 30)
print('Word of the day:')
espanola = random.choice(list(spanish_conjunc.keys()))
print('{}: {}'.format(espanola, spanish_conjunc[espanola]))