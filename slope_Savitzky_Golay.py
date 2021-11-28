# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 10:34:30 2021

@author: hanik
"""
# Exercise 6

#%% Importing modules and wd

import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter # used for double checking in task 2

os.chdir(os.path.abspath(os.path.dirname(__file__)))
print(os.getcwd()) # checking if location is correct

#%% Task 1 ######### 
# Slope calculations with Numpy

#Defining function 

def slope_calc(dem, res, dimension):
    rows = dimension[0]
    cols = dimension[1]
    empty_dem = np.zeros(dimension) - 1
    dist_win = [[np.sqrt(2), 1, np.sqrt(2)], 
            [1, -1, 1], [np.sqrt(2),  1, np.sqrt(2)]] # Window with distances to the cells

    dist_win = [[z * res for z in y] for y in dist_win] # multiplying by resolution
    
    for r in range(1,rows-1):
        for c in range(1,cols-1):
            temp_win = dem[r-1:r+2,c-1:c+2]
            for i in temp_win:
                         diff = abs(temp_win[1][1] - temp_win)
                         slope_win = diff/dist_win
                         slope_max = np.amax(slope_win)
            
            empty_dem[r][c] = slope_max # stores values in empty_dem
            
    return(empty_dem)
   

#%% Calculating slope of a Absiko DEM

#reading in text file
dem_abisko = np.loadtxt('dem_Abisko.txt', dtype = 'int', 
                 delimiter = ',')  #Loading DEM

#calulating slope
slope_abisko = slope_calc(dem = dem_abisko, res = 50,
                      dimension = np.shape(dem_abisko))

#%%

#Saving text file
np.savetxt('slope_abisko.txt', 
           slope_abisko,  fmt='%.4e',
           delimiter=',',
           newline='\n') 

#%% Plotting 

plt.imshow(slope_abisko, cmap=plt.cm.jet)
plt.colorbar()
plt.title('Slope for Abisko DEM (50m resolution)')
plt.show()



#%% Task 2 #############################################################

# Savitzky-Golay filter with numpy

ndvi = np.loadtxt('ndvi_no_outliers.txt',
                  dtype = 'float', 
                  delimiter = ',') # load data

ndvi_size = np.shape(ndvi) # size of array

sg = np.zeros(ndvi_size[0]) # For filtered data

# Values of x to fit the polynomial.
x_val = np.arange(1,8)
    
# Looping over all values except the first and last 3
for i in range(3,ndvi_size[0]-3):
    # Fit the polynomial
    sg_temp = np.polyfit(x = x_val, y = ndvi[i-3:i+4], deg = 2)
    # Evaluating the polynomial at the middle point
    sg[i] = np.polyval(sg_temp, 4)
    

#%% using the scipy package for double checking

# scipy svagol function
scipy_check_sg = savgol_filter(ndvi, window_length=7, polyorder = 2)

# results are very similar but not exactly the same due to 
# large number of decimal places
scipy_check_sg = np.around(scipy_check_sg, 5)
sg_check  = np.around(sg, 5)

# comparing both arrays
compare_sg = scipy_check_sg[3:684] == sg_check[3:684]

equal_arrays = compare_sg.all()

print(equal_arrays)


#%% plotting
#8-day intervals during the period 2000-2014
x = np.arange(0, 5492, 8)

plt.plot(x, ndvi, label = "Median-NDVI", color = "grey")
plt.plot(x, sg, label = "SG-filtered", color = "red", linestyle='dotted')
plt.title('NDVI with Savitzky-Golay filter applied')
plt.xlabel('Number of days between 2000 to 2014')
plt.ylabel('NDVI (scaled)')
plt.legend(loc = 'lower right')
plt.show()
    
    