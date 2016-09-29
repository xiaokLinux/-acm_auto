import sys,urllib,urllib2
import cookielib
import re
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj), urllib2.HTTPHandler)
f = opener.open("http://10.132.246.246")
html = f.read()

print "The cookies are:"
for cookie in cj:
    print cookie

for i in range(10):
    f = opener.open("http://10.132.246.246")
    html = f.read()

print "The cookies are:"
for cookie in cj:
    print cookie