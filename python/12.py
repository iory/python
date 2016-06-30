#!/usr/bin/env python
# -*- coding:utf-8 -*-

def decode_run_length_encoding(xlst):
    ret = []
    for x in xlst:
        ret.extend(x[1] * x[0])
    return ret

xlst = [[4, 'a'], [1, 'b'], [2, 'c'], [2, 'a'], [1, 'd'], [4, 'e']]
print(decode_run_length_encoding(xlst))
