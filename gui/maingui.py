import wx
from base import BaseFrame,WidgetPanel
class RaceConfigPanel(WidgetPanel):
    def SetupWidgets(self):
        
        ch_type = wx.Choice(self,-1,choices=["Laps","Timed"])
        ch_type.Select(0)
        
        end_laps = wx.TextCtrl(self,-1,"2")
        end_time = wx.TextCtrl(self,-1,"1")
        end_time.Hide()
        sz = wx.BoxSizer(wx.HORIZONTAL)
        sz.Add(ch_type)
        sz.AddSpacer(5)
        sz.Add(end_laps)
        sz.Add(end_time)
        self.sizer.Add(sz,0,wx.ALIGN_CENTER|wx.TOP,10)
        
        ch_class = wx.Choice(self,-1,choices=["Expert","Any","Muscle","Nascar","GT","Mini"],size=(100,-1))
        lbl = wx.StaticText(self,-1,"Race Class:")
        ch_class.Select(0)
        sz = wx.BoxSizer(wx.HORIZONTAL)
        sz.Add(lbl,0,wx.ALIGN_CENTER)
        sz.AddSpacer(10)
        sz.Add(ch_class)
        self.sizer.Add(sz,0,wx.ALIGN_CENTER|wx.TOP,5)
        self.sizer.AddSpacer(5)
        self.widgets={'rtype':ch_type,'end_laps':end_laps,'end_time':end_time}
        
        pass
class LeftPanel(WidgetPanel):
    def SetupWidgets(self):
        self.raceConfig1 = RaceConfigPanel(self,-1,size=(200,100))
        self.raceConfig1.SetBackgroundColour("red")
        #self.raceConfig1.SetSize((200,100))
        #self.raceConfig1.SetMinSize((200,100))
        self.racers = []
        self.sizer.Add(self.raceConfig1,0,wx.EXPAND) 
        self.sizer.Add(wx.StaticLine(self,-1,size=(180,-1)),0,wx.ALIGN_CENTER)
    
class RaceGui(BaseFrame):
    def Init(self):
        self.splitter = wx.SplitterWindow(self,-1)
        self.left_panel = LeftPanel(self.splitter,-1,size=(200,600))
        #self.left_panel = wx.Panel(self.splitter,-1,size=(200,600))
        #self.left_panel.SetBackgroundColour("white")
        self.splitter.SetBackgroundColour("black")
        
        self.right_panel = wx.Panel(self.splitter,-1,size=(600,200))
        self.right_panel.SetBackgroundColour("blue")
        
        self.splitter.SplitVertically(self.left_panel,self.right_panel,199)
        print "OK!!!"   
        
if __name__ == "__main__":
    a = wx.App(redirect = False)
    r = RaceGui()
    r.Show()
    a.MainLoop()