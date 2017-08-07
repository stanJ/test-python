#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

pwd = os.path.abspath('.')
curPath = pwd
key = input('请输入搜索关键字: ')
def search(curPath):
    for f in os.listdir(curPath):
        absPath = os.path.join(curPath, f)
        if os.path.isfile(absPath):
            if key in f:
                relativePath = absPath[len(pwd)+1:]
                print(relativePath)
        else:
            search(absPath)
search(curPath)