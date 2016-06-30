#!/usr/bin/env python
# -*- coding:utf-8 -*-

def eliminate_consecutive_duplicates(xlst):
    ret = [xlst[0]]
    for a, b in zip(xlst[:-1], xlst[1:]):
        if not a == b:
            ret.append(b)
    return ret

xlst = ["a","a","a","a","b","c","c","a","a","d","e","e","e","e"]
print(eliminate_consecutive_duplicates(xlst))
