from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox

window=Tk()
window.geometry("300x300")
window.title('WhatList')



class App:
    def __init__(self,window):
        self.window = window

        barra_Menu = Menu(self.window)

        barra_Menu.add_command(label="Página Inicial", command = self.home)
        barra_Menu.add_command(label="Notificações", command = self.notif)
        barra_Menu.add_command(label="Conta", command = self.conta)

        barra_Menu.add_command(label="Sair", command = window.quit)
        window.configure(menu=barra_Menu)

        lb1 = Label(window, text = "Login", font = ("Arial", 20))
        lb1.pack(side=TOP)

        idNome = Label(window, text="Nome", font =("Arial", 10))
        idNome.pack(side=TOP)
        txt_idNome = Entry(window, width=20)
        txt_idNome.pack(side=TOP)

        email = Label(window, text="Email", font =("Arial", 10))
        email.pack(side=TOP)
        txt_email = Entry(window, width=20)
        txt_email.pack(side=TOP)

        password = Label(window, text="Password", font =("Arial", 10))
        password.pack(side=TOP)
        txt_pass = Entry(window, width=20, show="*")
        txt_pass.pack(side=TOP)


        btn_auten = Button(window, text="Autenticar")
        btn_auten.pack(side=TOP)


    #cria uma janela para a Página inicial
    def home(self):
        top =Toplevel()
        top.geometry("700x300")
        top.title("WhatList")
        top.focus_force()
        top.grab_set()

        lb2 = Label(top, text="Caixa de entrada", font = ("Arial", 15))
        lb2.grid(column=1)
        
        btn_add = Button(top,text="Adicionar Tarefa")
        btn_add.grid(column=1)

        btn_comment = Button(top, text="Comentário")
        btn_comment.place(x=450,y=5)

        lista=["Não realizado", "Importante", "Em progresso"]
        btn_rank = Combobox(top, values=lista)
        btn_rank.place(x=550,y=5)

    #Cria uma janela para as notificações
    def notif(self):
        notifwindow =Toplevel()
        notifwindow.geometry("400x500")
        notifwindow.title("Notificações")
        notifwindow.focus_force()
        notifwindow.grab_set()

        lb3 = Label(notifwindow, text="Notificações", font = ("Arial", 20))
        lb3.pack(side=TOP)
    
    #Cria uma janela para a conta do utilizador
    def conta(self):
        contawin =Toplevel()
        contawin.geometry("700x300")
        contawin.title("WhatList")
        contawin.focus_force()
        contawin.grab_set()


App(window)

window.mainloop()