#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 05:43:44 2022

@author: michaellee
"""

def a():
    print('a() was called.')
    b()
    print('a() is returning')

def b():
    print('b() was called.')
    c()
    print('b() is returning')
    
def c():
    print('c() was called.')
    print('c() is returning')
    
a()