#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 13:49:39 2022

@author: michaellee
"""
#from showcallstack import showcallstack
def factorial(number):
    product = 1
    for i in range(1, number + 1):
        product = product * i
    #showcallstack()
    return product
print(factorial(5))