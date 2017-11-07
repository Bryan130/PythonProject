#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-01-10 10:35:54
# @Author  : Liber (haitao.lan@longsys.com)
# @Link    : ${link}
# @Version : $Id$

import os,sys
import re
import urllib
import urllib2
base_url = 'http://www.baidu.com'
array_url = list()
pic_url = list()
inner_url = list()
def get_array_url(array_url,base_url):
  content = urllib.urlopen(base_url).read()
  array_url_a = re.findall(r'/rihan.*?.html',content)
  for url in array_url_a:
    url_a = 'xxx'+url
    #print url_a
    array_url.a
      url_b = re.sub(r'ahref=\\'','',url[0])
      # print url_b
      url_c = re.sub(r'\\'target','',url_b)
      url_c = 'http://xxx/'+re.sub(r'/.*/','',url_c)
      inner_url.append(url_c)
  del inner_url[1]
  # print inner_url
def get_pic_url(pic_url,inner_url,array_url):
  content = urllib.urlopen(array_url).read()
  pic_url_a = re.findall(r'center.*?.jpg',content)
  print 'bbbbbbbbb',len(pic_url_a)
  pic_url_a = re.findall(r'http://.*.jpg',pic_url_a[0])
  pic_url.append(pic_url_a[0])
  j=2
  for i in inner_url:
    jj = '/'+str(j)+'.jpg'
    pic = re.sub(r'/1.jpg',jj,pic_url_a[0])
    pic_url.append(pic)
    j = j+1
  del pic_url[-1]
  for i in pic_url:
    print i
def urlcallback(a,b,c):
  """
    call back function
    a,已下载的数据块
    b,数据块的大小
    c,远程文件的大小
  """
  print "callback"
  prec=100.0*a*b/c
  if 100 < prec:
    prec=100
  print "%.2f%%"%(prec,)
def download(img_url,file_num):
    for img in img_url:
      print img
      img_name = re.sub(r'http://.*/','',img)
      path = 'C:/'+str(file_num)+'/'+img_name
      urllib.urlretrieve(img,path,urlcallback)
get_array_url(array_url,base_url)
file_num = 3
#download(pic_url,file_num)
get_inner_url(url,inner_url)
get_pic_url(pic_url,inner_url,url)
'''
for url in array_url:
  print url
  # get_inner_url(url,inner_url)
 # get_pic_url(pic_url,inner_url)
  get_inner_url(url,inner_url)
  get_pic_url(pic_url,inner_url,url)
  download(pic_url,file_num)
  file_num = file_num+1
  del inner_url[:]
  del pic_url[:]
'''