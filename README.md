# pythonProject
from tkinter import *
from datetime import datetime
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar

import os
import sqlite3
import csv

root = Tk()

class Funcoes():
    def pesquisar_msn2(self):
        self.lista_mensagem.delete(*self.lista_mensagem.get_children())
        self.abrir_banco()

        nome = '%' + self.entry_codigo2.get()

        self.cursor.execute("""SELECT * FROM chat1 WHERE id LIKE '%s' COLLATE NOCASE ORDER BY id ASC""" % nome)
        resultado_busca = self.cursor.fetchall()
        self.limpar_campos()

        for self.cliente in resultado_busca:
           self.lista_mensagem.insert("", END, values= self.cliente)

        self.fechar_banco()

    def pesquisar_msn(self):
        self.lista_mensagem.delete(*self.lista_mensagem.get_children())
        self.abrir_banco()

        nome = '%' + self.entry_codigo2.get()

        self.cursor.execute("""SELECT * FROM chat1 WHERE id LIKE '%s' COLLATE NOCASE ORDER BY id ASC""" % nome)
        resultado_busca = self.cursor.fetchmany()
        self.limpar_campos()

        for self.cliente in resultado_busca:
           self.lista_mensagem.insert("", END, values= self.cliente)

        self.fechar_banco()

    def pesquisa(self):
        self.limpar_campos()

        self.root2 = Toplevel()

        self.root2.configure(background='#00aa88')
        self.root2.geometry('800x350+280+77')

        self.widgets2()

    def widgets2(self):
        self.grid_root2()

        self.logo = PhotoImage(file=r'C:\Users\Junior\pythonProject\dialogue\imagens\fotologo.png')
        self.logo = self.logo.subsample(3, 3)
        self.logo1 = Label(self.root2, image=self.logo)
        self.logo1.image = self.logo

        self.logo = Label(self.root2, image=self.logo)
        self.logo.place(x=580, y=40)

        self.lb_codigo = Label(self.root2, text='DIGITA O CÓDIGO DA MENSAGEM', bg='#00aa88', fg='white', font=('arial', 13, 'bold'))
        self.lb_codigo.place(x=10, y=10)

        self.entry_codigo2 = Entry(self.root2, bg='#00aa88', fg='white', font=('arial', 15, 'bold'))
        self.entry_codigo2.place(x=290, y=10, width=70, height=25)

        self.bt_clica = Button(self.root2, text='oK', bg='#00aa88', fg='white', font=('arial', 8, 'bold'), command=self.pesquisar_msn)
        self.bt_clica.place(x=350, y=10)

        self.lb_clica = Label(self.root2, text='LISTAR TODAS AS MENSAGENS', bg='#00aa88', fg='white', font=('arial', 13, 'bold'))
        self.lb_clica.place(x=10, y=50)

        self.bt_clica2 = Button(self.root2, text='oK', bg='#00aa88', fg='white', font=('arial', 8, 'bold'), command=self.pesquisar_msn2)
        self.bt_clica2.place(x=280, y=50)

    def grid_root2(self):
        self.lista_mensagem = ttk.Treeview(self.root2, columns=('col0', 'col1', 'col2', 'col3', 'col4'))
        self.lista_mensagem.heading("#0", text='')
        self.lista_mensagem.heading("#1", text='CÓDIGO')
        self.lista_mensagem.heading("#2", text='DATA LOCAL')
        self.lista_mensagem.heading("#3", text='STATUS')
        self.lista_mensagem.heading("#4", text='MENSAGEM')

        self.lista_mensagem.column("#0", width=0)
        self.lista_mensagem.column("#1", width=60)
        self.lista_mensagem.column("#2", width=100)
        self.lista_mensagem.column("#3", width=75)
        self.lista_mensagem.column("#4", width=500)

        self.lista_mensagem.place(x=20, y=160, width=750, height=170)
        self.lista_mensagem.bind("<Double-1>", self.click_mensagem)

    def click_mensagem(self, e):
        self.limpar_campos()
        self.lista_mensagem.selection()

        for x in self.lista_mensagem.selection():
            col1, col2, col3, col4 = self.lista_mensagem.item(x, 'values')
            self.entry_id.insert(END, col1)
            self.entry_datalocal.insert(END, col2)
            self.status_msn.insert(END, col3)
            self.entry_texto.insert(END, col4)

            self.root2.destroy()

    def limpar_campos(self):
        self.entry_id.delete(0, END)
        self.entry_datalocal.delete(0, END)
        self.entry_texto.delete('1.0', END)
        self.status_msn.delete(0, END)

    def abrir_banco(self):
        self.conexao = sqlite3.connect('portar.sqlite3')
        self.cursor = self.conexao.cursor()

    def fechar_banco(self):
        self.conexao.close()

    def tabela(self):
        self.abrir_banco()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat1 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT NOT NULL,     
        status TEXT NOT NULL,
        mensagens TEXT NOT NULL
        );""");

        self.conexao.commit()
        self.fechar_banco()

    def capturar_campos(self):

        try:
            self.cod = self.entry_id.get()
            self.data = self.entry_datalocal.get()
            self.status = self.status_msn.get()
            self.mensagens = self.entry_texto.get('1.0', END)

        except:
            pass

    def inserir_dados(self):
        self.capturar_campos()
        self.abrir_banco()

        if self.entry_datalocal.get() == '':
            msg = '      PARA ENVIAR UMA MENSAGEM,\nÉ NECESSÁRIO CLICAR NO BOTÃO DATA'
            messagebox.showwarning('MENSAGEM',msg)

        else:
            self.abrir_banco()
            self.cursor.execute("""INSERT INTO chat1 (data, status, mensagens)
            VALUES (?,?,?) """, ((self.data, self.status, self.mensagens)))

            self.conexao.commit()
            self.fechar_banco()
            self.limpar_campos()
            self.gerar_csv()

    def gerar_csv(self):

        self.arq = self.data, self.status, self.mensagens

        # 1. cria o arquivo
        with open('conversations-300.csv', 'a', newline='', encoding='utf-8') as f:
            # 2. cria o objeto de gravação
            w = csv.writer(f, lineterminator='\r\n')

            # 3. grava as linhas
            w.writerow({self.arq})

    def listar_csv(self):
        os.startfile('conversations-300.csv')

    def terminal_csv(self):
        try:
            # 1. abrir o arquivo
            with open('conversations-300.csv', encoding='utf-8') as arquivo_csv:
                # 2. ler a tabela
                self.tabela = csv.reader(arquivo_csv, delimiter=',')

                # 3. navegar pela tabela
                for l in self.tabela:

                    print(l)
        except:
            pass

class principal(Funcoes):
    def __init__(self):
        self.root = root
        self.tabela()
        self.tela()
        self.logo_1()
        self.widgets()
        self.menus()

        root.mainloop()

    # Tela principal
    def tela(self):
        self.cores_widgets()
        self.root.title("")
        self.root.configure(bg=self.tela)
        self.root.geometry("1366x768+0+0")

    def cores_widgets(self):
        self.tela = 'white'
        self.botao = '#0055d4'
        self.fonte_b = 'white'
        self.fonte_P = 'black'
        self.label = 'white'
        self.text1 = '#c8c4b7'

    def logo_1(self):
        self.logo = PhotoImage(file=r'C:\Users\Junior\pythonProject\dialogue\imagens\fotologo.png')
        self.logo = self.logo.subsample(1, 1)
        self.logo1 = Label(self.root, image=self.logo)
        self.logo1.image = self.logo

        self.logo = Label(self.root, image=self.logo)
        self.logo.place(x=380, y=80)

    def widgets(self):
        self.cores_widgets()

        self.dialogo = Label(self.root, text='I n s i g h t s', bg=self.tela, fg='#0055d4', font=('arial black', 45, 'bold'))
        self.dialogo.place(x=460, y=0)

        self.lb_codigo = Label(self.root, text='Código da Mensagem:', bg=self.tela, fg='#000080', font=('arial', 15, 'bold'))
        self.lb_codigo.place(x=10, y=10)

        self.entry_id = Entry(self.root, bg=self.tela, fg=self.fonte_P, font=('arial', 15, 'bold'), relief=FLAT)
        self.entry_id.place(x=240, y=10, width=100, height=25)

        self.data = Button(self.root, text='DATA', bg=self.botao, fg='white', font=('arial', 15, 'bold'), command=self.data_local)
        self.data.place(x=30, y=150)

        self.entry_datalocal = Entry(self.root, bg=self.tela, fg=self.fonte_P, font=('arial', 18, 'bold'), relief=FLAT)
        self.entry_datalocal.place(x=110, y=155, width=120, height=35)

        self.opcao = Label(self.root, text='STATUS', bg=self.botao, fg=self.fonte_b, font=('arial', 15, 'bold'))
        self.opcao.place(x=30, y=225)

        self.status_msn = ttk.Combobox(self.root, font=('arial', 13, 'bold'),
                                       values=["Pendente", "Aberto", "Em Espera", "Respondido", "Ignorado"])
        self.status_msn.current(0)
        self.status_msn.place(x=30, y=260, width=125, height=25)

        self.enviar = Button(self.root, text='ENVIAR', bg=self.botao, fg='white', font=('arial', 20, 'bold'), command=self.inserir_dados)
        self.enviar.place(x=200, y=650)

        self.pesquisar = Button(self.root, text='PESQUISAR', bg=self.botao, fg='white', font=('arial', 20, 'bold'), command=self.pesquisa)
        self.pesquisar.place(x=500, y=650)

        self.limpar = Button(self.root, text='LIMPAR', bg=self.botao, fg='white', font=('arial', 20, 'bold'), command=self.limpar_campos)
        self.limpar.place(x=850, y=650)

        self.mensagem = Label(self.root, text='MENSAGEM:', bg=self.tela, fg='#000080', font=('arial', 25, 'bold'))
        self.mensagem.place(x=30, y=380)

        self.entry_texto = Text(self.root, bg=self.text1, fg='#0000aa', font=('arial', 20, 'bold'))
        self.entry_texto.place(x=30, y=433, width=1200, height=150)

    def calendario(self):

        self.calendar_local = Calendar(self.root, locale='pt_br')
        self.calendar_local.place(x=900, y=60)

    def data_local(self):
        self.dia_atual = (datetime.today().strftime('%d/%m/%Y'))

        self.TextoLabel = StringVar()
        self.TextoLabel.set(self.dia_atual)

        self.entry_datalocal = Entry(self.root, textvariable=self.TextoLabel, bg=self.tela, fg='#0000aa', font=('arial', 18, 'bold'), relief=FLAT)
        self.entry_datalocal.place(x=110, y=155, width=120, height=35)

    def status(self):
        self.status_msn = ttk.Combobox(self.root, fg='#0000aa', font=('arial', 13, 'bold'), values=["Pendente", "Aberto", "Em Espera", "Respondido", "Ignorado"])
        self.status_msn.current(1)
        self.status_msn.place(x=30, y=260, width=125, height=25)

    def menus(self):
        menubar = Menu(self.root)

        self.root.config(menu=menubar)
        filemenu1 = Menu(menubar, tearoff=0)

        menubar.add_cascade(label='Funções', menu=filemenu1)
        filemenu1.add_command(label='Listar CSV', command=self.listar_csv)
        filemenu1.add_command(label='CSV no terminal', command=self.terminal_csv)
        filemenu1.add_command(label='Calendário', command=self.calendario)

principal()
