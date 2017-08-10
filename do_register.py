#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json, os, hashlib

dbpath = 'db.json'
def register(username, password):
    db = {}
    if os.path.exists(dbpath):
        with open(dbpath, 'r') as f:
            db = json.load(f)
    db[username] = get_md5(username, password)
    with open(dbpath, 'w') as f:
        json.dump(db, f)

def get_md5(username, password):
    pw = password + username + 'the-Salt'
    md5 = hashlib.md5()
    md5.update(pw.encode('utf-8'))
    return md5.hexdigest()

def toRegister():
    while True:
        username = input('请输入用户名: ')
        password = input('请输入密码: ')
        register(username, password)

if __name__ == '__main__':
    toRegister()