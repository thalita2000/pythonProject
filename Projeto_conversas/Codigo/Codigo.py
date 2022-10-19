from tkinter import *
from datetime import datetime
from tkinter import ttk

root = Tk()

class principal():
    def __init__(self):
        self.root = root
        self.tela()
        self.logo_1()
        self.botoes()
        self.etiquetas()

        root.mainloop()

    # Tela principal
    def tela(self):
        self.root.title("")
        self.root.configure(bg='#008888')
        self.root.geometry("1366x768+0+0")


    def logo_1(self):
        self.logo = PhotoImage(file=r'C:\Users\logger\PycharmProjects\pythonProject\Projeto_conversas\imagens\fotologo.png')
        self.logo = self.logo.subsample(2, 2)
        self.logo1 = Label(self.root, image=self.logo)
        self.logo1.image = self.logo

        self.logo = Label(self.root, image=self.logo)
        self.logo.place(x=500, y=50)

    def botoes(self):
        self.data = PhotoImage(file=r'C:\Users\logger\PycharmProjects\pythonProject\Projeto_conversas\imagens\data.png')
        self.data = self.data.subsample(4, 4)
        self.agenda1 = Label(self.root, image=self.data)
        self.agenda1.image = self.data

        self.data = Button(self.root, image=self.data, command=self.data_local)
        self.data.place(x=200, y=350)

        self.mensagem = PhotoImage(file=r'C:\Users\logger\PycharmProjects\pythonProject\Projeto_conversas\imagens\mensage.png')
        self.mensagem = self.mensagem.subsample(4, 4)
        self.mensagem1 = Label(self.root, image=self.mensagem)
        self.mensagem1.image = self.mensagem

        self.mensagem = Button(self.root, image=self.mensagem, command=self.msn)
        self.mensagem.place(x=550, y=350)

        self.etiquetas3 = Button(self.root, text='STATUS', bg='#008888', fg='yellow', font=('arial', 20, 'bold'), command=self.status)
        self.etiquetas3.place(x=900, y=375)

        #self.enviar = PhotoImage(file=r'C:\Users\logger\PycharmProjects\pythonProject\Projeto_conversas\imagens\enviar.png')
        #self.enviar = self.enviar.subsample(7, 7)
        #self.lupa1 = Label(self.root, image=self.enviar)
        #self.lupa1.image = self.enviar

        self.enviar = Button(self.root, text='ENVIAR', bg='#008888', fg='white', font=('arial', 20, 'bold'), command='')
        self.enviar.place(x=200, y=650)

        self.pesquisar = Button(self.root, text='PESQUISAR', bg='#008888', fg='white', font=('arial', 20, 'bold'), command='')
        self.pesquisar.place(x=500, y=650)

        self.pesquisar = Button(self.root, text='LIMPAR', bg='#008888', fg='white', font=('arial', 20, 'bold'), command='')
        self.pesquisar.place(x=850, y=650)

    def etiquetas(self):
        self.etiquetas1 = Label(self.root, text='DATA', bg='#008888', fg='yellow', font=('arial', 20, 'bold'))
        self.etiquetas1.place(x=220, y=485)

        self.etiquetas2 = Label(self.root, text='MENSAGENS', bg='#008888', fg='yellow', font=('arial', 20, 'bold'))
        self.etiquetas2.place(x=525, y=485)

    def data_local(self):
        self.dia_atual = (datetime.today().strftime('%d/%m/%Y'))

        self.TextoLabel = StringVar()
        self.TextoLabel.set(self.dia_atual)

        self.entry_datalocal = Entry(self.root, textvariable=f'{self.TextoLabel}', bg='#008888', fg='white', font=('arial', 18, 'bold'), relief=FLAT)
        self.entry_datalocal.place(x=200, y=550, width=120, height=35)

    def msn(self):
        self.entry_texto = Text(self.root, bg='#008888', fg='white',  font=('arial', 10, 'bold'))
        self.entry_texto.place(x=450, y=533, width=330, height=100)
        self.entry_texto.focus_force()

    def status(self):
        self.status_msn = ttk.Combobox(self.root, font=('arial', 13, 'bold'), values=["Pendente", "Aberto", "Em Espera", "Respondido", "Ignorado"])
        self.status_msn.current(0)
        self.status_msn.place(x=905, y=440, width=125, height=25)

principal()