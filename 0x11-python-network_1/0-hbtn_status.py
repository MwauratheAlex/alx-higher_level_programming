#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    f = response.read()
    print('Body response:')
    print('\t- type:', type(f))
    print('\t- content:', f)
    print('\t- utf8 content:', f.decode('utf-8'))
