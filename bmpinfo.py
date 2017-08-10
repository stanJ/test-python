#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import struct, os

def checkBmp():
    path = input('请输入文件路径: ')
    if os.path.splitext(path)[1] == '.bmp':
        with open(path, 'rb') as f:
            s = f.read(30)
        info = struct.unpack('<ccIIIIIIHH', s)
        print('图片大小: %s * %s 颜色数: %s 文件大小: %s' % (info[6], info[7], info[9], info[2]))
    else:
        print('不是.bmp文件')

if __name__ == '__main__':
    checkBmp()