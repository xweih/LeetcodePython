# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 17:45:56 2021

@author: Xiaowei
"""

nums=[1,2,3,4]

def prod_except_self(nums):
    
    product = []     
    
    for i in range(len(nums)):
        
        copy=nums[:]  # essential: WRONG copy=nums 
        copy.pop(i)
        prod = 1
        
        for j in copy:
            prod = prod*j        
        
        product.append(prod)
        
    return product

print(prod_except_self(nums))