import wx
#_File = wx.MenuItem("File")

race_types = wx.Menu()
race_types.Append(20,"Open Class","Any Class Can Race")
race_types.Append(21,"Expert Class","No Mag Racing")
race_types.Append(22,"Endurance","Rotate Lanes, Extra Long")
race_types.AppendSeparator()
race_types.Append(24,"Muscle","Muscle Cars Only")
race_types.Append(25,"Nascar","Nascar Cars Only")
race_types.Append(26,"Mini","Mini Cars Only")



previous_races = wx.Menu()
previous_races.AppendMenu(10,'New Race',race_types,'Start a New Race')
previous_races.Append(11,'Last Race','Same Settings as Last Time')

fileMenu = wx.Menu()
fileMenu.Append(1,'Add Racer','Add A New Racer')
fileMenu.Append(2,'Edit Racer','Add/Remove Cars')
fileMenu.AppendMenu(3,"Start Racing",previous_races,'Race Options')
fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')



menu = wx.MenuBar()
menu.Append(fileMenu, '&File')
