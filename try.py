#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
class FooError(ValueError):
    pass
def foo(n):
    print('try...')
    x = int(n)
    if x == 0:
        raise ValueError('invalid value: %s' % n)
    r = 10 / x
    print('result:', r)
    return r
def bar():
    n = input('请输入除数：')
    return foo(n) * 2
def main():
    try:
        bar()
    except ZeroDivisionError as e:
        logging.exception(e)
        raise
    except ValueError as e:
        print('heheh: ')
        logging.exception(e)
        # print(e)
        # raise
    except Exception as e:
        print('Exception: ')
        raise
    else:
        print('no error!')
    finally:
        print('finally...')
    print('END')
main()