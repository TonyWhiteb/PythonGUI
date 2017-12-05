import sys,os
import wx

class FileDropCtrl(wx.Panel):

    def __init__(self, parent,size = (-1,100), label= 'default title', DEVEL =False ):

        super( FileDropCtrl,self).__init__(parent = parent, id =-1,style= wx.SIMPLE_BORDER)

        fdcLabel = wx.StaticText(self,-1,label = ' '+ label, size = (-1,17))
