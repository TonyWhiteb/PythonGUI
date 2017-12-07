import sys,os
import wx

import FileDropCtrl as fdctrl
class AppFrame(wx.Frame):

    def __init__(self, args,argc,title = 'Demo', DEVEL =False):
        self.DEVEL =DEVEL
        super(AppFrame, self).__init__(parent = None, id= -1, title = title, pos=(800,400))
        self.SetClientSize((650,400))
        frmPanel = wx.Panel(self,-1)
        frmPanel.SetName('frmPanel')
        frmPanel.SetBackgroundColour(wx.WHITE)
        # create the basic panel and go to create first control
        self.filedropctrl = fdctrl.FileDropCtrl(frmPanel, label='Any Files and Links :')
        self.filedropctrl.SetName('AppFrame::self.filesDropCtrl')
        #
        #Frame layout control
        #
        frmPnl_vertSzr = wx.BoxSizer( wx.VERTICAL )
        frmPnl_vertSzr.AddSpacer( 10 ) #space on the top
        frmPnl_vertSzr.Add(self.filedropctrl, flag = wx.EXPAND) #insert sub panel
        frmPnl_vertSzr.AddSpacer(10) #space on the bottom

        frmPnl_outerHorzSzr = wx.BoxSizer( wx.HORIZONTAL )
        frmPnl_outerHorzSzr.AddSpacer( 10 )     # space on the left
        frmPnl_outerHorzSzr.Add( frmPnl_vertSzr, proportion=1 )
        frmPnl_outerHorzSzr.AddSpacer( 10 ) #space on the right
        #
        #
        #
        frmPanel.SetSizerAndFit( frmPnl_outerHorzSzr )
        self.Show()
if __name__ == '__main__':
    args = sys.argv
    THISPYFILE = args.pop(0)
    argc = len(args)

    app = wx.App(redirect = False)
    appFrame = AppFrame(args, argc,DEVEL =1)
    import wx.lib.inspection
    app.MainLoop()
