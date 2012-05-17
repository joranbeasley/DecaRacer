import wx
class RaceController(wx.App):
    def __init__(self):
        wx.App.__init__(self, redirect=False)
        self.mainframe = RaceGui()
        self.MainLoop()
        