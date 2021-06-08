# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 19:57:00 2021
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
"""

arr=[1,1,1,3,3,4,3,2,4,2]

def dup_yes(arr):
    arr.sort()
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            return arr[i] == arr[j]
        
print(dup_yes(arr))