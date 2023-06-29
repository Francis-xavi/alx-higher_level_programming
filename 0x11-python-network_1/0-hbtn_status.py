#!/usr/bin/python3
""" what is my status
"""

if _name_ == "_main_":
    from urlib import request

    with request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
    print('Body response:')
    print('\t- type: {}'.format(type(html)))
    print('\t- content: {}'.format(html))
    print('\t- utf8 content: {}'.format(html.decode('utf-8')))
