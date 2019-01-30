#!/usr/bin/env python3

import hashlib
import base64
import datetime

import urllib.request
import xml.etree.ElementTree as ET
import ssl

def generate_token(domain, user, password):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    res = urllib.request.urlopen('https://' + domain + '/login.aspx?gethx=' + user, context=ctx).read()
    xml = ET.fromstring(res)

    ikod = xml[2].text
    salt = xml[3].text
    typ = xml[1].text

    hashpass = base64.b64encode(hashlib.sha512((salt+ikod+typ+password).encode('utf-8')).digest())

    now = datetime.datetime.today().strftime('%Y%m%d')

    rawtoken = '*login*' + user + '*pwd*' + hashpass.decode('utf-8') + '*sgn*ANDR' + now

    token = base64.b64encode(hashlib.sha512(rawtoken.encode('utf-8')).digest()).decode('utf-8')
    token = token.replace('\\', '_')
    token = token.replace('/', '_')
    token = token.replace('+', '-')

    return token

if __name__ == "__main__":
    import sys
    print(generate_token(sys.argv[1], sys.argv[2], sys.argv[3]))