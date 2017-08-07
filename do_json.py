#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
s = Student('Stan', 25, 99)
json_str = json.dumps(s, default=lambda obj: obj.__dict__)
print(json_str)
s1 = json.loads(json_str, object_hook=dict2student)
print(s1)