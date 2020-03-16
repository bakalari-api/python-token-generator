#!/usr/bin/env python3

import base64
import datetime
import hashlib
import ssl
import urllib.request
from xml.etree import ElementTree


class InvalidUsername(Exception):
    pass


def generate_token(url, user, password):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    res = urllib.request.urlopen(
        "https://{}/login.aspx?gethx={}".format(url, user), context=ctx
    ).read()
    xml = ElementTree.fromstring(res)

    if xml[0].text == "02":
        raise InvalidUsername("Neplatné uživatelské jméno")

    ikod = xml[2].text
    salt = xml[3].text
    typ = xml[1].text

    hashpass = base64.b64encode(
        hashlib.sha512((salt + ikod + typ + password).encode("utf-8")).digest()
    )

    now = datetime.datetime.today().strftime("%Y%m%d")

    rawtoken = "*login*" + user + "*pwd*" + hashpass.decode("utf-8") + "*sgn*ANDR" + now

    token = base64.b64encode(hashlib.sha512(rawtoken.encode("utf-8")).digest()).decode(
        "utf-8"
    )
    token = token.replace("\\", "_")
    token = token.replace("/", "_")
    token = token.replace("+", "-")

    return token


def cli():
    import argparse
    from getpass import getpass

    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="URL Bakalářů (např. subdomena.skola.cz/bakalari)")
    parser.add_argument("username", help="Uživatelské jméno")
    parser.add_argument(
        "pwd",
        help="Heslo (volitelné, pokud nezadáno, bude vyžádáno schovaným vstupem)",
        nargs="?",
        default=argparse.SUPPRESS,
    )
    args = parser.parse_args()
    if "pwd" in args:
        pwd = args.pwd
    else:
        pwd = getpass("Heslo: ")
    print(generate_token(args.url, args.username, pwd))


if __name__ == "__main__":
    cli()
