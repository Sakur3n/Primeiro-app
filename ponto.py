from tkinter import *
from tkinter import ttk
from time import strftime
import sqlite3
from datetime import datetime


tela = Tk()

class secundario:    
    def limpa_tela(self):
        self.projeto.delete(0, END)



    def conecta_bd(self):
        self.conn = sqlite3.connect("projetos.bd")
        self.cursor = self.conn.cursor()
    def desconectar_bd(self):
        self.conn.close()
    def montatabelas(self):
        self.conecta_bd() ; print('conectado')
        
        # Criar Tabela
        
        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS ponto(
                                nome_projeto CHAR(16),
                                horas TIMESTAMP
                            ) ;
                        ''')
        self.conn.commit() ; print ('BD criado')
        
        self.desconectar_bd() ; print ('BD desconectado')
    
    def add_projeto(self):
        
        self.project = self.projeto.get()
        self.hora = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
        
        self.conecta_bd()
        
        self.cursor.execute('''INSERT INTO ponto(nome_projeto, horas)
                            VALUES (?, ?)
                            
                            ''', (self.project, self.hora) )
        self.conn.commit()
        
        self.desconectar_bd()
        
        self.seleto()
        
        
    def seleto(self):
        self.proh.delete(*self.proh.get_children())
        
        self.conecta_bd()
        
        lista = self.cursor.execute('''
                                    SELECT nome_projeto, horas FROM ponto 
                                    ;
                                    ''')
        
        for i in lista:
            self.proh.insert('', END, values = i)
            
        self.desconectar_bd()
        self.limpa_tela()

class principal (secundario):
    
    def __init__(self):
        
        self.tela = tela
        self.tel()
        self.new_projeto()
        self.botao1()
        self.horario()
        self.tabela()
        self.montatabelas()
        self.seleto()

        tela.mainloop()

    def tel(self):
        self.tela.title('Ponto')
        self.tela.configure(background = '#155025255')
        self.tela.geometry('850x450')
        self.tela.maxsize(width = 1350, height = 720)
        self.tela.minsize(width = 550, height = 250 )
        
        self.div_1 = Frame (self.tela, bd= 4, bg= '#255255255')
        self.div_1.place (relx = 0.59, rely = 0.02, relwidth = 0.4, relheight = 0.96)
        
        self.div_2 = Frame (self.tela, bd= 4, bg= '#255255255')
        self.div_2.place (relx = 0.02, rely = 0.2, relwidth = 0.55, relheight = 0.17)
        
    def new_projeto(self):
        
        self.nproj = Label(tela, text = 'Nome do Projeto:', bg ='#155025255', fg = 'white', font = ('verdana', 8, 'bold'))
        self.nproj.place(relx = 0.02, rely = 0.08)
        self.projeto = Entry(tela, bg = '#266200266', fg = 'white')
        self.projeto.place(relx = 0.02, rely = 0.12, relheight = 0.06)

    def botao1 (self):
        self.incio = Button (tela, text = 'Inserir', bd=3, bg = '#255000255', fg = 'white', font = ('verdana', 8, 'bold'), padx = 1, pady = 1, command = self.add_projeto)
        self.incio.place (relx = 0.19, rely = 0.12, )
        self.incio.bind('<Return>', lambda event : self.add_projeto())
        
        ''' self.fim = Button (tela, text = ' Fim  ', bd=3, bg = '#255000255', fg = 'white', font = ('verdana', 8, 'bold'), padx = 1, pady = 1)
        self.fim.place (relx = 0.26, rely = 0.12)'''
        
        self.fechar_app = Button (tela, text = ' Fechar App  ', bd=3, bg = '#255000255', fg = 'white', font = ('verdana', 8, 'bold'), padx = 2, pady = 2, command = tela.destroy)
        self.fechar_app.place (relx = 0.02, rely = 0.93)

        self.projeto.bind("<Return>", lambda event: self.add_projeto())


    def horario(self):
        def hora_1 ():
            
            self.hora1 = strftime('%H: %M: %S')
            
            self.hora2 = self.hora1
                    
            hora =Label(self.div_2, text = 'Nome do Projeto:', bg ='#255255255', fg = '#857D76',font = ('verdana', 32, 'bold'))
            hora.place (relx = 0.2, rely = 0.01, relheight = 0.95, relwidth = 0.6)
            hora.config(text = self.hora1)
            hora.after(100, hora_1)
            
        hora_1 ()

    def tabela (self):
        #criando tabela
        self.proh = ttk.Treeview(self.div_1, height = 1, columns = ('col1','col2'))
        self.proh.place(relx=0.01, rely=0.01, relheight= 0.96, relwidth=0.94)
        
        #editando texto
        
        self.proh.heading('#1', text ='Projeto')
        self.proh.heading('#2', text ='Hora')
        self.proh.heading('#0', text ='')
        
        #editando coluna
        
        self.proh.column('#1', width = 80)
        self.proh.column('#2', width = 66)
        self.proh.column('#0', width = 0)


        #barra de rolagem

        self.barrinha = Scrollbar(self.div_1, orient = 'vertical')
        self.proh.configure( yscrollcommand = self.barrinha.set)
        self.barrinha.place(relx = 0.95, rely = 0.07, relheight = 0.90, relwidth =0.04)

principal()
