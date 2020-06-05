from tkinter import *

class Application:
    def __init__(self, master=None):
        #self.widget = Frame(master)
        #self.widget.pack()
        #self.msg = Label(self.widget, text="Ola mundo em Tkinter")
        #self.msg.pack()

        self.widget1 = Frame(master)
        self.widget1.pack(side=RIGHT)

        self.msg = Label(self.widget1, text="Segundo código em Tkinter")
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        self.msg.pack(side=RIGHT)

        self.sair = Button(self.widget1)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 10
        self.sair["command"] = self.widget1.quit
        self.sair.pack()

        self.mudaTexto = Button(self.widget1)
        self.mudaTexto["text"] = "CLique aqui"
        self.mudaTexto["font"] = ("Calibri", "12")
        self.mudaTexto["width"] = 12
        self.mudaTexto.bind("<Button-1>", self.mudarTexto)
        self.mudaTexto.pack()

    def mudarTexto(self, event):
        if self.msg["text"] == "Segundo código em Tkinter":
            self.msg["text"] = "O botão recebeu um clique"
        else:
            self.msg["text"] = "Segundo código em Tkinter"

root = Tk()
Application(root)
root.mainloop()