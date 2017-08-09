#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime, timezone, timedelta
import re

re_timezone = re.compile(r'^UTC(\+|\-0[0-9]|1[0-2]|[0-9])\:00$')
def to_timestamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    m_timezone = re_timezone.match(tz_str)
    hours = int(m_timezone.group(1))
    tz = timezone(timedelta(hours=hours))
    dt = dt.replace(tzinfo=tz)
    ts = dt.timestamp()
    return ts

if __name__ == '__main__':
    ts = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
    print(ts)
    

    