#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64

def safe_base64_decode(s):
    return base64.urlsafe_b64decode(s + '=' * ((4 - len(s) % 4) % 4))


if __name__ == '__main__':
    s1 = 'YWJj+/=='
    s2 = 'YWJj-_'
    print(safe_base64_decode(s1))
    print(safe_base64_decode(s2))