# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 19:09:18 2022

@author: Janas Laptop
"""

import pandas as pd 
import math

cov = pd.read_csv('cov.csv')


features = (4,5,6,7,8,11,12,13)



for row in range(0, len(cov)): 
    for col in features: 
        if(row > 1 and
           cov.iloc[row, 0] == cov.iloc[row-1, 0] and
           math.isnan(cov.iloc[row, col]) and 
           (not math.isnan(cov.iloc[row-1, col]))): 
            cov.iloc[row, col] = cov.iloc[row-1, col]
            
cov.to_csv('cov-less-na.csv', index = False)


