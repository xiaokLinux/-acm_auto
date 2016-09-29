# form and cookie
# -*-coding:utf-8 -*-
import sys,urllib,urllib2
import cookielib
import re

import cStringIO
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#模拟火狐的缓存
cookiejar=cookielib.MozillaCookieJar()
cookieSupport=urllib2.HTTPCookieProcessor(cookiejar)

#为了调试
httpHandler=urllib2.HTTPHandler(debuglevel=1)
httpsHandler=urllib2.HTTPSHandler(debuglevel=1)
opener=urllib2.build_opener(cookieSupport,httpsHandler)

#安装opener对象
urllib2.install_opener(opener)

loginpage="http://10.132.246.246/index"
PostUrl="http://10.132.246.246/index"
cookies=''
mytoken=''
##反crsf机制的令牌
vrifycodeUrl = "http://10.132.246.246/index"
file = urllib2.urlopen(vrifycodeUrl)
#pic= file.read()
# print "first view header:"
info=file.info()
for k,v in info.items():
     print "%s:%s" % (k,v)
mytoken=info.get("set-cookie")[10:42]
print "mytoken :",mytoken

print "##############################get sessionid#########################"
for c in cookiejar:
    print c

print len(cookiejar)
for index,cookie in enumerate(cookiejar):
    print "%d:%s" % (index,cookie)
    cookies=cookies+cookie.name+"="+cookie.value+";"

print "#####################cookie here###############################"
cookie=cookies[:-1]
print "cookies :",cookie


username="14211160137"
password="12345"
#表单数据
postData={
        'rfmiddlewaretoken':mytoken,
        'username': username,
        'password': password
}
#报头
headers={
        'Host': '10.132.246.246',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding':'gzip, deflate',
        'DNT':'1',
        'Referer':'http://10.132.246.246/index/',
        'Cookie': cookies,
        'Connection': 'Keep-Alive',
        'Upgrade-Insecure-Requests': '1',
}
data=urllib.urlencode(postData)
print "###########################form data###################################"
print data
print "###########################form data###################################"
request=urllib2.Request(PostUrl,data,headers)
try:
    response=urllib2.urlopen(request)
    status=response.getcode()
    print  status
    # info = response.info()
    # for k, v in info.items():
    #     print "%s:%s" % (k, v)
except urllib2.HTTPError,e:
    print e.code

f=response.read()
outfile=open("rel_ip.txt","w")
print >> outfile ,"%s" % (f)

info=response.info()

print info

#测试是否成功
testurl="http://10.132.246.246/course/mycourse/"
try:
    response=urllib2.urlopen(testurl)
except  urllib2.HTTPError,e:
    print e.code

f=response.read().decode("utf-8").encode("utf-8")
outfile=open("out_ip.txt","w")
print >> outfile , "%s" % (f)

tag="Java".encode("utf-8")
if re.search(tag,f):
    print 'Logged in successfully!'
else:
    print 'Logged in failed,check result.html file for details'

response.close()