#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 14:02:37 2022

@author: michaellee
"""

def fibonacci(nthNumber):
    a, b = 1, 1
    print('a = %s, b = %s' % (a, b))
    for i in range(1, nthNumber):
        a, b = b, a + b # get the next Fibonacci number
        print('a = %s, b = %s' % (a, b))
    return a

print(fibonacci(10))
