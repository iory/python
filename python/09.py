#!/usr/bin/env python
# -*- coding:utf-8 -*-

def pack_consecutive_duplicates_to_list(xlst):
    ret = [[xlst[0]]]
    for a, b in zip(xlst[:-1], xlst[1:]):
        if a == b:
            ret[-1].append(b)
        else:
            ret.append([b])
    return ret

xlst = ["a","a","a","a","b","c","c","a","a","d","e","e","e","e"]
print(pack_consecutive_duplicates_to_list(xlst))
