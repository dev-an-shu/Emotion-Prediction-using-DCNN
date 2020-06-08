# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 14:51:17 2020

@author: Devanshu
"""

import numpy as np

a = np.array([[1,2,3],
			  [1,2,3],
			  [1,2,3],
			  [1,2,3],
			  [4,5,6]])

print("Before: ",a.shape)

a = np.reshape(a, (6,3))

print("After: ",a.shape)