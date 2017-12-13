import sys,os
import wx

import ListColCtrl as lcc

class ListColFrame(wx.Frame):

    # def __init__(self, title ='2nd Demo'):
    #
    #
    #     super(ListColFrame, self).__init__(parent = None, id = -1, title = title, pos = (700,300))
    #     self.SetClientSize((650,400))
    #     colPanel = wx.Panel(self,-1)
    #     colPanel.SetName('colPanel')
    #     colPanel.SetBackgroundColour(wx.WHITE)
    #
    #     self.listcolctrl = lcc.ListColCtrl(colPanel, size= (50,200), label = 'All columns list')
    def __init__(self):
        wx.Frame.__init__(self,None, wx.ID_ANY, "2nd_Demo",pos=(700,300))
        self.SetClientSize((650,400))
        panel = wx.Panel(self, wx.ID_ANY)
        # self.chbBSizer = wx.BoxSizer(wx.VERTICAL)

        self.index = 0
        self.list_ctrl = lcc.ListColCtrl(panel, size = (-1,100), style = wx.LC_REPORT|wx.BORDER_SUNKEN)
        self.list_ctrl.InsertColumn(0,'Common Column Names')
    def ListColInfo(self,col):
        for i in range(len(col)):
        #     chb = wx.CheckBox(self, wx.ID_ANY, col[i], wx.DefaultPosition, wx.DefaultSize, 0 )
        #     self.chbBSizer.Add(chb)
        #
        # self.Layout()
            self.list_ctrl.InsertItem(self.index,col[i])
            # chb = wx.CheckBox(self, wx.ID_ANY, self.list_ctrl.GetItemText(self.index), wx.DefaultPosition, wx.DefaultSize, 0 )
            self.index +=1
