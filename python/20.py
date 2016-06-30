#!/usr/bin/env python
# -*- coding:utf-8 -*-

def remove_at(xlst, k):
    return xlst[k-1], xlst[:k-1] + xlst[k:]

xlst = ['a', 'b', 'c', 'd']
print(remove_at(xlst, 2))
