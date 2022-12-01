#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 06:03:16 2022

@author: michaellee
"""

def a():
    spam = 'Ant'
    print('spam is ' + spam)
    b()
    print('spam is ' + spam)

def b():
    spam = 'Bobcat'
    print('spam is ' + spam)
    c()
    print('spam is ' + spam)
    
def c():
    spam = 'Coyote'
    print('spam is ' + spam)
    
a()