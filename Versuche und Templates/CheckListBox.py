'''Template für Checklist-Box aus dem Internet
Aufbau und Events'''

import wx

global choice
choice = 0

# Internet-Version CheckBox
class Mywin(wx.Frame):
    def __init__(self, parent, title):
        super(Mywin, self).__init__(parent, title=title, size=(300, 200))

        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)
        self.label = wx.StaticText(panel, label="IST oder SOLL?", style=wx.ALIGN_CENTRE)

        box.Add(self.label, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 20)

        cblbl = wx.StaticText(panel, label="Combo box", style=wx.ALIGN_CENTRE)

        box.Add(cblbl, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)
        languages = ["Auswahl treffen", "IST", "SOLL"]
        self.combo = wx.ComboBox(panel, choices=languages)

        box.Add(self.combo, 1, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)
        chlbl = wx.StaticText(panel, label="Choice control", style=wx.ALIGN_CENTRE)

        box.Add(chlbl, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)
        self.choice = wx.Choice(panel, choices=languages)
        box.Add(self.choice, 1, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        box.AddStretchSpacer()
        self.combo.Bind(wx.EVT_COMBOBOX, self.OnCombo)
        self.choice.Bind(wx.EVT_CHOICE, self.OnChoice)

        panel.SetSizer(box)
        self.Centre()
        self.Show()

    def OnCombo(self, event):
        global choice
        self.label.SetLabel("Es wurde " + self.combo.GetValue() + " ausgewählt")
        if self.combo.GetValue() == "IST":
            choice = 1
        elif self.combo.GetValue() == "SOLL":
            choice = 2
        else:
            choice = "Bitte SOLL oder IST auswählen"
            print("Bitte SOLL oder IST auswählen")

    def OnChoice(self, event):
        self.label.SetLabel("You selected " + self.choice.GetString
        (self.choice.GetSelection()) + " from Choice")


app = wx.App()
Mywin(None, 'Auswahlmenü')
app.MainLoop()
print(choice)