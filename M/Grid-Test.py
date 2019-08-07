import wx
import wx.grid

class Fenster(wx.Frame):
    def __init__(self, parent, title):
        '''Constructor, der das Fenster erzeugt'''
        #wx.Frame.__init__(self, parent=None, title = "Fenster", size=(1000, 700))
        super(Fenster, self).__init__(parent, title=title, size=(800,800))

        panel = wx.Panel(self, size=(800, 700))
        panel.SetBackgroundColour("gray")
        box = wx.BoxSizer(wx.VERTICAL)

        self.label = wx.StaticText(panel, label="Übersicht", style=wx.ALIGN_CENTER)
        box.Add(self.label, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 15)

        self.button = wx.Button(panel, 0, label="Close", )
        self.button.Bind(wx.EVT_BUTTON, self.bei_Click)

        self.myGrid = MyGrid(panel)
        box.Add(self.myGrid)

        panel.SetSizer(box)
        self.Centre()
        self.Show()

    def bei_Click(self, event):
        self.Close()


class MyGrid(wx.grid.Grid):
    def __init__(self, parent):
        wx.grid.Grid.__init__(self, parent)


        self.parent = parent
        self.CreateGrid(150, 10)
        self.EnableEditing(False)


        self.Show()




app = wx.App()
Fenster(None, "Fenster")
app.MainLoop()