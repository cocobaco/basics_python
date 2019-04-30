# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 13:17:26 2019

@author: Admin
"""

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
                'y': 'and',
                'aunque': 'although, even though',
                'sino': 'but, except',
                'mientras': 'while',
                }


for k, v in spanish_conjunc.items():
    print('{:<12s} {}'.format(k, v))