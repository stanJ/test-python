#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from xml.parsers.expat import ParserCreate
import json

data = {}
textlist = []
class WeatherSaxHandler(object):
    def start_element(self, name, attr):
        if not name in data:
            data[name] = []
        data[name].append({'attr' : attr}) 
    
    def char_data(self, text):
        textlist.append(text)
    
    def end_element(self, name):
        global textlist
        str = ''.join(textlist)
        data[name][-1]['text'] = str
        textlist = []


def parse_weather(xml):
    handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml)
    location = data['yweather:location']
    forecast = data['yweather:forecast']
    return {
        'city': location[0]['attr']['city'],
        'country': location[0]['attr']['country'],
        'today': {
            'text': forecast[0]['attr']['text'],
            'low': forecast[0]['attr']['low'],
            'high': forecast[0]['attr']['high'],
        },
        'tomorrow': {
            'text': forecast[1]['attr']['text'],
            'low': forecast[1]['attr']['low'],
            'high': forecast[1]['attr']['high'],
        },
    }
    #可将数据写入json文件
    # with open('weather_data.json', 'w') as f:
    #     json.dump(data, f)

if __name__ == '__main__':
    from do_weather_xml import getWeatherXML
    xml = getWeatherXML()
    d = parse_weather(xml)
    print(str(d))