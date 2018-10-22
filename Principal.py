import wx
APP_EXIT = 1
class Principal(wx.Frame):
    #Construtor da classe
    #def __init__(self, parent, id):
    def __init__(self, *args, **kwargs):
        super(Principal, self).__init__(*args, **kwargs)    

        self.InitMenuBar()
        self.criaPainel()
    
    def InitMenuBar(self):

        #Criando barra de menu na interface
        menuBar = wx.MenuBar()
        #Cria um objeto menubar
        fileMenu = wx.Menu()

        #Cria os itens do menu
        fileMenu.Append(wx.ID_NEW, '&Novo')
        fileMenu.Append(wx.ID_OPEN, '&Open')
        fileMenu.Append(wx.ID_SAVE, '&Save')
        fileMenu.AppendSeparator()

        #Itens do submenu
        imp = wx.Menu()
        imp.Append(wx.ID_ANY, 'Importar newfeed list')
        imp.Append(wx.ID_ANY, 'Importar bookmarks')
        imp.Append(wx.ID_ANY, 'Importar main')

        fileMenu.AppendMenu(wx.ID_ANY, '&Import', imp)
        #Cria um item do menu com o nome 'sair' (ID = item do menu, 'título', 'string de ajuda curta na barra de status')
        #fileItem = fileMenu.Append(wx.ID_EXIT, 'Sair', '&Quit\tCtrl+Q')
        #Adicionando ícone
        qmi = wx.MenuItem(fileMenu, APP_EXIT, '&Quit\tCtrl+Q')
        #qmi.SetBitmap(wx.Bitmap('exit.png'))
        fileMenu.Append(qmi)
        self.Bind(wx.EVT_MENU, self.fechar, id=APP_EXIT)

        #Insere o item de menu com o nome passado como segundo parâmetro (& indica que o menu pode ser acessado com Alt+F, um atalho)
        menuBar.Append(fileMenu, '&Opções')
        #Insere o menu o frame
        self.SetMenuBar(menuBar)

        self.SetSize(500, 400)
        self.SetTitle('PyPerf')
        self.Center()

    def criaPainel(self):
        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(5, 5)
        #Cria o box para os comandos personalizados
        sb = wx.StaticBox(panel, label="Optional Attributes")
        #Cria o tamanho da box
        boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)

        boxsizer.Add(wx.CheckBox(panel, label="Comando 1"), flag=wx.LEFT|wx.TOP, border=5)
        boxsizer.Add(wx.CheckBox(panel, label="Comando 2"), flag=wx.LEFT, border=5)
        boxsizer.Add(wx.CheckBox(panel, label="Comando 3"), flag=wx.LEFT, border=5)
        boxsizer.Add(wx.CheckBox(panel, label="Comando 4"), flag=wx.LEFT, border=5)
        boxsizer.Add(wx.CheckBox(panel, label="Comando 5"), flag=wx.LEFT|wx.BOTTOM, border=5)
        sizer.Add(boxsizer, pos=(7, 0), span=(1, 5), flag=wx.TOP|wx.LEFT|wx.RIGHT , border=10)

        sizer.AddGrowableCol(1)

        panel.SetSizer(sizer)
        #Ocupa somente o espaço necessário (dde acordo com a quantidade de elementos na tela)
        #sizer.Fit(self)

    def fechar(self, event):
        self.Close()
    
    #Método do botão fechar
    def closebutton(self, event):
        self.Close(True)
    
    #Método para fechar a janela
    def closewindow(self, event):
        self.Destroy()

def main():
    app = wx.App()
    ex = Principal(None, title="Create Java Class")
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()