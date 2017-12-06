import sys,os
import wx


class FileListCtrl(wx.ListCtrl):
    def __init__(self,*args,**kwargs):
        super(FileListCtrl,self).__init__(*args,**kwargs)

        self.currRow = None

        self.Bind(wx.EVT_LEFT_DOWN, self.OnFindCurrentRow )
        # self.Bind(wx.EVT_RIGHT_DOWN,)

    def OnFindCurrentRow(self,event): #find current row control
        if (self.currRow is not None):
            self.Select(self.currRow, False)

        row,_ignoredFlags = self.HitTest(event.GetPosition())
            # HitTest, Determine which item is at the specified point.
            # Returns index of the item or wxNOT_FOUND if no item is at the specified point.
        self.currRow = row
        self.Select(row)    

    # def OnRightDown(self,event): #Right click menu
    #
    #     menu = wx.Menu()
    #     menuItem = menu.Append(-1,'Delete this file')
    #
    #     self.Bind(wx.EVT_MENU, )




class FileDropCtrl(wx.Panel):

    def __init__(self, parent,size = (-1,100), label= 'default title', DEVEL =False ):

        super( FileDropCtrl,self).__init__(parent = parent, id =-1,style= wx.SIMPLE_BORDER)

        fdcLabel = wx.StaticText(self,-1,label = ' '+ label, size = (-1,17))#Creating and Showing a text control

        SetBold(fdcLabel)

        fdcID = wx.NewId()
