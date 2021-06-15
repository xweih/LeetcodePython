# -*- coding: utf-8 -*-
"""
238. Product of Array Except Self

Given an array nums of n integers where n > 1, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

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