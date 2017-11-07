#!/usr/bin/env python
# -*- coding : utf-8 -*-
# @Date      : 2017-03-21 17:41:51
# @Author  : Sniper
# @Email     : haitao.lan@longsys.com

import wx

class SubclassDialog(wx.Dialog):
    """docstring for SubclassDialog"""
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, 'Dialog Subclass', size=(400, 100))
        # okButton = wx.Button(self, wx.ID_OK, "OK", pos=(15, 15))
        # okButton.SetDefault()
        # cancelButton = wx.Button(self, wx.ID_CANCEL, 'Cancel', pos=(115, 15))
        text = wx.StaticText(self, -1, label= "m", pos = wx.DefaultPosition, size= wx.DefaultSize, style = wx.ALIGN_CENTER, name = "staticText")
        text.SetForegroundColour('red')
        # static_text.SetForegroundColour('red')
        # input_text = wx.TextCtrl(self, -1, u'input', size=(175, -1))
        # input_text.SetInsertionPoint(0)

if __name__ == '__main__':
    app = wx.PySimpleApp()
    app.MainLoop()
    dialog = SubclassDialog()
    result = dialog.ShowModal()
    if result == wx.ID_OK:
        print "OK"
    else:
        print "Cancel"
    dialog.Destroy()


