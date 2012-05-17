import wx

class BaseFrame(wx.Frame):
    title="Generic Window"
    size = (700,600)
    def __init__(self):
        from menu import menu,previous_races
        wx.Frame.__init__(self,None,-1,title=self.title,size=self.size)
        self.SetMenuBar(menu)
        self.SetStatusBar(wx.StatusBar(self,-1))
        self.Init()
    def Init(self):
        pass
    def SetStatus(self,txt):
        self.SetStatusText(txt)
        

class WidgetPanel(wx.Panel):
    def GetWidgetValue(self,widgetInst):
        if hasattr(widgetInst,"GetValue"):
            return widgetInst.GetValue()
        if hasattr(widgetInst,"rval"):
            return widgetInst.rval
    def SetWidgetValue(self,widgetInst,val):
        if hasattr(widgetInst,"SetValue"):
            return widgetInst.SetValue(val)  
    def __init__(self,parent,id,**args):
        wx.Panel.__init__(self,parent,id,**args)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.sizer)
        self.widgets = {}
        self.SetupWidgets()
        self.Layout()
        self.Fit()
    def SetupWidgets(self):
        pass
    def GetValue(self):
        for w in self.widgets:
            self.GetWidgetValue(w)
    def SetValue(self,valueDict):
        for v in valueDict:
            if v in self.widgets:
                self.SetWidgetValue(self.widgets[v], valueDict[v])
                
if __name__ == "__main__":
    a= wx.App(redirect=False)
     #must be imported after app init
    
    f = BaseFrame()
    f.SetStatus("Welcome")
    f.Show()
    
    a.MainLoop()