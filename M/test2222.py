import wx
import wx.grid

class Fenster(wx.Frame):
    def __init__(self):
        '''Constructor, der das Fenster erzeugt'''
        wx.Frame.__init__(self, parent=None, title = "Fenster", size=(1000, 700))

        self.panel = wx.Panel(self, size=(800, 700))

        box = wx.BoxSizer(wx.VERTICAL)


        self.button = wx.Button(self.panel, 0, label="plot me")

        self.myGrid = MyGrid(self.panel)
        box.Add(self.myGrid)


        self.Centre()
        self.Show()

class MyGrid(wx.grid.Grid):
    def __init__(self, parent):
        wx.grid.Grid.__init__(self, parent)


        self.parent = parent
        self.CreateGrid(100, 100)

        self.Show()




app = wx.App()
Fenster()
app.MainLoop()