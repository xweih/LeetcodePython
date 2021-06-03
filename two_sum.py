# -*- coding: utf-8 -*-
"""
TWO sum
"""
nums=[11,2,7]
target=9

def two_sum(nums,target):
    
    basket = {}
    
    for ind, val in enumerate(nums):
        remainder = target-nums[ind]
            
        if remainder in basket:
            return [ind,basket[remainder]]
        else: 
            basket[val]=ind 

print(two_sum(nums,target))