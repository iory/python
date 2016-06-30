#!/usr/bin/env python
# -*- coding:utf-8 -*-

def extract_slice(xlst, start, end):
    return xlst[start-1:end]

xlst = ["a","b","c","d","e","f","g","h","i","k"]
print(extract_slice(xlst, 3, 7))
