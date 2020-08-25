# -*- coding: utf-8 -*-
"""
Created on Fri May 24 05:29:33 2019

@author: Admin
"""

# realpython.com/python-super

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    

# this class inherits from Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
        

class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return 6 * face_area
    
    
sq1 = Square(4)
print('area =', sq1.area())

cub1 = Cube(3)
print('surface are =', cub1.surface_area())