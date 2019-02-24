from tkinter import *
import sys
import os


class AccentureLogin:
    def __init__(self, master=None):
        self.caminhoLocal = os.path.abspath(os.path.dirname(sys.argv[0]))
        self.caminhoLocal = self.caminhoLocal.replace(r'\\', '/')
        self.mensagem = None
        self.cor = "#f8f7f9"
        self.cor2 = "#00A4FF"
        self.cor3 = "#1f1f1f"
        self.root = Tk()
        self.root.lift()
        self.root.configure(background=self.cor3)
        self.root.focus_force()
        self.root.bind("<Escape>", self.pressiona_esc)
        self.fonte_padrao = ("Century Gothic", "13")
        self.texto_verificador = ""
        self.usuario_classe = ""
        self.senha_classe = ""
        self.captcha_classe = ""
        self.vpn_classe = False
        self.sucesso = False
        self.cancela = False
        self.imagem = PhotoImage(file="static/imagens/logo-vegans2go.png")
        self.imagem_label = Label(self.root, image=self.imagem, background=self.cor3)
        self.imagem_label.imagem = self.imagem
        self.imagem_label["height"] = 230
        self.imagem_label["width"] = 440
        self.imagem_label.pack()

        self.container1 = Frame(master)
        self.container1.configure(background=self.cor2)
        self.container1["pady"] = 15
        self.container1["padx"] = 56
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2.configure(background=self.cor3)
        self.container2["pady"] = 10
        self.container2.pack()

        self.titulo = Label(self.container1, text="", background=self.cor2, foreground=self.cor3)
        self.titulo["font"] = ("Century Gothic", "23")
        self.titulo.pack()

        self.inserir_label = Label(self.container2, text=" Inserir: ", font=self.fonte_padrao, background=self.cor3, foreground=self.cor)
        self.inserir_label["pady"] = 5
        self.inserir_label.grid(row=0, column=1, sticky=W)

        self.inserir = Entry(self.container2)
        self.inserir["width"] = 30
        self.inserir["show"] = "*"
        self.inserir["font"] = self.fonte_padrao
        self.inserir.bind("<Return>", self.pressiona_enter)
        self.inserir.bind("<Escape>", self.pressiona_esc)
        self.inserir.grid(row=0, column=2, sticky=W)

        self.editar_label = Label(self.container2, text=" Editar:", font=self.fonte_padrao, background=self.cor3, foreground=self.cor)
        self.editar_label["pady"] = 5
        self.editar_label.grid(row=1, column=1, sticky=W)

        self.editar = Entry(self.container2)
        self.editar["width"] = 30
        self.editar["show"] = "*"
        self.editar["font"] = self.fonte_padrao
        self.editar.bind("<Return>", self.pressiona_enter)
        self.editar.bind("<Escape>", self.pressiona_esc)
        self.editar.grid(row=1, column=2, sticky=W)

        self.captcha = Entry(self.container2)
        self.captcha["width"] = 17
        self.captcha["font"] = self.fonte_padrao
        self.captcha.bind("<Return>", self.pressiona_enter)
        self.captcha.bind("<Escape>", self.pressiona_esc)
        self.captcha.grid(row=3, column=2, sticky=W)

        self.mensagem = Label(self.container2, text="", font=self.fonte_padrao, background=self.cor3, foreground=self.cor)
        self.mensagem["pady"] = 5
        self.mensagem.grid(row=4, column=1, columnspan=2)

        self.vpn = StringVar(self.root)
        self.box = Checkbutton(self.container2, text="V", variable=self.vpn, activebackground=self.cor3,
                               activeforeground=self.cor, bg=self.cor3, fg=self.cor, selectcolor=self.cor3, tristatevalue=0)
        self.box["font"] = self.fonte_padrao
        self.box.grid(row=5, column=2, sticky=W)

        self.iniciar = Button(self.container2)
        self.iniciar["text"] = "Concluído"
        self.iniciar["font"] = self.fonte_padrao
        self.iniciar["width"] = 9
        self.iniciar["command"] = self.teste
        self.iniciar.grid(row=6, column=2, sticky=W, pady=30)

        self.iniciar = Button(self.container2)
        self.iniciar["text"] = "Cancelar"
        self.iniciar["font"] = self.fonte_padrao
        self.iniciar["width"] = 9
        self.iniciar["command"] = self.pressiona_esc
        self.iniciar.grid(row=6, column=2, sticky=E, pady=30)

    def pressiona_enter(self, event):
        self.verifica_codigo()

    def pressiona_esc(self, event=None):
        self.cancela = True
        self.root.destroy()

    def verifica_codigo(self):
        senha_digitada = self.editar.get()
        captcha_digitado = self.captcha.get()
        vpn_marcada = self.vpn.get()
        if senha_digitada == "":
            self.mensagem["text"] = "Favor informar a Senha de acesso!"
        elif captcha_digitado == "":
            self.mensagem["text"] = "Favor informar o Captcha de acesso!"
        else:
            self.senha_classe = senha_digitada
            self.captcha_classe = captcha_digitado
            self.vpn_classe = vpn_marcada
            self.sucesso = True
            self.root.destroy()

    def teste(self, master2=None):
        root2 = Tk()
        root2.lift()
        root2.configure(background=self.cor3)
        root2.focus_force()
        root2.bind("<Escape>", self.pressiona_esc)
        fonte_padrao = ("Century Gothic", "13")

        container1 = Frame(master2)
        container1.configure(background=self.cor2)
        container1["pady"] = 15
        container1["padx"] = 56
        container1.pack()

        container2 = Frame(master2)
        container2.configure(background=self.cor3)
        container2["pady"] = 10
        container2.pack()

        titulo = Label(container1, text="", background=self.cor2, foreground=self.cor3)
        titulo["font"] = ("Century Gothic", "23")
        titulo.pack()

        inserir_label = Label(container2, text=" Inserir: ", font=fonte_padrao, background=self.cor3, foreground=self.cor)
        inserir_label["pady"] = 5
        inserir_label.grid(row=0, column=1, sticky=W)

        inserir = Entry(container2)
        inserir["width"] = 30
        inserir["show"] = "*"
        inserir["font"] = fonte_padrao
        inserir.bind("<Return>", self.pressiona_enter)
        inserir.bind("<Escape>", self.pressiona_esc)
        inserir.grid(row=0, column=2, sticky=W)

        editar_label = Label(container2, text=" Editar:", font=fonte_padrao, background=self.cor3, foreground=self.cor)
        editar_label["pady"] = 5
        editar_label.grid(row=1, column=1, sticky=W)

        editar = Entry(container2)
        editar["width"] = 30
        editar["show"] = "*"
        editar["font"] = fonte_padrao
        editar.bind("<Return>", self.pressiona_enter)
        editar.bind("<Escape>", self.pressiona_esc)
        editar.grid(row=1, column=2, sticky=W)

        captcha = Entry(container2)
        captcha["width"] = 17
        captcha["font"] = fonte_padrao
        captcha.bind("<Return>", self.pressiona_enter)
        captcha.bind("<Escape>", self.pressiona_esc)
        captcha.grid(row=3, column=2, sticky=W)

        mensagem = Label(container2, text="", font=fonte_padrao, background=self.cor3, foreground=self.cor)
        mensagem["pady"] = 5
        mensagem.grid(row=4, column=1, columnspan=2)

        vpn = StringVar(root2)
        box = Checkbutton(container2, text="V", variable=vpn, activebackground=self.cor3,
                          activeforeground=self.cor, bg=self.cor3, fg=self.cor, selectcolor=self.cor3, tristatevalue=0)
        box["font"] = fonte_padrao
        box.grid(row=5, column=2, sticky=W)

        iniciar = Button(container2)
        iniciar["text"] = "Concluído"
        iniciar["font"] = fonte_padrao
        iniciar["width"] = 9
        iniciar["command"] = self.verifica_codigo
        iniciar.grid(row=6, column=2, sticky=W, pady=30)

        iniciar = Button(container2)
        iniciar["text"] = "Cancelar"
        iniciar["font"] = fonte_padrao
        iniciar["width"] = 9
        iniciar["command"] = self.pressiona_esc
        iniciar.grid(row=6, column=2, sticky=E, pady=30)


AccentureLogin()
