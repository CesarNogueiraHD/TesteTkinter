from Usuarios import Usuarios
from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Verdana", "8")

        # Container 1
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()

        # Container 2
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()

        # Container 3
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()

        # Container 4
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()

        # Container 5
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()

        # Container 6
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()

        # Container 7
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()

        # Container 8
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()

        # Container 9
        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()

        # Container 1
        self.titulo = Label(self.container1, text="Informe os dados: ")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()

        # Container 2
        self.lblidusuario = Label(self.container2, text="idUsuario: ", font=self.fontePadrao, width=10)
        self.lblidusuario.pack(side=LEFT)

        self.txtidusuario = Entry(self.container2)
        self.txtidusuario["width"] = 10
        self.txtidusuario["font"] = self.fontePadrao
        self.txtidusuario.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fontePadrao, width=10)
        self.btnBuscar["command"] = self.buscarUsuario
        self.btnBuscar.pack(side=RIGHT)

        self.btnBuscarTodos = Button(self.container2, text="Buscar Todos", font=self.fontePadrao, width=10)
        self.btnBuscarTodos["command"] = self.buscarTodos
        self.btnBuscarTodos.pack()

        # Container 3
        self.lblnome = Label(self.container3, text="Nome: ", font=self.fontePadrao, width=10)
        self.lblnome.pack(side=LEFT)

        self.txtnome = Entry(self.container3)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fontePadrao
        self.txtnome.pack(side=LEFT)

        # Container 4
        self.lbltelefone = Label(self.container4, text="Telefone: ", font=self.fontePadrao, width=10)
        self.lbltelefone.pack(side=LEFT)

        self.txttelefone = Entry(self.container4)
        self.txttelefone["width"] = 25
        self.txttelefone["font"] = self.fontePadrao
        self.txttelefone.pack(side=LEFT)

        # Container 5
        self.lblemail = Label(self.container5, text="E-mail: ", font=self.fontePadrao, width=10)
        self.lblemail.pack(side=LEFT)

        self.txtemail = Entry(self.container5)
        self.txtemail["width"] = 25
        self.txtemail["font"] = self.fontePadrao
        self.txtemail.pack(side=LEFT)

        # Container 6
        self.lblusuario = Label(self.container6, text="Usuário: ", font=self.fontePadrao, width=10)
        self.lblusuario.pack(side=LEFT)

        self.txtusuario = Entry(self.container6)
        self.txtusuario["width"] = 25
        self.txtusuario["font"] = self.fontePadrao
        self.txtusuario.pack(side=LEFT)

        # Container 7
        self.lblsenha = Label(self.container7, text="Senha: ", font=self.fontePadrao, width=10)
        self.lblsenha.pack(side=LEFT)

        self.txtsenha = Entry(self.container7)
        self.txtsenha["width"] = 25
        self.txtsenha["show"] = "*"
        self.txtsenha["font"] = self.fontePadrao
        self.txtsenha.pack(side=LEFT)

        # Container 8
        self.btnInsert = Button(self.container8, text="Inserir", font=self.fontePadrao, width=12)
        self.btnInsert["command"] = self.inserirUsuario
        self.btnInsert.pack(side=LEFT)

        self.btnAlterar = Button(self.container8, text="Alterar", font=self.fontePadrao, width=12)
        self.btnAlterar["command"] = self.alterarUsuario
        self.btnAlterar.pack(side=LEFT)

        self.btnExcluir = Button(self.container8, text="Excluir", font=self.fontePadrao, width=12)
        self.btnExcluir["command"] = self.excluirUsuario
        self.btnExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

    def inserirUsuario(self):
        user = Usuarios()

        user.nome = self.txtnome.get()
        user.telefone = self.txttelefone.get()
        user.email = self.txtemail.get()
        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()

        self.lblmsg["text"] = user.insertUser()

        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)

    def alterarUsuario(self):
        user = Usuarios()

        user.idusuario = self.txtidusuario.get()
        user.nome = self.txtnome.get()
        user.telefone = self.txttelefone.get()
        user.email = self.txtemail.get()
        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()

        self.lblmsg["text"] = user.updateUser()

        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)

    def excluirUsuario(self):
        user = Usuarios()

        user.idusuario = self.txtidusuario.get()

        self.lblmsg["text"] = user.deleteUser()

        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)

    def buscarUsuario(self):
        user = Usuarios()

        idusuario = self.txtidusuario.get()

        self.lblmsg["text"] = user.selectUser(idusuario)

        self.txtidusuario.delete(0, END)
        self.txtidusuario.insert(INSERT, user.idusuario)

        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, user.nome)

        self.txttelefone.delete(0, END)
        self.txttelefone.insert(INSERT, user.telefone)

        self.txtemail.delete(0, END)
        self.txtemail.insert(INSERT, user.email)

        self.txtusuario.delete(0, END)
        self.txtusuario.insert(INSERT, user.usuario)

        self.txtsenha.delete(0, END)
        self.txtsenha.insert(INSERT, user.senha)

    def buscarTodos(self):
        user = Usuarios()
        self.lblmsg["text"] = user.lerTudo()

root = Tk()
Application(root)
root.mainloop()