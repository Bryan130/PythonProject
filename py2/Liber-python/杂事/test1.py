#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Date      : 2017-03-23 11:28:37
# @Author  : Sniper
# @Email     : haitao.lan@longsys.com

import wx
import time
#import winsound

class ClockFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Clock',size=(260,130))
        self.SetBackgroundColour('White')
        self.initialTime()

        self.createTextCtrl()
        self.createButton()
        self.bindEvent()
        self.createTimer()
        self.clocktimer = None
    def initialTime(self):
        self.filename = 'init'
        file = open(self.filename,'r')
        self.clocktime = file.readlines()[0]
        file.close()

    def createTextCtrl(self):
        self.cur_time = wx.StaticText(self,label=u'当前时间:',pos=(0,0))
        w,self.h = self.cur_time.GetClientSize()
        self.time_label = wx.StaticText(self,pos=(w,0))
        self.conf_label = wx.StaticText(self,label=u'设置闹钟时间:',pos=(0,2*self.h))
        w = self.conf_label.GetClientSize()[0]
        self.set_time = wx.TextCtrl(self,pos=(w+5,2*self.h))
        w += self.set_time.GetClientSize()[0]
        self.set_time.SetValue(self.clocktime)

    def createButton(self):
        self.button = wx.Button(self,label=u'确定',pos=(0,4*self.h))
        self.stop_btn = wx.Button(self,label=u'停止',pos=(80,4*self.h))
        self.reset_btn = wx.Button(self,label=u'重设',pos=(160,4*self.h))

    def bindEvent(self):
        self.button.Bind(wx.EVT_BUTTON,self.OnOK)
        self.stop_btn.Bind(wx.EVT_BUTTON,self.OnStop)
        self.reset_btn.Bind(wx.EVT_BUTTON,self.OnReset)
        self.Bind(wx.EVT_CLOSE,self.OnClose)

    def createTimer(self):
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER,self.OnRefresh,self.timer)
        self.timer.Start(1000)

    def OnRefresh(self,event):
        t = time.localtime(time.time())
        self.st =time.strftime("%H:%M:%S",t)
        self.time_label.SetLabel(self.st)

    def OnOK(self,event):
        self.set_time.SetEditable(False)
        self.clocktime =  self.set_time.GetValue()
        self.setclocktime2file()
        self.clocktimer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER,self.OnClock,self.clocktimer)
        self.clocktimer.Start(1000)

    def setclocktime2file(self):
        file = open(self.filename,'w')
        file.write(self.set_time.GetValue())
        file.close()

#    def OnClock(self,event):
#        if self.st == self.clocktime :
#            self.clocktimer.Stop()
#            for i in range(20):
#                winsound.Beep(1000,200)

    def OnClock(self,event):
        if self.st == self.clocktime :
            #self.clocktimer.Stop()
            self.sound = wx.Sound('clock.wav')
            self.sound.Play()

    def OnStop(self,event):
        if self.sound.IsOk():
            self.sound.Stop()

    def OnReset(self,event):
        if not self.set_time.IsEditable():
            self.set_time.SetEditable(True)

    def OnClose(self,event):
        self.timer.Stop()
        if self.clocktimer:
            self.clocktimer.Stop()
        self.Destroy()


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = ClockFrame(parent=None,id=-1)
    frame.Show()
    app.MainLoop()
