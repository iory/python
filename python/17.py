#!/usr/bin/env python
# -*- coding:utf-8 -*-

def split_list(xlst, n):
    return xlst[:n], xlst[n:]

xlst = ["a","b","c","d","e","f","g","h","i","k"]
print(split_list(xlst, 3))
