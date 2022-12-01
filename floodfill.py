#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 21:12:31 2022

@author: michaellee
"""

import sys

# create the image (rectangular)
im = [list('..#########################..........'),
      list('..#.......................#..#####...'),
      list('..#......#########........####...#...'),
      list('..#......#.......#...............#...'),
      list('..#......#########.............###...'),
      list('..####.........................#.....'),
      list('.....#..####............########.....'),
      list('.....####..##############............')]

HEIGHT = len(im)
WIDTH = len(im[0])


def floodFill(image, x, y, newChar, oldChar=None):
    if oldChar == None:
        # oldChar defaults to the character at x, y
        oldChar = image[y][x]
    if oldChar == newChar or image[y][x] != oldChar:
        # base case
        return
