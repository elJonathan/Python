import urllib.request, urllib.parse, urllib.error

fh = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fh:
    print(line.decode().strip())
