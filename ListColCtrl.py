import sys,os
import wx

import FileDropCtrl as fdctrl
import DragandDrop as ddt

class ListColFrame(wx.Frame):

    def __init__(self, title ='2nd Demo'):


        super(ListColFrame, self).__init__(parent = None, id = -1, title = title, pos = (700,300))
        self.SetClientSize((650,400))
