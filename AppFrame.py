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
        self.filedropctrl = fdctrl.FileDropCtrl(frmPanel, size=( -1, 100), label='Any Files and Links :')
        self.filedropctrl.SetName('AppFrame::self.filesDropCtrl')
        #
        #
        #
        frmPnl_vertSzr = wx.BoxSizer( wx.VERTICAL )
        frmPnl_vertSzr.AddSpacer( 10 )
        frmPnl_vertSzr.Add(self.filedropctrl, flag = wx.EXPAND)
        frmPnl_vertSzr.AddSpacer(10)

        frmPnl_outerHorzSzr = wx.BoxSizer( wx.HORIZONTAL )
        frmPnl_outerHorzSzr.AddSpacer( 10 )     # border/padding
        frmPnl_outerHorzSzr.Add( frmPnl_vertSzr, proportion=1 )
        frmPnl_outerHorzSzr.AddSpacer( 10 )

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
