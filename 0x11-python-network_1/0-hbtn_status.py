#!/usr/bin/python3
""" what is my status
"""

if _name_ == "_main_":
    request = urlib.request.Request("https://alx-intranet.hbtn.io/status")
    with urlib.request.urlopen(request) as response:
        body = response.read()
        print("body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
