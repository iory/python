#!/usr/bin/env python
# -*- coding:utf-8 -*-

def flatten(xlst):
    ret = []
    for x in xlst:
        if isinstance(x, list):
            ret.extend(flatten(x))
        else:
            ret.append(x)
    return ret

xlst = [1,2,[1,2,3,[0 ,[0,[0,[]]]], [[[[[]]]]], [1,]]]
print(flatten(xlst))
