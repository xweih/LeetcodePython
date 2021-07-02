# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 12:14:20 2021

11. Container With Most Water
"""

height = [1,2,1]

def MostWater(height):
    max=0
    left=right=0
    for i in range(len(height)-1):
        for j in range(i+1,len(height)):            
            s = min(height[i], height[j]) * (j-i)
            print(i,j,s)
            if s > max:
                left = i
                right = j
                max = s                
    return height[left], height[right], max 

print(MostWater(height))
