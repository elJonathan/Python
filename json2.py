import json
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
url = urllib.request.urlopen(address, context=ctx)
u = url.read()
data = json.loads(u)
#print(data)
n = data['comments']
#print(n)
s = 0
for i in n:
    z = i['count']
    s = s + z

print(s)
