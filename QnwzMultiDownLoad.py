# -*- coding: utf-8 -*-

import urllib2
import re
import os
def Download(url,output):
    print url
    print "downloading..."
    try:
        response = urllib2.urlopen(url)
        resourceFile = open(output,"wb")
        resourceFile.write(response.read())
        resourceFile.close()
    except Exception,e:
        output = open('./thefile.txt', "a")
        output.write("\n" + url)
        output.close()
    

def DownloadMP3(url,ext = "mp3",output = "./"):
    #1.domain
    index = url.rfind("/");
    domain = url[0:index+1];
    
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    #2.content
    content = response.read()
    #print content
    #3.resource
    mode = '\"([^\"]+'+ext+')\"'
    pattern = re.compile(mode)
    strMatch = pattern.findall(content)
    size = len(strMatch)
    targetDir = output + url.split("/")[6] + url.split("/")[7];
    try:
        os.makedirs(targetDir)
    except Exception,e:
        pass
    for i in range(0,size,1):
        fileName = strMatch[i]
        partIndex = fileName.rfind('/')
        if fileName.startswith('http://'):
            fileOutput = targetDir +fileName[partIndex:]
            print fileOutput
            Download(fileName,fileOutput)
    
def Action(url):

    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    content = response.read()
    mode = '\'([^\']+'+"html"+')\''
    pattern = re.compile(mode)
    strMatch = pattern.findall(content)
    size = len(strMatch)
    lenth = 0
    for i in range(0,size,1):
        one = strMatch[i]
        if not (one.startswith("/html/yinlegushihui/magazine/2016") or
			one.startswith("/html/yinlegushihui/magazine/2015") or
			one.startswith("/html/yinlegushihui/magazine/2014") or 
            one.startswith("/html/yinlegushihui/magazine/2013") or
            one.startswith("/html/yinlegushihui/magazine/2012") or 
            one.startswith("/html/yinlegushihui/magazine/2011")):
            continue
        lenth = lenth + 1
	print "amount:" + str(lenth)
    for i in range(0,size,1):
        one = strMatch[i]
        if not (one.startswith("/html/yinlegushihui/magazine/2016") or
			one.startswith("/html/yinlegushihui/magazine/2015") or
			one.startswith("/html/yinlegushihui/magazine/2014") or 
            one.startswith("/html/yinlegushihui/magazine/2013") or
            one.startswith("/html/yinlegushihui/magazine/2012") or 
            one.startswith("/html/yinlegushihui/magazine/2011")):
            continue
        UrlItem = "http://www.qnwz.cn" + one
        DownloadMP3(UrlItem)
        print "remain:"  + str(lenth - i - 1)

if __name__=='__main__':
    print "download"
    url = "http://www.qnwz.cn/html/yinlegushihui/magazine/list_259_3.html";
    Action(url);
    
