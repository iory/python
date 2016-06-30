#!/usr/bin/env python
# -*- coding:utf-8 -*-

def run_length_encoding(xlst):
    ret = [[1, xlst[0]]]
    for a, b in zip(xlst[:-1], xlst[1:]):
        if a == b:
            ret[-1][0] += 1
        else:
            ret.append([1, b])
    return ret

xlst = ["a","a","a","a","b","c","c","a","a","d","e","e","e","e"]
print(run_length_encoding(xlst))
