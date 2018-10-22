import wx


APP_EXIT = 1

class Principal(wx.Frame):

    #Construtor da classe
    #def __init__(self, parent, id):
    def __init__(self, *args, **kwargs):
        super(Principal, self).__init__(*args, **kwargs)    

        self.InitUI()
    
    def InitUI(self):

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

        #Cria um frame
        #wx.Frame.__init__(self, parent, id, 'PyPerf - Interjato', size=(500, 400))
        #Insere o 'contexto' no painel
        #panel=wx.Panel(self)
        #Cria um botão dentro do painel, com o nome exit na posição e tamanho informados
        #button=wx.Button(panel, label='Exit', pos=(300, 300), size=(60, 30))
        #Insere um evento no botão, indica qual função irá chamar ao ser clicado e informa o 'quem é o botão'
        #self.Bind(wx.EVT_BUTTON, self.closebutton, button)
        #Insere o evento close e chama a função para encerrar a janela como segundo evento
        #self.Bind(wx.EVT_CLOSE, self.closewindow) 



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
    ex = Principal(None)
    ex.Show()
    app.MainLoop()

if __name__=='__main__':
    main()