

import sys,urllib2,urllib


def addGETdata(url,data):
    return url+'?'+urllib.urlencode(data)
req1=urllib2.Request("http://10.132.246.246")
#fd1=urllib2.urlopen(req1)
opener=urllib.FancyURLopener()
opener.addheader('Connection','keep-alive')
fd1=opener.open("http://10.132.246.246")
print "info :"
info=fd1.info()
for k,v in info.items():
    print "%s:%s" % (k,v)

print "The most important : %s" ,info.get("set-cookie")
#print type(info.get("set-cookie"))
print "the next important : %s" , info.get("set-cookie")[10:42]  #token here
mytoken=info.get("set-cookie")[10:42]

myurl="http://10.132.246.246/user/logincheck/"
#mydata=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0'),
#       ('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),('Accept-Language','zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'),
#      ('Accept-Encoding','gzip, deflate'),('DNT','1'),('Referer','http://10.132.246.246/index/'),
#     ('Cookie','REMEMBERME=VG9weGlhXFNlcnZpY2VcVXNlclxDdXJyZW50VXNlcjpNamMxTURJMU5qUTFRSEZ4TG1OdmJRPT06MTQ3NTA1ODU2OToyOTMyODZhZDI5NTRkMzZhZGUxNzJhNjYyYTVlZTY3YWMxZjFhYWU3ZDVlMjYxZDY1ZWZmZDFjNGE0YjZmM2Y1; csrftoken=oNsakZuCVPc9cmCTPVm4ksJo8ypSVLor; sessionid=e160f64f3b12934f88d3cfdc02a9b48d')]
mydata=[('csrfmiddlewaretoken',mytoken),('username','14211160137'),('password','12345')]

url=addGETdata(myurl,mydata)

#print "Using URL",url
#req=urllib2.Request(url)
#fd=urllib2.urlopen(req)
fd = opener.open("http://10.132.246.246/user/logincheck/")
nfo=fd.info()
for k,v in info.items():
    print "%s:%s" % (k,v)



