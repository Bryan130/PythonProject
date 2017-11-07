#!/usr/bin/env python
# -*- coding : utf-8 -*-
# @Date      : 2017-03-21 19:54:12
# @Author  : Sniper
# @Email     : haitao.lan@longsys.com

import wx


class StaticTextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u'这是Static Text Example', size=(400, 300))

        box_sizer = wx.WrapSizer()
        self.SetAutoLayout(True)
        self.SetSizer(box_sizer)

        ########## Label ##########
        static_text = wx.StaticText(self, -1, u'这是个Label', style=wx.ALIGN_CENTER)
        static_text.SetForegroundColour('red')  #颜色
        wx_font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.BOLD)
        static_text.SetFont(wx_font)
        box_sizer.Add(static_text)

        ########## 单行文本框 ##########
        input_text = wx.TextCtrl(self, -1, u'input', size=(175, -1))
        input_text.SetInsertionPoint(0)
        box_sizer.Add(input_text)

        ########## 多行文本框 ##########
        self.area_text = wx.TextCtrl(self, -1, u'textArea多行文本，可Ctrl+A', size=(200, 100),
                                     style=(wx.TE_MULTILINE | wx.TE_AUTO_SCROLL | wx.TE_DONTWRAP))
        self.area_text.SetInsertionPoint(0)
        self.area_text.Bind(wx.EVT_KEY_UP, self.OnSelectAll)
        box_sizer.Add(self.area_text)





        ########## 富文本框 ##########
        self.rich_text = wx.TextCtrl(self, -1, u'rich富文本', size=(200, 100),
                                     style=(wx.TE_MULTILINE | wx.TE_AUTO_SCROLL | wx.TE_DONTWRAP | wx.TE_RICH2))
        self.rich_text.SetInsertionPoint(0)
        #设置文本样式  len(rich_text.GetValue())
        f = wx.Font(18, wx.ROMAN, wx.ITALIC, wx.BOLD, True)  #创建一个字体
        self.rich_text.SetStyle(0, self.rich_text.GetLastPosition(), wx.TextAttr("red", "green", f))

        box_sizer.Add(self.rich_text)

    #自定义 多行文本框  全选
    def OnSelectAll(self, event):
        if (event.GetKeyCode() == 65 and event.ControlDown()):
            self.area_text.SelectAll()


if __name__ == '__main__':
    root = wx.App()
    frame = StaticTextFrame()
    frame.Show()
    root.MainLoop()
