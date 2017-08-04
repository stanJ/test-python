#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
    def run():
        print('animal is running')
class Dog(Animal):
    def run():
        print('dog is running')
class Husky(Dog):
    def run():
        print('husky is running')
class MyDog(object):
    def __len__(self):
        return 100
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x