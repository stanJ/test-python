#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64

def safe_base64_decode(s):
    if isinstance(s, bytes):
        s = s.decode('utf-8')
    return base64.urlsafe_b64decode(s + '=' * ((4 - len(s) % 4) % 4))

if __name__ == '__main__':
    assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
    assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
    assert b'abcd\x0f\xbe' == safe_base64_decode(b'YWJjZA--'), safe_base64_decode('YWJjZA--')
