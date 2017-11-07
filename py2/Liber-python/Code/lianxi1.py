# -*- coding:utf-8 -*-
'''
Created on 2016年11月28日

@author: v_tjietang
'''
import os
import time

x = '--------------------------------'
y = '--------------------------------'
dizhi = raw_input("请输入目录地址:")

if os.path.exists(dizhi.decode('utf-8')) == False:
    print "地址错误或不存在"

        
elif os.path.isdir(dizhi.decode('utf-8')) == False:
    a = os.stat(dizhi)
    amtime = a.st_mtime
    alt = time.localtime(amtime)
    amlt = time.strftime('%Y/%m/%d %H:%M',alt)
    print '%10d%20s'%(a.st_size,amlt)
else:
    list = os.listdir(dizhi.decode('utf-8'))
    for l in list:
#         print l
        mulu = dizhi.decode('utf-8') + "\\" + l
#         print mulu
        a = os.stat(mulu)
#         print l,a.st_size
        amtime = a.st_mtime
        alt = time.localtime(amtime)
        amlt = time.strftime('%Y/%m/%d %H:%M',alt)
        if os.path.isdir(mulu) == True:
            mulu_list = os.listdir(mulu.decode('utf-8'))
            for mulu_l in mulu_list:
                m_l = mulu + '\\' + mulu_l
                b = os.stat(m_l)
                c = os.stat(mulu) #文档的信息
                bmtime = b.st_mtime
                blt = time.localtime(bmtime)
                bmt = time.strftime('%Y/%m/%d %H:%M',blt)
                     
                print l + '%6d%20s'%(a.st_size,amlt) + '\n'+ x +'\n%12s%8d%20s'%(mulu_l,b.st_size,bmt)+'\n'+ y
                
        else:
            
            
            print l+'%8d%22s'%(a.st_size,amlt)
            
            
        
#     else:
#         mulu1 = dizhi + "\\" + l
#         mulu_list = os.listdir(mulu1.decode('utf-8'))
#         for mulu_l in mulu_list:
#             m_l = mulu1 + '\\' + mulu_l
#             b = os.stat(m_l)
#             print mulu_l,b.st_size
#         else:
            
#     list =  os.listdir(dizhi.decode("utf-8"))
#     print list
# for l in list:
#     a = os.stat(l)
#     print a.st_size 
# print os.path.isfile("D:\\test.txt")