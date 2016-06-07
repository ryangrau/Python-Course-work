import wx

class Frame(wx.Frame):
    def _init_(self, title):
        wx.Frame._init_(self, None, \
            title=title, size =(300,200))
        panel = wx.Panel(self)

        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        exitItem = fileMenu.Append(wx.NewId(), "Exit")
        menuBar.Append(fileMenu, "File")

        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.exitProgram, exitItem)

        self.CreateStatusBar()

    def exitProgram(self, event):
        self.Destroy()

app = wx.App()
frame = Frame("Python GUI")
frame.Show()
app.MainLoop()
