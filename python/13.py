#!/usr/bin/env python
# -*- coding:utf-8 -*-

def run_length_encoding(xlst):
    cnt = 1
    start = 0
    xlst += [None]
    for i, x in enumerate(xlst[1:], 1):
        if xlst[i] == xlst[i-1]:
            cnt += 1
        else:
            if cnt == 1:
                xlst[start] = xlst[i-1]
            else:
                xlst[start] = [cnt, xlst[i-1]]
            start += 1
            cnt = 1
    return xlst[:start]

xlst = ["a","a","a","a","b","c","c","a","a","d","e","e","e","e"]
print(run_length_encoding(xlst))
