#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from html.parser import HTMLParser
import urllib.request

response = urllib.request.urlopen('https://www.python.org/events/python-events/')
class PythonEvent(HTMLParser):
    def __init__(self):
        super(PythonEvent, self).__init__()
        self.key = 0
        self.location_key = 0
        self.event_list = []
        self.event_tmp = []
    def handle_starttag(self, tag, attrs):
        if attrs:
            if attrs[0][1] == 'event-title' or tag == 'time':
                self.key = 1 # self.key=1表示data需要保存
            if attrs[0][1] == 'event-location':
                self.key = 1
                self.location_key =1 # self.location_key=1表示单个data信息结尾

    def handle_data(self, data):
        if self.key:
            self.event_tmp.append(data)
        if self.location_key:
            self.event_list.append(self.event_tmp) # event_tmp保存进list并重置
            self.event_tmp = []

    def handle_endtag(self, tag):
        self.key = 0
        self.location_key = 0

event = PythonEvent()
event.feed(response.read().decode('utf-8'))
for i in event.event_list:
    print(i)