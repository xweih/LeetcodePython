# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 20:01:39 2021
Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


def max_prof(prices):
    profits = [0]
    for i in range(len(prices)-1): 
        for j in range(i+1,len(prices)):
            if prices[i] < prices[j]: 
                profits.append(prices[j]-prices[i])
            else: 
                continue
                
    return max(profits)

prices = [7,6,4,3,1]

print(max_prof(prices))