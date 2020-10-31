import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('comments')
n = tags[0]
#print(n)

o = n.decode()
print(o)
sa = 0
stuff = ET.fromstring(o)
lst = stuff.findall('comment')
for item in lst:
    num = item.find('count').text
    num = int(num)
    sa = sa + num
print(sa)
