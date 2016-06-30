#!/usr/bin/env python
# -*- coding:utf-8 -*-

def drop_every_nth_element(xlst, n):
    ret  = []
    for i, x in enumerate(xlst):
        if ((i+1) % n) == 0:
            continue
        ret.append(x)
    return ret

xlst = ["a","b","c","d","e","f","g","h","i","k"]
print(drop_every_nth_element(xlst, 3))
