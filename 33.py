# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 12:07:27 2021
Search in Rotated Sorted Array

"""


def rotated(nums,target):
    if target in nums:
        return nums.index(target)
    else:
        return -1
    
nums = [4,5,6,7,0,1,2]
target = 3

print(rotated(nums,target))