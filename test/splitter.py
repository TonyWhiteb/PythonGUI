import wx
import wx.grid as gridlib

class LeftPanel(wx.Panel):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)

########################################################################
class RightPanel(wx.Panel):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)
        txt = wx.TextCtrl(self)

########################################################################
class MyForm(wx.Frame):

    #----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, title="Splitter Tutorial", pos = (700,300))
        self.SetClientSize((650,400))
        splitter = wx.SplitterWindow(self)
        leftP = wx.Panel(splitter)
        rightP = RightPanel(splitter)

        # split the window
        splitter.SplitVertically(leftP, rightP)
        splitter.SetMinimumPaneSize(500)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(splitter, 1, wx.EXPAND)
        self.SetSizer(sizer)

#----------------------------------------------------------------------
# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()