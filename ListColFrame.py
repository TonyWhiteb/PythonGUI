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
        onButtonHandlers = self.OnFinalButton
        self.buttonPanel = ButtonPanel(panel, onButtonHandlers = onButtonHandlers)
        # self.chbBSizer = wx.BoxSizer(wx.VERTICAL)

        self.index = 0
        self.list_ctrl = lcc.ListColCtrl(panel, size = (-1,100), style = wx.LC_REPORT|wx.BORDER_SUNKEN)
        self.list_ctrl.InsertColumn(0,'Column Name')
        self.list_ctrl.InsertColumn(1,'File Name')
    def ListColInfo(self,final_dict):
        key_list = []
        value_list =[]

        for key, value in final_dict.items():
            key_list.append(key)
            value_list.append(value)
        if len(key_list) == len(value_list):
            for i in range(len(key_list)):
                for j in range(len(value_list[i])):
                    self.list_ctrl.InsertItem(j,value_list[i][j])
                    self.list_ctrl.SetItem(j,1,key_list[i])

        return self.list_ctrl
    def OnFinalButton(self,event):
        print(self.list_ctrl.getSelected())

class ButtonPanel(wx.Panel):

    def __init__(self, parent= None, id= -1, onButtonHandlers = None):

        super(ButtonPanel, self).__init__(parent = parent, id = id)

        listAllBtn = wx.Button(self, -1, 'Create Final File')

        listAllBtn.Bind(wx.EVT_LEFT_DOWN, onButtonHandlers)

        btnPanel_innerHorzSzr = wx.BoxSizer( wx.HORIZONTAL )
        btnPanel_innerHorzSzr.AddStretchSpacer( prop=1 )
        btnPanel_innerHorzSzr.Add( listAllBtn )
        btnPanel_innerHorzSzr.AddSpacer( 25 )

        btnPanel_innerHorzSzr.AddStretchSpacer( prop=1 )

        btnPanel_outerVertSzr = wx.BoxSizer( wx.VERTICAL )
        btnPanel_outerVertSzr.AddSpacer( 5 )
        btnPanel_outerVertSzr.Add( btnPanel_innerHorzSzr, flag=wx.EXPAND )
        btnPanel_outerVertSzr.AddSpacer( 5 )

        self.SetSizer( btnPanel_outerVertSzr )
        self.Layout()
