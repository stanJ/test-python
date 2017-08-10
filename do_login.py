#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json, os, hashlib
from do_register import get_md5

def login(username, password):
    with open('db.json', 'r') as f:
        db = json.load(f)
    hash = get_md5(username, password)
    if db[username] == hash:
        print('登陆成功')
    else:
        print('用户名或密码错误')

def toLogin():
    print('欢迎登陆')
    username = input('请输入用户名: ')
    password = input('请输入密码: ')
    login(username, password)

if __name__ == '__main__':
    toLogin()