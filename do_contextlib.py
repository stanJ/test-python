#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# class Query(object):

#     def __init__(self, name):
#         self.name = name

#     def __enter__(self):
#         print('Begin')
#         return self

#     def __exit__(self, exc_type, exc_value, traceback):
#         if exc_type:
#             print('Error')
#         else:
#             print('End')
    
#     def query(self):
#         print('Query info about %s...' % self.name)

from contextlib import contextmanager

class Query(object):
    def __init__(self, name):
        self.name = name
    
    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')

@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('</%s>' % name)




if __name__ == '__main__':
    # with create_query('Bob') as q:
    #     q.query()
    
    # with tag('h1'):
    #     print('hello')
    #     print('world')

    from contextlib import closing
    # @contextmanager
    # def closing(thing):
    #     try:
    #         yield thing
    #     finally:
    #         thing.close()
    from urllib.request import urlopen

    with closing(urlopen('https://www.python.org')) as page:
        for line in page:
            print(line)