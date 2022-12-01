#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 07:12:31 2022

@author: michaellee
"""

def exponentWithPowerRule(a, n):
    # step 1: determine the operations to be performed
    opStack = []
    while n > 1:
        if n % 2 == 0:
            # n is even
            opStack.append('square')
            n = n // 2
        elif n % 2 == 1:
            # n is odd
            n -= 1
            opStack.append('multiply')
    
    # step 2: perform the operations in reverse order
    result = a # start reesult at 'a'
    while opStack:
        op = opStack.pop()
        
        if op == 'multiply':
            result *= a
        elif op == 'square':
            result *= result
    
    return result

print(exponentWithPowerRule(3, 6))
print(exponentWithPowerRule(10, 3))
print(exponentWithPowerRule(17, 10))