import wx
from App.logic.MyFrame import TableFrame as MyFrame


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()