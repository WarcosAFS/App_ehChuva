from tkinter import *
from PIL import ImageTk, Image
import os
import time


class Login:
    def __init__(self, master= None):

######## CAMINHO E DIRETORIO ATUAL
        self.caminho_atual = os.path.abspath(__file__)
        self.diretorio_atual = os.path.dirname(self.caminho_atual)

######## CRIAR A AREA CANVAS
        self.canvas = Canvas(master, width = 360, height = 640, highlightthickness=0.5)
        self.canvas.pack()

######## COR DE FUNDO DO APLICATIVO
        self.caminho_chuva = os.path.join(self.diretorio_atual, 'Imagens/chuva.jpeg')
        self.abrir_chuva = Image.open(self.caminho_chuva)
        #self.chuva_resized = self.abrir_chuva.resize(())
        self.photo_chuva = ImageTk.PhotoImage(self.abrir_chuva)
        self.canvas.create_image(0,0, image = self.photo_chuva)

        #self.cor_de_fundo = self.canvas.create_rectangle(0,0, 360, 640, fill = '#D0D0D0')

######## ADICIONAR IMAGEM DO LOGO
        self.caminho_logo = os.path.join(self.diretorio_atual, 'Imagens/ehChuva_logo.png')
        self.abrir_logo = Image.open(self.caminho_logo)
        self.logo_resized = self.abrir_logo.resize((360,640))
        self.photo_logo = ImageTk.PhotoImage(self.logo_resized)
        self.canvas.create_image(180,110, image = self.photo_logo)

######## CRIAR BORDAS PARA AS ENTRADAS E OS BOTOES
        x1, x2 = 40, 80
        y1, y2 = 241, 287
        horizontal, vertical = 240, 110

        for i in range(3):
            self.canvas.create_oval(x1, y1, x2, y2, fill = 'white', outline = 'white')
            self.canvas.create_oval(x1, y1+vertical, x2, y2+vertical, fill = 'white', outline = 'white')
            self.canvas.create_oval(x1, y1+2*vertical, x2, y2+2*vertical, fill = '#5E9CE0', outline = '#5E9CE0')
            x1 += horizontal
            x2 += horizontal

######## PRÉ-TEXTO INDICATIVO NAS ENTRADAS DE NOME E SENHA
        def pretexto_nome(event):
            if self.nome_entry.get() == 'Nome...':
                self.nome_entry.delete(0, 'end')
            elif self.nome_entry.get() == '':
                self.nome_entry.insert(0, 'Nome...')

        def pretexto_senha(event):
            if self.senha_entry.get() == 'Senha...':
                self.senha_entry.delete(0, 'end')
                self.senha_entry['show'] = '*'
            elif self.senha_entry.get() == '':
                self.senha_entry.insert(0, 'Senha...')
                self.senha_entry['show'] = ''

######## ENTRADAS DE NOME E SENHA
        self.nome_entry = Entry(master, font = ("Lemon Milk", "30"), justify= 'center', width = 11, borderwidth=0, fg = 'grey')
        self.nome_entry.insert(0, 'Nome...')
        self.nome_entry.bind('<FocusIn>', pretexto_nome), self.nome_entry.bind('<FocusOut>', pretexto_nome)
        self.nome_entrada = self.canvas.create_window(60, 240.5, window = self.nome_entry, anchor = 'nw')

        self.senha_entry = Entry(master, font = ("Lemon Milk", "30"), justify= 'center', width = 11, borderwidth=0, fg = 'grey')
        self.senha_entry.insert(0, 'Senha...')
        self.senha_entry.bind('<FocusIn>', pretexto_senha), self.senha_entry.bind('<FocusOut>', pretexto_senha)
        self.senha_entrada = self.canvas.create_window(60, 350.5, window = self.senha_entry, anchor = 'nw')


######## MENSAGENS DE AVISO:     CAMPO VAZIO E LOGIN INVALIDO
        mensagem = self.canvas.create_text(180, 600, text = '', font = ("Arial", "12", "bold"), fill = 'red', justify = 'center')
        campo_nome_text = self.canvas.create_text(180, 296.9, text = '', font = ("Arial", "10"), fill = 'red', justify = 'center')
        campo_senha_text = self.canvas.create_text(180, 406.9, text = '', font = ("Arial", "10"), fill = 'red', justify = 'center')

######## AUTENTICAÇÃO DAS CREDENCIAIS
        def autenticar(event):
            Nome = self.nome_entry.get()
            Senha = self.senha_entry.get()
            self.canvas.itemconfig(mensagem, text = '')

            if Nome == 'Nome...' or not Nome:
                self.canvas.itemconfig(campo_nome_text, text = '*Campo Obrigatório*')
            else:
                self.canvas.itemconfig(campo_nome_text, text = '')
            if Senha == 'Senha...' or not Senha:
                self.canvas.itemconfig(campo_senha_text, text = '*Campo Obrigatório*')
            else:
                self.canvas.itemconfig(campo_senha_text, text = '')

            if Nome and Senha and Nome != 'Nome...' and Senha != 'Senha...':
                if Nome not in Nomes:
                    self.canvas.itemconfig(mensagem, text = 'Conta inexistente. Por favor, cadastre-se')
                elif Senha and Senha != 'Senha...' and Senha != Senhas[Nomes.index(Nome)]:
                    self.canvas.itemconfig(mensagem, text = 'A senha está incorreta')
                else:
                    self.canvas.itemconfig(mensagem, text = '')

######## BOTAO AUTENTICAR
        def cursor_in(event):
            self.canvas.configure(cursor='hand2')
        
        def cursor_out(event):
            self.canvas.configure(cursor='')

        self.botao_login = self.canvas.create_rectangle(60, 461.1, 300, 506.9, fill = '#5E9CE0', outline= '#5E9CE0')
        self.botao_login_text = self.canvas.create_text(180,485, text = 'Log In', font = ("Lemon Milk", "20"), justify = 'center')
        self.canvas.tag_bind(self.botao_login, '<Button-1>', autenticar), self.canvas.tag_bind(self.botao_login_text, '<Button-1>', autenticar)
        self.canvas.tag_bind(self.botao_login,'<Enter>', cursor_in), self.canvas.tag_bind(self.botao_login,'<Leave>', cursor_out)
        self.canvas.tag_bind(self.botao_login_text,'<Enter>', cursor_in)

######## REMOVER FOCO DAS ENTRADAS:
        def remover_foco(event):
             self.canvas.focus_set()

        self.canvas.bind('<Button-1>', remover_foco)



######## BOTAO CADASTRO


        self.cadastrar_text = self.canvas.create_text(180, 540, text = 'Não tem uma conta? Cadastre-se', font = ("Lemon Milk", "13", "bold"), justify = 'center', fill = 'green')
        self.canvas.tag_bind(self.cadastrar_text, '<Button-1>', cadastrar)
        self.canvas.tag_bind(self.cadastrar_text,'<Enter>', cursor_in), self.canvas.tag_bind(self.cadastrar_text,'<Leave>', cursor_out)

def tela_cadastro():
    login = Login(None)
    cadastro = Signup(root)
    root.mainloop()

root = Tk()
login = Login(root)
root.title('Login')


root.resizable(False, False)


Nomes = ['adm']
Senhas = ['adm']


root.geometry("360x640")
root.mainloop()


