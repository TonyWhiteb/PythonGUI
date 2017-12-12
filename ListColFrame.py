import sys,os
import wx

import ListColCtrl as lcc

class ListColFrame(wx.Frame):

    def __init__(self, title ='2nd Demo'):


        super(ListColFrame, self).__init__(parent = None, id = -1, title = title, pos = (700,300))
        self.SetClientSize((650,400))
        colPanel = wx.Panel(self,-1)
        colPanel.SetName('colPanel')
        colPanel.SetBackgroundColour(wx.WHITE)

        self.listcolctrl = lcc.ListColCtrl(colPanel, size= (50,200))
