import customtkinter as ctk
from tkinter import *
from tkinter import messagebox



#funções

def adicionar_contato():
    contato = f'Nome: {entrada_nome.get()}  \n Telefone:{entrada_telefone.get()}  E-Mail:{entrada_email.get()}'
    if contato:
        lista_contatos.insert(0, contato)
        entrada_nome.delete(0, END)
        entrada_telefone.delete(0, END)
        entrada_email.delete(0, END)
        salvar_contato()
    else:
        messagebox.showerror('Erro', 'Digite um contato para adicionar.')

def remover_contato():
        selecao = lista_contatos.curselection()
        
        if selecao:
            lista_contatos.delete(selecao)
            salvar_contato()
        else:
            messagebox.showerror('Erro', 'Por favor, escolha um contato para remover.')


def salvar_contato():
    with open('contatos.txt', 'w') as t:
        contatos = lista_contatos.get(0, END)
        for i in contatos:
            t.write(i + '\n')
            
def carregar_contatos():
        with open('contatos.txt', 'r') as t:
            contatos = t.readlines()
            for i in contatos:
                lista_contatos.insert(0,i.strip())
    

# ----- default style
ctk.set_appearance_mode('dark')
app = ctk.CTk()
app.geometry('500x800')
app.title('TO-DO List')

#----root style
fontH1 = ('Arial', 24, 'bold')
fontH2 = ('Arial', 18, 'bold')
fontH3 = ('Arial', 14, 'bold')
fontP = ('Arial', 12, 'bold')

# Title
ctk.CTkLabel(app,text='Agenda de Contatos',
             text_color='white',font=fontH1).pack(pady=5)

ctk.CTkLabel(app,text='No campo abaixo, \n adicione as informações de contato',
             text_color='white',font=fontH2).pack(pady=5)

# entrada de nome

ctk.CTkLabel(app, text='Nome',
             text_color='white',
             font=fontH3).place(x=30, y=95)
entrada_nome = ctk.CTkEntry(app, font=fontP,
                             width=300, height=20)
entrada_nome.place(x=100, y=100)

# entrada de telefone
ctk.CTkLabel(app, text='Telefone',
             text_color='white',
             font=fontH3).place(x=30, y=125)
entrada_telefone = ctk.CTkEntry(app, font=fontP,
                             width=300, height=20)
entrada_telefone.place(x=100, y=130)

# entrada de em
ctk.CTkLabel(app, text='E-mail',
             text_color='white',
             font=fontH3).place(x=30, y=155)
entrada_email = ctk.CTkEntry(app, font=fontP,
                             width=300, height=20)
entrada_email.place(x=100, y=160)



# Botão para adicionar
button_adicionar = ctk.CTkButton(app, text='Adicionar Contato',
                              font=fontH3, text_color='white',
                               fg_color='green', cursor='hand2',
                              width=135,corner_radius=5, hover_color='darkgreen',
                              command=adicionar_contato
                              )
button_adicionar.place(x=60, y=220)


# Botão para remover
button_remove = ctk.CTkButton(app, text='Remover Contato',
                              font=fontH3, text_color='white',
                              fg_color='red', cursor='hand2',
                              width=135,corner_radius=5,hover_color='darkred',
                              command=remover_contato
                        )
button_remove.place(x=300, y=220)


# Lista de tarefas
ctk.CTkLabel(app, text='Contatos',
             text_color='white',
             font=fontH2).place(x=200, y=280)



lista_contatos = Listbox(app, font=fontP,
                        width=50, height=20,
                        bg='#3e3e3e', fg='white')
lista_contatos.place(x=20, y=350)






carregar_contatos()
app.mainloop()