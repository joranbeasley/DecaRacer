import wx
from base import WidgetPanel
class AddCarPanel(WidgetPanel):
    car_classes = ["Expert","Nascar","Muscle","Mini","Unknown"]
    def SetupWidgets(self):
        sz = wx.BoxSizer(wx.HORIZONTAL)
        lbl = wx.StaticText(self,-1,"Racer Name:",size=(100,-1))
        self.widgets['name'] = wx.TextCtrl(self,-1)
        sz.AddMany([(lbl,0,wx.ALIGN_LEFT),(self.widgets['name'],0,wx.ALIGN_RIGHT)])
        self.sizer.Add(sz,0,wx.ALL,10)
        sz = wx.BoxSizer(wx.HORIZONTAL)
        lbl = wx.StaticText(self,-1,"Car Class:",size=(100,-1))
        self.widgets['xclass'] = wx.Choice(self,-1,choices=self.car_classes)
        sz.AddMany([(lbl,0,wx.ALIGN_LEFT),(self.widgets['xclass'],0,wx.ALIGN_RIGHT)])
        self.sizer.Add(sz,0,wx.ALL,10)
        sz = wx.BoxSizer(wx.HORIZONTAL)
        b1 = wx.Button(self,wx.ID_OK)
        b2 = wx.Button(self,wx.ID_CANCEL)
        sz.AddMany([(b1,0,wx.ALIGN_LEFT|wx.RIGHT,10),(b2,0,wx.ALIGN_RIGHT|wx.LEFT,10)])
        self.sizer.Add(wx.StaticLine(self,-1),0,wx.EXPAND|wx.ALL,10)
        self.sizer.Add(sz,0,wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM,10)
class AddCar(wx.Dialog):
    def __init__(self,title="Add Car"):
        wx.Dialog.__init__(self,None,-1,title=title)
        self.panel = AddCarPanel(self,-1)
        sz = wx.BoxSizer()
        sz.Add(self.panel)
        
        self.SetSizerAndFit(sz)
class AddRacerPanel(WidgetPanel):
    def SetupWidgets(self):
        sz = wx.BoxSizer(wx.HORIZONTAL)
        lbl = wx.StaticText(self,-1,"Racer Name:",size=(100,-1))
        self.widgets['name'] = wx.TextCtrl(self,-1)
        sz.AddMany([(lbl,0,wx.ALIGN_LEFT),(self.widgets['name'],0,wx.ALIGN_RIGHT)])
        self.sizer.Add(sz,0,wx.LEFT|wx.RIGHT|wx.TOP,10)
        sz = wx.BoxSizer(wx.HORIZONTAL)
        add_new_car = wx.Button(self,-1,"Add Car")
        borrow_car  = wx.Button(self,-1,"Borrow a Car")
        add_new_car.Bind(wx.EVT_BUTTON,self.add_car)
        sz.AddMany([(add_new_car,0,wx.ALIGN_LEFT|wx.RIGHT,10),(borrow_car,0,wx.ALIGN_RIGHT|wx.LEFT,10)])
        self.sizer.Add(wx.StaticLine(self,-1),0,wx.EXPAND|wx.ALL,10)
        self.sizer.Add(sz,0,wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM,10)
        
        
class AddRacer(wx.Dialog):
    def __init__(self,title="Add Racer"):
        wx.Dialog.__init__(self,None,-1,title=title)
        self.panel = AddRacerPanel(self,-1)
        sz = wx.BoxSizer()
        sz.Add(self.panel)
        
        self.SetSizerAndFit(sz)

#def add_racer():
if __name__ == "__main__":
    a = wx.App(redirect=False)
    dlg = AddCar()
    dlg.Show() 
    a.MainLoop()
