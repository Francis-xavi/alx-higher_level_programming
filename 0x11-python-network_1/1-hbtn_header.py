#!/usr/bin/python3
"""displays the X-request_Id header variable of a request to a given URL.
Usage: ./1-hbtn_header.py <URL>
"""
import sys
import urlib.request


if _name_=="_main_":
    url = sys.argv[1]

    request = urlib.request.Requet(url)
    with urlib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Requesst-Id"))
