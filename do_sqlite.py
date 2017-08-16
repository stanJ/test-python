#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sqlite3
from contextlib import closing

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)
with sqlite3.connect(db_file) as conn:
    with closing(conn.cursor()) as cursor:
        cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
        cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
        cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
        cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
    conn.commit()

def get_score_in(low, high):
    with sqlite3.connect(db_file) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(r'select name from user where score >= ? and score <= ? order by score asc', (low, high))
            values = cursor.fetchall()
    return [x[0] for x in values]

if __name__ == '__main__':
    assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
    assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
    assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)