#!/usr/bin/env python
# -*- coding:utf-8 -*-

def duplicate_elements(xlst):
    ret = []
    for x in xlst:
        ret.extend(x * 2)
    return ret

xlst = ["a","b","c","c","d"]
print(duplicate_elements(xlst))
