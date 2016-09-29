#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys,urllib2,getpass

class TerminalPassword(urllib2.HTTPPasswordMgr):
    def find_user_password(self, realm, authuri):
        retval=urllib2.HTTPPasswordMgr.find_user_password(self,realm,authuri)

        if retval[0]==None and retval[1]==None:
            sys.stdout.write("Login required for %s at %s\n" % (realm,authuri))
            sys.stdout.write("username: ")
            username=sys.stdin.readline().rstrip()
            password=getpass.getpass().rstrip()
            return (username,password)
        else:
            return retval

req=urllib2.Request(b"http://10.132.246.246/index") #请求
opener=urllib2.build_opener(urllib2.HTTPBasicAuthHandler(TerminalPassword()))
#d=urllib2.urlopen(req)
fd=opener.open(req)
print 'next is header of : %s' % fd.geturl()
info=fd.info()
for key,value in info.items():
    print "%s=%s" % (key,value)

#while True:
 #   data=fd.read(1024)
  #  if not len(data):
   #     break
    #sys.stdout.write(data)



