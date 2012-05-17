import wx

#default string renderer just prints the in the center of a cell
def StrRender(dc,value,pos,size):
    sw,sh =dc.GetTextExtent(str(value))
    x,y = pos[0]+(size[0]/2-sw/2),pos[1]+(size[1]/2-sh/2)
    dc.DrawText(str(value),x,y)


class CustomGrid(wx.Panel):
    fields=["a","b","c"]
    data= [[1,2,3],[4,5,6],[7,8,9]]
    title= "Title"
    CellWidth = 60
    CellHeight = 30
    bgColor_header_main=(0,0,0)
    borderColor_header_main=(0,0,0)
    txtColor_header_main = (255,255,255)
    font_header_main = (32,wx.FONTFAMILY_MODERN,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_BOLD)
    
    bgColor_header_grid=(100,120,100)
    borderColor_header_grid=(0,0,0)
    txtColor_header_grid = (255,255,255)
    font_header_grid = (20,wx.FONTFAMILY_MODERN,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_BOLD)
    
    bgColor_grid=(0xcc,0xcc,0xcc)
    borderColor_grid=(0,0,0)
    txtColor_grid = (0,0,0)
    font_grid = (16,wx.FONTFAMILY_MODERN,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_BOLD)
    
    def __init__(self,parent,id,**kwargs):
        wx.Panel.__init__(self,parent,id)
        self.dc=None
        self.states = []
        if hasattr(self,"images"):
        
            for image in self.images:
                #print "Add image:",image
                if image:self.states.append(wx.Bitmap(image))
                else:self.states.append(None)
                #print self.states
        
        #self.SetDoubleBuffered(True)
        self.fields = kwargs.get("fields",self.fields)
        self.data = kwargs.get("data",self.data)
        self.title = kwargs.get("title",self.title)
        self.renderes = kwargs.get('renderers',[StrRender for i in range(len(self.fields))])
        self.CellHeight = kwargs.get('cellHeight',self.CellHeight)
        self.CellWidth = kwargs.get('cellWidth',self.CellWidth)
        self.spacer = kwargs.get('spacer',5)
        
        self.bgColor_header_main = kwargs.get('header_bg',self.bgColor_header_main)
        self.borderColor_header_main=kwargs.get('header_border',self.borderColor_header_main)
        self.txtColor_header_main=kwargs.get('header_text_color',self.txtColor_header_main)
        self.font_header_main = kwargs.get('header_font_args',self.font_header_main)
        
        self.bgColor_header_grid = kwargs.get('label_bg',self.bgColor_header_grid)
        self.borderColor_header_grid=kwargs.get('label_border',self.borderColor_header_grid)
        self.txtColor_header_grid=kwargs.get('label_text_color',self.txtColor_header_grid)
        self.font_header_grid = kwargs.get('label_font_args',self.font_header_grid)
        
        self.bgColor_grid = kwargs.get('grid_bg',self.bgColor_grid)
        self.borderColor_grid=kwargs.get('grid_border',self.borderColor_grid)
        self.txtColor_grid=kwargs.get('grid_text_color',self.txtColor_grid)
        self.font_grid = kwargs.get('grid_font_args',self.font_grid)
        
        self.Bind(wx.EVT_PAINT,self.OnPaint)
        self.nRows = len(self.data)
        self.nCols = len(self.fields)
        self.current_y = 0
        w,h = self.CalcMinSize()
        #print "Min Size:",w,h
        self.SetSize((w,h))
        self.SetMinSize((w,h))
    def GetCol(self,col):
        return [d[col] for d in self.data]
    def AddRow(self,rowTuple):
        self.data.append(rowTuple)
        self.Refresh()
    def SetData(self,data):
        if data == self.data:return
        self.data = data
        self.Refresh()
        #print "Set Data",data
    def SetRow(self,row,rowTuple):
        self.data[row]=rowTuple
        self.Refresh()
    def InsertRow(self,row,rowData):
        self.data.insert(row,rowData)
        self.Refresh()
    def GetValue(self,row,col=None):
        try:the_row = self.data[row]
        except: return None
        if col != None:
            try:return the_row[col]
            except:return ""
        return the_row
    def SetValue(self,row,col,value):
        self.data[row][col]=value
    def SetupDCAttribsFor(self,key="header_main"):
        bg =self.__dict__["bgColor_%s"%key]
        fg =self.__dict__["borderColor_%s"%key]
        tc =self.__dict__["txtColor_%s"%key]
        fnt=self.__dict__["font_%s"%key]
              
        self.dc.SetBrush(wx.Brush(wx.Color(*bg)))
        self.dc.SetPen(wx.Pen(wx.Color(*fg)))
        self.dc.SetTextForeground(wx.Color(*tc))
        self.dc.SetFont(wx.Font(*fnt))
    def CalcMinSize(self):
        gw = self.CellWidth*self.nCols
        gh = self.CellHeight*(self.nRows+1)
        
        th = self.CellHeight*2
        
        h=gh+th+self.spacer*3
        w=gw+self.spacer*2
        #print "W:",w
        return (w,h)
    def PaintHeader(self):
        h = self.CellHeight*2
        
        w = self.CellWidth*self.nCols
        
        self.SetupDCAttribsFor('header_main')
        self.dc.DrawRectangle(self.spacer,self.spacer,w,h)
        sw,sh=self.dc.GetTextExtent(self.title)
        self.dc.DrawText(self.title,(self.spacer*2+w)/2-sw/2,(self.spacer*2+h)/2-sh/2)
        self.current_y = h+self.spacer
    def PaintColumnHeaders(self):
        w = self.CellWidth
        h = self.CellHeight
        y = self.current_y+self.spacer
        for i in range(self.nCols):
            x=self.spacer+w*i
            self.dc.DrawRectangle(x,y,w,h)
            sw,sh = self.dc.GetTextExtent(self.fields[i])
            self.dc.DrawText(self.fields[i],x+w/2-sw/2,y+(h/2-sh/2))
            
          
        self.current_y = self.current_y+h+self.spacer
    def PaintRow(self,rowData):
        #print "Paint Row:",rowData
        for i in range(self.nCols):
            try:val = rowData[i]
            except:val = ""
            w , h = self.CellWidth,self.CellHeight
            x , y = self.spacer+w*i,self.current_y 
            #print "Draw %s at y=%d"%(val,y)
            self.dc.DrawRectangle(x,y,w,h)
            self.renderes[i](self.dc,val,(x,y),(w,h))
        self.current_y += self.CellHeight
            
    def PaintGridContents(self):
        for row in self.data:
            self.PaintRow(row)        
    def PaintGrid(self):
        self.SetupDCAttribsFor('header_grid')
        self.PaintColumnHeaders()
        self.SetupDCAttribsFor('grid')
        self.PaintGridContents()
    def OnPaint(self,evt):
        self.current_y=0
        self.dc = dc = wx.PaintDC(self)
        self.dc.Clear()
        #print "Painting with DC:",dc
        dc.SetBrush(wx.BLACK_BRUSH)
        dc.BeginDrawing()
        self.PaintHeader()
        self.PaintGrid()
        #print "Update!xx"
#        self.PaintGridHeader()
#        self.PaintRacerData("bob","1",96)
#        self.PaintRacerData("charlie","2",126)
#        self.PaintRacerData("frank","3",156)
#        self.PaintRacerData("ronald","4",186)
        dc.EndDrawing()
        self.Update()
        evt.Skip()
        
if __name__ == "__main__":
    a = wx.App(redirect=False)
    f =wx.Frame(None,-1)
    p = CustomGrid(f,-1)
    f.Show()
    a.MainLoop()