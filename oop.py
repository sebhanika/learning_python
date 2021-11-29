# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 20:16:03 2021

@author: hanik
"""

### This code is my introduction to object oriented programming. I creates 
# three objects (point , circle, polyline) and calculates different
# characteristics for each of them. 
# This code includes some tests in the bottom

# importing neccessary functions
from math import pi, sqrt

#%% Points

# Created by giving position as an (x,y) tuple   
class Point:
    def __init__(self, pos):
        # tuple with the x and y coordinates as: (x, y)
        self.pos = tuple(pos)
    
    def move(self, dx, dy):
        # Moving in x and y direction
        self.pos = (self.pos[0] + dx, self.pos[1])
        self.pos = (self.pos[0], self.pos[1] + dy)
        
    def __str__(self):
        return f'The point is located at: {self.pos}'


#%% Circle

class Circle:
    def __init__(self, pos, radius):
        # (x, y) tuple as center Point of circle 
        # radius of circle 
        self.pos = tuple(pos)
        self.radius = radius
        
    def area(self):
        # area of the circle
        self.area = round((pi * self.radius**2),4) # rounding for better printing
        
    def move(self, dx, dy):
        # Moving in x and y direction
        self.pos = (self.pos[0] + dx, self.pos[1])
        self.pos = (self.pos[0], self.pos[1] + dy)
        
    def __str__(self):
        
        return (f'The center of the circle is located at: {self.pos}.\n'
                f'The area of the circle is: {self.area}')
        
#%% Polyline
      
class PolyLine:
    def __init__(self, points):        
        
        # list of (x, y) tuples
        self.points = list(points)
        
    def move(self, dx, dy):
        
        # moving polyline by moving each points in x and y direction
        
        self.points_new = [] # new list for new points
        
        for index, values in enumerate(self.points):
              self.points_new.append( 
                  (values[0] + dx, values[1] + dy) 
                  )
        
        
    def length(self):
        # calculate length of polyline
        for item in self.points:
            n = len(self.points)-1
            self.length = 0.0
            for i in range(n):
                self.length += sqrt((self.points[i+1][0]-self.points[i][0])**2 +
                                (self.points[i+1][1]-self.points[i][1])**2)
                self.length = round(self.length, 3)
    

    def __str__(self):
        
        return (f'The length of the line segments is {self.length}.'
                f'The points were orginally located at: {self.points}.'
                f' The points were moved to: {self.points_new}')
    
# Testing code
if __name__ == '__main__':
    
    # testing code point 
    p1 = Point(pos = [4,5]) # creates point, input as list
    p1.move(dx = 2, dy = 3) # moving point
    assert p1.pos == (6,8) , 'The point was not properly moved'
    print(p1)
    
    #testing code circle
    circle1 = Circle(pos = (3,9), radius = 5)
    circle1.move(dx = 1, dy = 4) # moving point
    assert circle1.pos == (4,13) , 'The point was not properly moved'
    circle1.area()
    assert circle1.area > 0 , 'The area was not properly calculated'
    print(circle1)
    
    #testing code polyline
    polyline1 = PolyLine(points = [(2,2), (3,3), (3,6), (4,8)])
    polyline1.move(dx = 1, dy = 3) # moving point
    
    assert polyline1.points_new == [(3,5), (4,6), (4,9), (5,11)] , 'The points was not properly moved'
    polyline1.length()
    print(polyline1)
    
