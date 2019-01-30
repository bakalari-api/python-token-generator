#!/usr/bin/env python3

import hashlib
import base64
import datetime

import urllib.request
import xml.etree.ElementTree as ET
import ssl

import sys


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
res = urllib.request.urlopen('https://' + sys.argv[1] + '/login.aspx?gethx=' + sys.argv[2], context=ctx).read()
xml = ET.fromstring(res)

pwd = sys.argv[3]
ikod = xml[2].text
salt = xml[3].text
typ = xml[1].text
name = sys.argv[2]

hashpass = base64.b64encode(hashlib.sha512((salt+ikod+typ+pwd).encode('utf-8')).digest())

now = datetime.datetime.today().strftime('%Y%m%d')

rawtoken = '*login*' + name + '*pwd*' + hashpass.decode('utf-8') + '*sgn*ANDR' + now

token = base64.b64encode(hashlib.sha512(rawtoken.encode('utf-8')).digest()).decode('utf-8')
token = token.replace('\\', '_')
token = token.replace('/', '_')
token = token.replace('+', '-')

print(token)

