#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import poplib
from email.parser import Parser

email = input('Email: ')
password = input('Password: ')
pop3_server = input('POP3 server: ')

server = poplib.POP3_SSL(pop3_server, port=995)
server.set_debuglevel(1)
print(server.getwelcome().decode('utf-8'))

server.user(email)
server.pass_(password)

print('Message: %s. Size: %s' % server.stat())
resp, mails, octets = server.list()
print(mails)

index = len(mails)
resp, lines, octets = server.retr(index)

msg_content = b'\r\n'.join(lines).decode('utf-8')
msg = Parser().parsestr(msg_content)
print(msg)
server.quit()
