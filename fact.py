#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fact(n):
    '''
    用来计算阶乘
    >>> fact(0)
    1
    >>> fact(-1)
    Traceback (most recent call last):
        ...
    ValueError
    >>> fact(3)
    6
    '''
    if n < 0:
        raise ValueError()
    if n == 0:
        return 1
    return n * fact(n-1)
if __name__ == '__main__':
    import doctest
    doctest.testmod()