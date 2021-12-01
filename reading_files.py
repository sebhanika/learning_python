# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 22:32:12 2021

@author: hanik
"""

# This code introduces the concept of reading and writing files into python

#%% setting working diretory 

# this code sets the working directory to the script file location 
# and change the current working directory
import os 
import math

os.chdir(os.path.abspath(os.path.dirname(__file__)))
print(os.getcwd()) # checking if location is correct

#%%  Task 1

# creating a dictionary of soil temperature and coordinates

# data loading and data wrangling
with open(r'soil_temp.txt', 'r') as f:
    read_data = f.readlines()

# Removing the first item which is the header of the file
del read_data[0]

# setting threshold for later
thres = 8

# initating lists
ID = []
x = []
y = []
soil_temp = []

# splitting lists 
for line in read_data:
        Type = line.split(", ")
        ID.append(Type[0])
        x.append(Type[1])
        y.append(Type[2])
        soil_temp.append(Type[3])
        
# deleting trailing \n
soil_temp = [x.strip('\n') for x in soil_temp]

# turing ID and temp into integers
ID = ([int(i) for i in ID])
soil_temp = ([int(i) for i in soil_temp])

# Looping over all samples/ copied code from exercise 4 
coor_dict = dict(zip(ID, soil_temp))# create dictionary

for keys in coor_dict:
    if coor_dict[keys] > thres:
        print(f' At ID {keys} the soil temperature is {coor_dict[keys]}')
    else:
        pass
    
#%% Task 2 

# reads in data from polyline file and calculates the length of polylines
 
with open('polyline.txt', 'r') as p:
    for line in p:
        temp_line = line.strip('\n') # first strip, then split. Otherwise error
        temp_line = temp_line.split('; ')
        id_poly = temp_line[0] # stores ID
        coord = temp_line[1:] # selects only coordinate pairs
        coord = list(map(eval, coord)) # evaluates string as numbers
        poly_length = 0.0 
        
        for i in range(len(coord)-1):
            coord_pair1 = tuple(coord[i])
            coord_pair2 = tuple(coord[i+1])
            
            # storing x and y varibles as floats
            xi = float(coord_pair1[0]) 
            yi = float(coord_pair1[1])
            xii = float(coord_pair2[0])
            yii = float(coord_pair2[1])
            
            # calculating final length
            poly_length += round(
                            math.sqrt((xii - xi)**2 + (yii - yi)**2)
                                ,3)
            # printing final answers
        print(f'For Polyline {id_poly} the coordinates are: {coord}')
        print(f'and he sum of segment lengths is {poly_length}\n')
         
#%%