import sys,os
import wx

class ListColCtrl(wx.Panel):

    def __init__(self, parent, size =(-1,200), label = 'default col list'):

        super( ListColCtrl, self).__init__(parent = parent, id= -1, style = wx.SIMPLE_BORDER)
