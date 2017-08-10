#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
# try:
#     f = open('aa.txt', 'r', encoding='utf-8')
#     print(f.read())
# except FileNotFoundError as e:
#     logging.exception(e)
# finally:
#     if f:
#         f.close()

# with open('test.txt', 'r', encoding='utf-8') as f:
#     for line in f.readlines():
#         print(line.strip())

# with open('群体.jpg', 'rb') as f:
#     print(f.read())

with open('test.txt', 'w') as f:
    f.write('Hello, Stan!')