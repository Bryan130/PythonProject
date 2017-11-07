#!/usr/bin/env python
# -*- coding : utf-8 -*-
# @Date      : 2017-02-17 18:10:34
# @Author  : Liber (haitao.lan@longsys.com)
# @Link       : http://.com


import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1


html = getHtml("http://tieba.baidu.com/p/2460150866")

print getImg(html)

