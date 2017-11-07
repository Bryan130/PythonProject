#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Date     :2017-03-16 19:51:14
# @Author  :Liber (haitao.lan@longsys.com)
# @Link       :http://.com


#引入wx模块
import wx

#定义一个wx 的class
class sayHello(wx.App):

    def OnInit(self):
        frame = wx.Frame(parent=None,title="Hello wxPython")
        frame.Show()
        return True


app = sayHello()
#主循环
app.MainLoop()
