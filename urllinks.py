# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

proc = input("Enter Count: ")
proc = int(proc)

pos = input("Enter Position: ")
pos = int(pos)
url = input('Enter - ')

for i in range (0,proc):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    n = tags[pos - 1]

    data = n.decode()
    ns = re.findall('href="(.+)"',data)
    print(ns)

    url = ns[0]
