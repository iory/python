#!/usr/bin/env python
# -*- coding:utf-8 -*-

def rotate(xlst, n):
    n %= len(xlst)
    return xlst[n:] + xlst[:n]

xlst = ["a","b","c","d","e","f","g","h"]
print(rotate(xlst, 3))
print(rotate(xlst, -2))
