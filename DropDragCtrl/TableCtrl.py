import wx

class TableCtrl(wx.Panel):

    def __init__(self, parent,callbackFunc = None,size = (100,200), label= 'default title', DEVEL =False ):

        super( TableCtrl,self).__init__(parent = parent, id =-1,style= wx.SIMPLE_BORDER)

        self.callbackFunc = callbackFunc

        fdcLabel = wx.StaticText(self,-1,label = ' '+ label, size = (-1,20))#Creating and Showing a text control

        # SetBold(fdcLabel)
        # self.type_list = []
        # self.path_list = []
        # self.name_list = []

        # fdcID = wx.NewId()
        # self.filesListCtrl = FileListCtrl(self, fdcID, size= size, style = wx.LC_REPORT)

        self.filesDropTarget = self.filesListCtrl
# Layout Control
        fdcPnl_vertSzr = wx.BoxSizer(wx.VERTICAL)
        fdcPnl_vertSzr.Add(fdcLabel, proportion = 0, flag = wx.EXPAND)
        fdcPnl_horzSzr = wx.BoxSizer(wx.HORIZONTAL)
        fdcPnl_horzSzr.Add(fdcPnl_vertSzr, proportion =1, flag = wx.EXPAND)
#
        self.SetSizer(fdcPnl_horzSzr) #Sets the window to have the given layout sizer