# https://wiki.wxpython.org/DragAndDrop
import wx

class FileDropTarget (wx.FileDropTarget):
    def __init__(self,obj):
        
