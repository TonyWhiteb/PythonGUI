import sys,os
import wx

import  wx.lib.mixins.listctrl  as  listmix
from collections import defaultdict

class TableFrame(wx.Frame):

    def __init__(self, title = 'Dictionary View', Dictionary_Dict = None):


        self.dictionary = Dictionary_Dict
        super(TableFrame,self).__init__(parent = None, id= -1, title = title, pos=(800,400))
        self.SetClientSize((650,400))
        # frmPanel1
        frmPanel1 = wx.Panel(self,1)
        frmPanel1.SetName('frmPanel1')
        frmPanel1.SetBackgroundColour(wx.RED)
        # frmPanel2
        frmPanel2 = wx.Panel(self,1)
        frmPanel2.SetName('frmPanel2')
        frmPanel2.SetBackgroundColour(wx.GREEN)
        #
        self.field_list = []
        self.exeFolder = None
        # self.incFoldersList = list()
        self.tablename = []
        # create the basic panel and go to create first control
        # self.filedropctrl = fdctrl.FileDropCtrl(frmPanel1,size = (50,200), label='Dictionary')
        # self.filedropctrl.SetName('AppFrame::self.filesDropCtrl')
        #Create the sub panel for list control
        # self.filedropctrl.SetCallbackFunc(self.OnFilesDropped)
        # self.filedropctrl.SetBackgroundColour(wx.BLUE)
        headerLabelList = [  'Parent Path','File or Link Name','File Type' ]
        # self.filedropctrl.WriteHeaderLabels( headerLabelList )

        srcFilesHelpText = 'Drop Files and Links Here'
        # self.filedropctrl.WriteHelptext( srcFilesHelpText )

        # onButtonListCol = self.OnListColButton
        # onButtonSQL = self.OnSQLButton

        # self.buttonPanel = ButtonPanel(frmPanel1, onButtonListCol = onButtonListCol, onButtonSQL= onButtonSQL)
        #
        #Frame layout control
        #
        frmPnl_vertSzr = wx.BoxSizer( wx.VERTICAL )
        frmPnl_vertSzr.AddSpacer( 10 ) #space on the top
        # frmPnl_vertSzr.Add(self.filedropctrl, flag = wx.EXPAND) #insert sub panel
        frmPnl_vertSzr.AddSpacer(10) #space on the bottom
        # frmPnl_vertSzr.Add( self.buttonPanel,    flag=wx.EXPAND )
        frmPnl_vertSzr.AddSpacer( 10 )

        frmPnl_outerHorzSzr = wx.BoxSizer( wx.HORIZONTAL )
        frmPnl_outerHorzSzr.AddSpacer( 10 )     # space on the left
        frmPnl_outerHorzSzr.Add( frmPnl_vertSzr, proportion=1 )
        frmPnl_outerHorzSzr.AddSpacer( 10 ) #space on the right
        #
        #
        #
        frmPanel1.SetSizerAndFit( frmPnl_outerHorzSzr )
        # self.Show()
def main():
    app = wx.App()
    frame = TableFrame()
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()        