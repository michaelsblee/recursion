#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 07:07:44 2022

@author: michaellee
"""

def exponentByRecursion(a, n):
    if n == 1:
        # base case
        return a
    elif n % 2 == 0:
        # recursive case when n even
        result = exponentByRecursion(a, n // 2)
        return result * result
    elif n % 2 == 1:
        # recursive case when n odd
        result = exponentByRecursion(a, n // 2)
        return result * result * a
    
print(exponentByRecursion(3, 6))
print(exponentByRecursion(10, 3))
print(exponentByRecursion(17, 10))