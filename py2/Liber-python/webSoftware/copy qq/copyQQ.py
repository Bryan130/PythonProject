#!/usr/bin/env python
# -*- coding : utf-8 -*-
# @Date      : 2017-03-21 19:37:37
# @Author  : Sniper
# @Email     : haitao.lan@longsys.com

from win32gui import CreateRoundRectRgn, GetWindowRect
from winxpgui import SetWindowRgn
import wx
from configer import Cfg
from hooks.skinhook import SkinButton, SkinMinSizeButton, SkinCloseButton, SkinInput, InstallSkin
from tools.common import  MessageBox
import wx.lib.hyperlink as hyperlink
from ui.dialogs.setttingdlg import SettingDlg
from uilogic.frameinf import ILoginUIHandler
from ui.image import ImageCenter

UIHandler=ILoginUIHandler
class LoginFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'E时代安全电子文档V2.0',wx.DefaultPosition, (380, 280),style=wx.NO_BORDER|wx.FRAME_SHAPED)
        self.panel=LoginPanel(self,(380,280))
        self.SetDefaultItem(self.panel.btnLogin)

        self.panel.Bind(wx.EVT_MOTION,self.OnMouseMove)
        self.panel.Bind(wx.EVT_LEFT_DOWN, self.OnMouseDown)
        self.panel.Bind(wx.EVT_LEFT_UP,self.OnMouseUp)

        self.delta = (0,0)
        self.SetBalloonShape()
        self.Center()

    def OnMouseDown(self,event):
        self.panel.CaptureMouse()
        x, y =  self.ClientToScreen(event.GetPosition())
        originx, originy = self.GetPosition()
        dx = x - originx
        dy = y - originy
        self.delta = ((dx, dy))

    def OnMouseUp(self, evt):
        if self.panel.HasCapture():self.panel.ReleaseMouse()

    def OnMouseMove(self, evt):
        if evt.Dragging() and evt.LeftIsDown():
            x, y = self.ClientToScreen(evt.GetPosition())
            fp = (x - self.delta[0], y - self.delta[1])
            self.Move(fp)


    def SetBalloonShape(self):
        left,top,right,bottom=GetWindowRect(self.GetHandle())
        hrgn=CreateRoundRectRgn(left,top,right,bottom,5,5)
        SetWindowRgn(self.GetHandle(),hrgn,True)

#       width, height = self.GetSize()
#       bmp = wx.EmptyBitmap(width,height)
#       dc = wx.BufferedDC(None, bmp)
#       dc.DrawRoundedRectangle(0, 0, width-1, height-1,3)
#       dc.EndDrawing()
#       self.hasShape = self.SetShape(wx.RegionFromBitmapColour(bmp, wx.Colour(0,0,0)))

    def SaveName(self):
        Cfg.c_lastname=self.panel.username \
        if Cfg.bool(Cfg.c_savename) else ''

    def ClearPasswrod(self):
        self.panel.pwdText.SetValue('')


class LoginPanel(wx.Panel):

    def __init__(self,parent,size):
        wx.Panel.__init__(self,parent,-1,size=size)

        self.bgBmp =ImageCenter.WLoginBgBmp.GetBitmap()
        self.logoBmp=ImageCenter.WLogoBmp.GetBitmap()

