# -*- coding: utf-8 -*-
"""
53. Maximum Subarray  

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
"""

def max_subarray(nums):
    sub_sum = nums[0]
    print(sub_sum)
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if (i==j) and (nums[j] > sub_sum):
                sub_sum = nums[j]
                print(i,j,nums[i],nums[j],sub_sum)
            elif sum(nums[i:j]) > sub_sum:
                sub_sum = sum(nums[i:j])
                print(i,j,nums[i],nums[j],sub_sum)
            else:
                print(nums[0],nums[i],nums[j])
            print('\n')
    return sub_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]


print(max_subarray(nums))

