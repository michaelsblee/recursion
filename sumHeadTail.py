#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 09:47:10 2022

@author: michaellee
"""

def sum(numbers):
    if len(numbers) == 0:
        # base case
        return 0
    else:
        # recursive case
        head = numbers[0]
        tail = numbers[1:]
        return head + sum(tail)
    
nums = [1,2,3,4,5]
print('The sum of', nums, 'is', sum(nums))
nums = [5,2,4,8]
print('The sum of', nums, 'is', sum(nums))
nums = [1,10,100,1000]
print('The sum of', nums, 'is', sum(nums))