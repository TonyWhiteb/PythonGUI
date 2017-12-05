import sys,os
import wx

class AppFrame(wx.Frame):

    def __init__(self, args,argc,title = 'Demo', DEVEL =False):
        self.DEVEL =DEVEL
        super(AppFrame, self).__init__(parent = None, id= -1, title = title, pos=(800,400))
        self.SetClientSize((650,400))

if __name__ == '__main__':
    args = sys.argv
    THISPYFILE = args.pop(0)
    argc = len(args)

    app = wx.App(redirect = False)
    appFrame = AppFrame(args, argc,DEVEL =1)
    import wx.lib.inspection
    app.MainLoop()
