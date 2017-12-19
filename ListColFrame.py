import sys,os
import wx
import pandas as pd


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
    def __init__(self,big_dict):
        wx.Frame.__init__(self,None, wx.ID_ANY, "2nd_Demo",pos=(700,300))
        self.SetClientSize((650,400))
        panel = wx.Panel(self, wx.ID_ANY)
        onButtonHandlers = self.OnFinalButton
        self.buttonPanel = ButtonPanel(panel, onButtonHandlers = onButtonHandlers)
        self.big_dict = big_dict
        self.filelist = []
        self.filedict = {}
        self.index_list =[]
        self.items = []
        self.index = 0
        # self.column_name = []
        self.list_ctrl = lcc.ListColCtrl(panel, size = (500,304), style = wx.LC_REPORT|wx.BORDER_SUNKEN)
        self.list_ctrl.InsertColumn(0,'Column Name')
        self.list_ctrl.InsertColumn(1,'File Name')
        #
        #
        #
        frmPnl_vertSzr = wx.BoxSizer( wx.VERTICAL )
        frmPnl_vertSzr.AddSpacer( 10 ) #space on the top
        frmPnl_vertSzr.Add(self.list_ctrl, flag = wx.EXPAND) #insert sub panel
        frmPnl_vertSzr.AddSpacer(10) #space on the bottom
        frmPnl_vertSzr.Add( self.buttonPanel,    flag=wx.EXPAND )
        frmPnl_vertSzr.AddSpacer( 10 )

        frmPnl_outerHorzSzr = wx.BoxSizer( wx.HORIZONTAL )
        frmPnl_outerHorzSzr.AddSpacer( 10 )     # space on the left
        frmPnl_outerHorzSzr.Add( frmPnl_vertSzr, proportion=1 )
        frmPnl_outerHorzSzr.AddSpacer( 10 ) #space on the right
        #
        #
        #
        panel.SetSizerAndFit( frmPnl_outerHorzSzr )
    def ListColInfo(self,big_dict):
        key_list = []
        value_list =[]

        for key, value in big_dict.items():
            key_list.append(key)
            value_list.append(value)
        if len(key_list) == len(value_list):
            for i in range(len(key_list)):
                for k in value_list[i]:
                    k_list =[]
                    k_list.append(k)
                    for j in range(len(k_list)) :
                        self.list_ctrl.InsertItem(j,k_list[j])
                        self.list_ctrl.SetItem(j,1,key_list[i])

        self.Autosize()
        self.filelist = key_list
        self.filedict = self.filedict.fromkeys(key_list)
        return self.list_ctrl

    def Autosize(self):
        for colIndex in range(2):
            self.list_ctrl.SetColumnWidth(colIndex,wx.LIST_AUTOSIZE)

    def OnFinalButton(self,event):
        self.index_list = self.list_ctrl.getSelected_id()
        column_name = []
        # items = self.list_ctrl.GetItem(index_list[0], 1)
        for filename in self.filelist:
            item_list = []
            for i in range(len(self.index_list)):
                if filename == self.list_ctrl.GetItemText(self.index_list[i],1):
                    item_list.append(self.list_ctrl.GetItemText(self.index_list[i],0))
            self.filedict[filename]= item_list
            column_name += self.filedict[filename]
        column_name = list(set(column_name))

        # for i in range(len(self.index_list)):
        #     # self.items.append(self.list_ctrl.GetItemText(self.index_list[i],0))
        #     for filename in self.filelist:
        #         item_list = []
        #         if filename == self.list_ctrl.GetItemText(self.index_list[i],1):
        #             item_list.append(self.list_ctrl.GetItemText(self.index_list[i],0))
        #             self.filedict[filename]= item_list
        print(self.filedict)


        # print(column_name)
    def ReadFile(self,big_dict):

        file_need = {}
        file_need = self.filedict


        for i in range(len(big_dict)):
            if file_path_list[i][0] in self.filelist:
                file_need[file_path_list[i][0]]= file_path_list[i][1]
        for k, r in file_need:
            os.chdir(r)
            afile = open(k,"r").readlines()




    def SaveFile(self,column_name):
        pass
    def GetWidth(self):
        table_width = self.list_ctrl.GetSize()[0]
        return table_width

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
        btnPanel_outerVertSzr.Add( btnPanel_innerHorzSzr)
        btnPanel_outerVertSzr.AddSpacer( 5 )

        self.SetSizer( btnPanel_outerVertSzr )
        self.Layout()
