#!/usr/bin/env python
# -*- coding:utf-8 -*-

def duplicate_elements(xlst, times=2):
    ret = []
    for x in xlst:
        ret.extend(x * times)
    return ret

xlst = ["a","b","c","c","d"]
print(duplicate_elements(xlst, 3))
