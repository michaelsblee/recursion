#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 07:04:16 2022

@author: michaellee
"""

def exponentByIteration(a, n):
    result = 1
    for i in range(n):
        result *= a
    return result

print(exponentByIteration(3, 6))
print(exponentByIteration(10, 3))
print(exponentByIteration(17, 10))