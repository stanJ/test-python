#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
logging.basicConfig(level=logging.INFO)
import pdb
def foo(s):
    n = int(s)
    # print('>>> n = %d' % n)
    # assert n != 0, 'n is zero!'
    # logging.info('n = %d' % n)
    pdb.set_trace()
    return 10 / n
def main():
    foo(0)
main()