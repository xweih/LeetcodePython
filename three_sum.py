# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 21:33:23 2021

@author: freed
"""

nums_1 = [0]
target_1 = 0

def three_sum(nums,target):
    
    nums.sort()
    
    collect = []
    
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                if nums[i]+nums[j]+nums[k] == target and [nums[i],nums[j],nums[k]] not in collect:
                    collect.append([nums[i],nums[j],nums[k]])  
    
    return collect

print(three_sum(nums_1,target_1))