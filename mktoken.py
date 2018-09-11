#!/usr/bin/env python2

import hashlib
import base64
import datetime

import urllib2
import xml.etree.ElementTree as ET

import sys

def credentials(domain, user):
    res = urllib2.urlopen('https://' + domain + '/login.aspx?gethx=' + user).read()
    xml = ET.fromstring(res)
    return {
        'res': xml[0].text,
        'typ': xml[1].text,
        'ikod': xml[2].text,
        'salt': xml[3].text,
        'name': user
    }

creds = credentials(sys.argv[1], sys.argv[2])

pwd = sys.argv[3]
ikod = creds['ikod']
salt = creds['salt']
typ = creds['typ']
name = creds['name']

hashpass = base64.b64encode(hashlib.sha512(salt+ikod+typ+pwd).digest())

now = datetime.datetime.today().strftime('%Y%m%d')

rawtoken = '*login*' + name + '*pwd*' + hashpass + '*sgn*ANDR' + now

token = base64.b64encode(hashlib.sha512(rawtoken).digest())
token = token.replace('\\', '_')
token = token.replace('/', '_')
token = token.replace('+', '-')

print(token)

