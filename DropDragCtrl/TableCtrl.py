import wx

class TableCtrl(wx.ListCtrl):
    def __init__(self,*args,**kwargs):
        super(TableCtrl,self).__init__(*args,**kwargs)
        self.numCols = -1
        self.currRow = None
        self.Bind(wx.EVT_LEFT_DOWN,self.OnFindCurrentRow)

    def OnFindCurrentRow(self,event):
        if (self.currRow is not None):
            self.Select(self.currRow, False)

        row, _ignoredFlags = self.HitTest(event.GetPosition())

        self.currRow = row
        self.Select(row)
    def Autosize(self):

        self.Append(self.headerLabelList)
        for colIndex in range( len( self.headerLabelList ) ) :
            self.SetColumnWidth( colIndex, wx.LIST_AUTOSIZE )

        self.DeleteItem( self.GetItemCount() - 1 )

        """
        If any one filename is very long the column width was set too long and
          occupies "too much" width in the control causing little or no display
          of the folder paths to be shown.

        Set first row's width to no more than 50% of the control's client width.
        This is a "reasonable" balance which leaves both columns's data
           at least 50% displayed at all times.
        """
        firstColMaxWid = self.GetClientSize()[ 0 ] / 2      # Half the avaiable width.
        firstColIndex = 0                           # Avoid the use of "Magic Numbers".
        firstColActualWid = self.GetColumnWidth( firstColIndex )
        reasonableWid = min( firstColMaxWid, firstColActualWid )
        self.SetColumnWidth( firstColIndex, reasonableWid )
    

class TablePanel(wx.Panel):

    def __init__(self, parent,callbackFunc = None,size = (300,200), label= 'default title', DEVEL =False ):

        super( TablePanel,self).__init__(parent = parent, id =-1,style= wx.SIMPLE_BORDER)

        self.callbackFunc = callbackFunc

        fdcID = wx.NewId()
        fdcLabel = wx.StaticText(self,-1,label = ' '+ label, size = (-1,20))#Creating and Showing a text control
        self.tablectrl = TableCtrl(self, fdcID, size= size, style = wx.LC_REPORT)

# Layout Control
        fdcPnl_vertSzr = wx.BoxSizer(wx.VERTICAL)
        fdcPnl_vertSzr.Add(fdcLabel, proportion = 0, flag = wx.EXPAND)
        fdcPnl_vertSzr.Add(self.tablectrl,proportion = 1, flag = wx.EXPAND)
        fdcPnl_horzSzr = wx.BoxSizer(wx.HORIZONTAL)
        fdcPnl_horzSzr.Add(fdcPnl_vertSzr, proportion =1, flag = wx.EXPAND)
#
        self.SetSizer(fdcPnl_horzSzr) #Sets the window to have the given layout sizer
    def WriteHeaderLabels( self, headerLabelList ) :
        """ Write the column header labels. """

        self.headerLabelList = headerLabelList
        self.tablectrl.headerLabelList = headerLabelList

        #-----

        # This sets the "official" number of columns the textCtrl has.
        self.numCols = len( self.headerLabelList )
        self.tablectrl.numCols = self.numCols

        for col in range( self.numCols ) :
            self.tablectrl.InsertColumn( col, self.headerLabelList[ col ] )

        # AUTOSIZE
        for col in range( self.numCols ) :
            self.tablectrl.SetColumnWidth( col, wx.LIST_AUTOSIZE )

        # Widen the header-list-as-row-data in order to completely show the column labels.
        # This hack works very well !
        hdrListWidened = headerLabelList
        for i in range( len( hdrListWidened ) ) :
            hdrListWidened[ i ] += ' '     # Estimated number of spaces needed
                                            #   to fully show the header.
        # Delete the header-list-as-row-data.
        self.tablectrl.Append( hdrListWidened )   # Does NOT add to item/row data list.
        numRows = self.tablectrl.GetItemCount()
        self.tablectrl.DeleteItem( numRows - 1 )