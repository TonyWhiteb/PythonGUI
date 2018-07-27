import wx

class ListSQLCtrl(wx.ListCtrl):
    def __init__(self,*args,**kwargs):
        super(ListSQLCtrl,self).__init__(*args,**kwargs)
        self.currRow = None
        self.numCols = -1
        self.haveEntries = False
        self.numEntries = 0
        self.entriesList = []

    def OnFindCurrentRow(self,event): #find current row control
        if (self.currRow is not None):
            self.Select(self.currRow, False)

        row,_ignoredFlags = self.HitTest(event.GetPosition())
            # HitTest, Determine which item is at the specified point.
            # Returns index of the item or wxNOT_FOUND if no item is at the specified point.
        self.currRow = row
        self.Select(row)
    

    def WriteTextTuple(self, rowDataTuple):

        assert(len(rowDataTuple) >= self.numCols), 'Given data must have at least %d items.' %(self.numCols)

        for idx in range(self.numCols):
            assert(isinstance(rowDataTuple[idx],(bytes,str))),'One or both data elements are not strings.'

        rowDataTupleTruncated = tuple(rowDataTuple[:self.numCols])
        if (rowDataTupleTruncated not in self.entriesList):

            if (not self.haveEntries):
                self.DeleteAllItems()

            self.Append(rowDataTupleTruncated)
            self.entriesList.append(rowDataTupleTruncated)
            self.numEntries += 1
            self.haveEntries = True

            self.Autosize()


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