#       self.btnLogin=wx.Button(self, -1, '登录')
#       self.btnSetting=wx.Button(self,-1,  '设置')

        self.btnLogin=SkinButton(self, -1, '登录')
        self.btnLogin.SetDefault()
        self.btnSetting=SkinButton(self,-1,  '设置')

        self.minBth=SkinMinSizeButton(self)
        self.closeBth=SkinCloseButton(self)

        self.minBth.BindMinSize(parent)
        self.closeBth.BindClose(parent)

        self.nameText=SkinInput(self,size=(190,30),fontsize=11,nullText='帐号')
        self.pwdText=SkinInput(self,size=(190,30),style=wx.TE_PASSWORD,fontsize=11,nullText='密码')
        #self.txtUserName,self.txtPwd=self.namePanel.GetTextCtrl(),self.pwdPanel.GetTextCtrl()

        self.nameText.SetValue(Cfg.c_lastname if Cfg.c_savename else '')

        self.pwdText.SetValue('')

        self.reglink=hyperlink.HyperLinkCtrl(self, -1,u"注册账号")
        self.reglink.SetBackgroundColour('#f9f1f7')
        #self.forgetPwdlink=hyperlink.HyperLinkCtrl(panel, -1, "忘记密码")
        self.reglink.UnsetToolTip()
        self.reglink.Bind(hyperlink.EVT_HYPERLINK_LEFT,self.EvtReglinkClick)
        self.reglink.AutoBrowse(False)
        self.reglink.EnableRollover(True)
        self.reglink.SetUnderlines(False,False,True)
        self.reglink.OpenInSameWindow(True)
        self.reglink.UpdateLink()


        self.rebName = wx.CheckBox(self, -1, "记住帐号")
        self.rebName.SetValue(Cfg.bool(Cfg.c_savename))

        self.username=self.nameText.GetValue()

        self.Bind(wx.EVT_PAINT,self.OnPaint)
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.Bind(wx.EVT_BUTTON, self.BthLoginClick, self.btnLogin)
        self.Bind(wx.EVT_BUTTON, self.BthSettingClick, self.btnSetting)




    def OnPaint(self,evt):
        dc = wx.BufferedPaintDC(self)
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        dc.DrawBitmap(self.bgBmp, 0, 0)
        rect=self.GetClientRect()
        y=145
        x=100
        dc.DrawBitmap(self.logoBmp,10,y-8)
        self.nameText.SetDimensions(x,y,self.nameText.width,self.nameText.height)
        w,h=self.reglink.GetClientSize()
        self.reglink.SetDimensions(x+self.nameText.width+10,y+8,w,h)
        y+=35
        self.pwdText.SetDimensions(x,y,self.pwdText.width,self.pwdText.height)

        y+=self.pwdText.height+10
        w,h=self.rebName.GetSizeTuple()

        self.rebName.SetDimensions(x,y,w,18)

        x=rect.x +rect.width-self.closeBth.width-1
        self.closeBth.SetDimensions(x,1,
            self.closeBth.width, self.closeBth.height-1)
        x-=self.minBth.width
        self.minBth.SetDimensions(x, 1,
            self.minBth.width, self.minBth.height-1)

        x=rect.x + 10
        y=rect.y +rect.height-32
        self.btnSetting.SetDimensions(x,y,self.btnSetting.width, self.btnSetting.height)

        #w,h=self.btnLogin.GetClientSizeTuple()

#       x=rect.x+rect.width - w-10
#       self.btnLogin.SetDimensions(x,y,w,h)

        x=rect.x+rect.width - self.btnLogin.width-10
        self.btnLogin.SetDimensions(x,y,self.btnLogin.width, self.btnLogin.height)





    def BindEvent(self):
        self.Bind(wx.EVT_BUTTON, self.BthLoginClick, self.btnLogin)
        self.Bind(wx.EVT_BUTTON, self.BthSettingClick, self.btnSetting)



    def BthLoginClick(self, event):
        name, pwd = self.nameText.GetValue().strip(), self.pwdText.GetValue().strip()

        Cfg.c_savename=str(self.rebName.IsChecked())
        self.username=self.nameText.GetValue()

        if name == "":
            MessageBox( '请输入用户名！')
        elif pwd == "":
            MessageBox('请输入密码！')
            self.nameText.SetFocus()

        else:
            UIHandler.OnLogin(self,name,pwd)


    def EvtReglinkClick(self,evt):
        UIHandler.OnRegister()


    def BthSettingClick(self, evt):
        dlg = SettingDlg(self)
        dlg.ShowModal()
        dlg.Destroy()


if __name__=='__main__':

    app=wx.PySimpleApp()
    f=LoginFrame()
    f.Show()
    app.MainLoop()


