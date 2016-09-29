
import sys,urllib2,urllib

mydata=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0'),
        ('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),('Accept-Language','zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'),
        ('Accept-Encoding','gzip, deflate'),('DNT','1'),('Referer','http://10.132.246.246/index/'),
        ('Cookie','REMEMBERME=VG9weGlhXFNlcnZpY2VcVXNlclxDdXJyZW50VXNlcjpNamMxTURJMU5qUTFRSEZ4TG1OdmJRPT06MTQ3NTA1ODU2OToyOTMyODZhZDI5NTRkMzZhZGUxNzJhNjYyYTVlZTY3YWMxZjFhYWU3ZDVlMjYxZDY1ZWZmZDFjNGE0YjZmM2Y1; csrftoken=oNsakZuCVPc9cmCTPVm4ksJo8ypSVLor; sessionid=e160f64f3b12934f88d3cfdc02a9b48d'),
        ('Content-Type','application/x-www-form-urlencoded'),('Content-Length','88'),('rfmiddlewaretoken','oNsakZuCVPc9cmCTPVm4ksJo8ypSVLor&username=14211160137&password=12345')]
myurl="http://10.132.246.246/user/logincheck/"

data=urllib.urlencode(mydata)
req=urllib2.Request(myurl)
fd=urllib2.urlopen(req,data)
while True:
    data=fd.read(1024)
    if not len(data):
        break
    sys.stdout.write(data)