import sys,os
import wx
import pandas as pd
from pandas import ExcelWriter
from DropDragCtrl import FileDropCtrl as fdctrl
from DropDragCtrl import ListSQLCtrl as lsc
from DropDragCtrl import TableCtrl as tc


class TableFrame(wx.Frame):

    def __init__(self,big_dict,file_path):
        wx.Frame.__init__(self,None, wx.ID_ANY, "SQL_Demo",pos=(700,300))
        self.SetClientSize((500,400))
        # splitter = wx.SplitterWindow(self)
        # leftP = wx.Panel(self,-1)
        # rightP = wx.Panel(self,-1)
        # rightP = RightPanel(splitter)
        # splitter.SplitVertically(leftP, rightP)
        # panel = wx.Panel(self, wx.ID_ANY)
        # onButtonHandlers = self.onSaveFile
        # self.buttonPanel = ButtonPanel(leftP)
        self.file_path = file_path
        self.currentDirectory = os.getcwd()
        self.big_dict = big_dict 
        self.filelist = []
        self.filedict = {}
        self.index_list =[]
        self.final_col_list = []
        self.items = []
        self.index = 0
        # self.column_name = []
        list_ctrl_header = ['Field Name','Process']
        select_ctrl_header = ['Table Name']

        FirstSplitter = wx.SplitterWindow(self)
        NextSplitter = wx.SplitterWindow(FirstSplitter)

        # self.list_ctrl = myPanel(leftP, size = (200,300), label= 'left',InsertCol= ['Column Name','Needed Name'])
        self.list_ctrl = tc.TablePanel(FirstSplitter,-1, size = (200,300), label= 'left')
        self.list_ctrl.WriteHeaderLabels(list_ctrl_header)
        self.list_ctrl.tablectrl.Autosize()
        self.select_ctrl = tc.TablePanel(NextSplitter,-1, size = (200,300), label = 'right')
        self.select_ctrl.WriteHeaderLabels(select_ctrl_header)
        self.select_ctrl.tablectrl.Autosize()
        # panel_button = wx.Button(self.select_ctrl,-1,label = 'test')
        # selelct_bt = wx.Button(self.select_ctrl, -1,label = "test")

        btPanel = ButtonPanel(NextSplitter, label = '3')

        NextSplitter.SplitHorizontally(self.select_ctrl,btPanel)
        NextSplitter.SetSashGravity(0.8)
        

        FirstSplitter.SplitVertically(self.list_ctrl,NextSplitter)
        FirstSplitter.SetSashGravity(0.5)
        
        # splitter.SetMinimumPaneSize(200)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(FirstSplitter,1,wx.EXPAND)
        self.SetSizer(sizer)

         
        #
        #
        #
    def ListSelectInfo(self,big_dict):
        self.select_list = []
        self.info_list = []
        for key, value in big_dict.items():
            select_list.append(key)
            info_list.append(value)
        for i in range(len(select_list)):
            self.select_ctrl.tablectrl.InsertItem(i,select_list[i])

        self.Autosize()

        return self.select_ctrl

    def OnInfoButton(self,event):
        if self.select_ctrl.tablectrl.currRow is None:
            raise Exception('Select a table name')
        else:
            
    

    def Autosize(self):
        for colIndex in range(2):
            self.select_ctrl.tablectrl.SetColumnWidth(colIndex,wx.LIST_AUTOSIZE)



        # frmPnl_outerHorzSzr = wx.BoxSizer( wx.HORIZONTAL )
        # frmPnl_outerHorzSzr.AddSpacer( 10 )     # space on the left
        # frmPnl_outerHorzSzr.Add( self.list_ctrl,0)
        # frmPnl_outerHorzSzr.AddSpacer( 10 ) #space on the right
        # frmPnl_outerHorzSzr.Add( self.select_ctrl,0)
        # frmPnl_outerHorzSzr.AddSpacer( 10 ) #space on the right        
        # #
        # #
        # #
        # leftP.SetSizerAndFit( frmPnl_outerHorzSzr )
        # # rightP.SetSizerAndFit( frmPnl_outerHorzSzr )


class ButtonPanel(wx.Panel):

    def __init__(self, parent,label = 'default' , onButtonHandlers = None):

        super(ButtonPanel, self).__init__(parent = parent, id = -1)

        listAllBtn = wx.Button(self, -1, 'Show Info')

        listAllBtn.Bind(wx.EVT_LEFT_DOWN, onButtonHandlers)

        btnPanel_innerHorzSzr = wx.BoxSizer( wx.HORIZONTAL )
        btnPanel_innerHorzSzr.AddStretchSpacer( prop=1 )
        btnPanel_innerHorzSzr.Add( listAllBtn )
        btnPanel_innerHorzSzr.AddSpacer( 25 )

        btnPanel_innerHorzSzr.AddStretchSpacer( prop=1 )

        btnPanel_outerVertSzr = wx.BoxSizer( wx.VERTICAL )
        btnPanel_outerVertSzr.AddSpacer( 20 )
        btnPanel_outerVertSzr.Add( btnPanel_innerHorzSzr)
        btnPanel_outerVertSzr.AddSpacer( 20 )

        self.SetSizer( btnPanel_outerVertSzr )
        self.Layout()


