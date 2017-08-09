#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
re_email = re.compile(r'^([a-zA-Z0-9][\w\.]*[a-zA-Z0-9])@([0-9a-z]+\.[a-z]+)$')
re_name = re.compile(r'^\<(.*)\>\s*([a-zA-Z0-9][\w\.]*[a-zA-Z0-9])@([0-9a-z]+\.[a-z]+)$')