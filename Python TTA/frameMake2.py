import wx

class windowClass(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)

        self.basicGUI()

    def basicGUI(self):

        panel = wx.Panel(self)
        
        menuBar = wx.MenuBar()
        
        fileButton = wx.Menu()
        editButton = wx.Menu()
        importItem = wx.Menu()

        importItem.Append(wx.ID_ANY, "Import Document...")
        importItem.Append(wx.ID_ANY, "Import Picture...")
        importItem.Append(wx.ID_ANY, "Import Video...")

        fileButton.AppendMenu(wx.ID_ANY, 'Import', importItem)

        toolBar = self.CreateToolBar()
        quitToolButton = toolBar.AddLabelTool(wx.ID_ANY, 'Quit',
                                              wx.Bitmap(''))
        
        toolBar.Realize()
        self.Bind(wx.EVT_TOOL, self.Quit, quitToolButton)
        
        
        exitItem = wx.MenuItem(fileButton, wx.ID_EXIT, 'Quit\tCtrl+Q')
        #exitItem.SetBitmap(wx.Bitmap('quit.png'))
        fileButton.AppendItem(exitItem)


        
        menuBar.Append(fileButton, 'File')
        #menuBar.Append(fileButton, 'Edit')

        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)

        nameBox = wx.TextEntryDialog(None, 'What is your name?', 'Welcome', 'Ryan')

        if nameBox.ShowModal() == wx.ID_OK:
            userName = nameBox.GetValue()
            

        yesNoBox = wx.MessageDialog(None, 'Do you enjoy wxPython?', 'Question',wx.YES_NO)
        yesNoAnswer = yesNoBox.ShowModal()
        yesNoBox.Destroy()

        

        if yesNoAnswer == wx.ID_NO:
            userName = 'Loser!'

        chooseOneBox = wx.SingleChoiceDialog(None, 'What is your favorite color?',
                                             'Color Question',
                                             ['Green','Red','Blue','Yellow'])
        if chooseOneBox.ShowModal() == wx.ID_OK:
            favColor = chooseOneBox.GetStringSelection()




        wx.TextCtrl(panel, pos=(3,100), size=(150,50))

        aweText = wx.StaticText(panel, -1, "AwesomeText", (3,3))
        aweText.SetForegroundColour('yellow')
        aweText.SetBackgroundColour('black')

        rlyAweText = wx.StaticText(panel, -1, "Customized Awesomeness", (3,30))
        rlyAweText.SetForegroundColour(favColor)
        aweText.SetBackgroundColour('black')
        


            

        self.SetTitle('Welcome '+userName)
        self.Show(True)

    def Quit(self, e):
        self.Close()

def main():
    app = wx.App()
    windowClass(None)

    app.MainLoop()

main()

