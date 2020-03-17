#!/usr/bin/env python3

import base64
import datetime
import hashlib
import re
import ssl
import urllib.request
from urllib.parse import urlencode, urlparse
from xml.etree import ElementTree


class InvalidUsername(Exception):
    pass


def generate_token(url, username, password):
    """Generates token for authentication with Bakaláři server

    Requests hashing salt for the `username` from the endpoint `url`. Then generates
    a string which includes the `password` and server-provided salt. This string is
    hashed and included in new string, along with username and current date. This
    string is hashed again and encoded with base64.

    :param str url: The URL used to get salt to generate token. Including
      /login.aspx, but not /next/, even though the UI lives there. Something like
      `https://subdomain.skola.cz/bakalari/login.aspx`

    :param str username: Username

    :param str password: Password

    :returns: The generated token, valid for today
    :rtype: str

    :raises InvalidUsername: if the server indicates it doesn't recognize the username
    """
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    res = urllib.request.urlopen(
        url + "?" + urlencode({"gethx": username}), context=ctx
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

    rawtoken = (
        "*login*" + username + "*pwd*" + hashpass.decode("utf-8") + "*sgn*ANDR" + now
    )

    token = base64.b64encode(hashlib.sha512(rawtoken.encode("utf-8")).digest()).decode(
        "utf-8"
    )
    token = token.replace("\\", "_")
    token = token.replace("/", "_")
    token = token.replace("+", "-")

    return token


def process_url(url):
    """Tries to make `url` suitable for :py:func:`generate_token()`

    Removes everything from `url` except host and path, and removes `/login.aspx` or
    `/next/*.aspx` from the path if present. Then appends `https://` and
    `/login.aspx`. This should work for most cases.

    :param str url: The url to process

    :returns: The processed url
    :rtype: str
    """
    p = urlparse(url)
    path = p.path

    # this magic excludes /login.aspx or /next/*.aspx
    match = re.search(r"^(.*?)(?:(?:/next/[a-z]+\.aspx)|(?:/login.aspx))$", path)
    if match is not None:
        path = match.group(0)

    return "https://" + p.netloc + path + "/login.aspx"


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
    parser.add_argument(
        "-k",
        "--keep-url",
        action="store_false",
        default=True,
        dest="process_url",
        help="Nepokoušet se upravit URL. Argument url by tedy už měl být něco jako https://subdomena.skola.cz/bakalari/login.aspx",
    )
    args = parser.parse_args()

    url = process_url(args.url) if args.process_url else args.url

    if "pwd" in args:
        pwd = args.pwd
    else:
        pwd = getpass("Heslo: ")
    print(generate_token(url, args.username, pwd))


if __name__ == "__main__":
    cli()
