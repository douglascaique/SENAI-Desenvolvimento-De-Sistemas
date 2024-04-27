import customtkinter as ctk
from tkinter import *
from tkinter import messagebox


# ----funções

def adicionar_tarefa():
    tarefa = entrada_tarefas.get()
    if tarefa:
        lista_tarefas.insert(0, tarefa)
        entrada_tarefas.delete(0, END)
    else:
        messagebox.showerror('Erro', 'Digite uma tarefa para adicionar.')

def remover_tarefa():
    try:
        selecao = lista_tarefas.curselection()
        lista_tarefas.delete(selecao)
    except ctk.TclError:
        messagebox.showerror('Erro', 'Digite uma tarefa para remover.')


# ----- default style
ctk.set_appearance_mode('dark')
app = ctk.CTk()
app.geometry('350x450')
app.title('TO-DO List')

#----root style
fontH1 = ('Arial', 24, 'bold')
fontH3 = ('Arial', 14, 'bold')
fontP = ('Arial', 12, 'bold')

# ------------------

# Title
ctk.CTkLabel(app,text='TO-DO LIST',
             text_color='white',font=fontH1).pack(pady=5)




# Botão para adicionar
button_adicionar = ctk.CTkButton(app, text='Adicionar Tarefa',
                              font=fontH3, text_color='white',
                               fg_color='green', cursor='hand2',
                              width=135,corner_radius=5, hover_color='green',
                              command=adicionar_tarefa
                              )
button_adicionar.place(x=40, y=60)


# Botão para remover
button_remove = ctk.CTkButton(app, text='Remover Tarefa',
                              font=fontH3, text_color='white',
                              fg_color='red', cursor='hand2',
                              width=135,corner_radius=5,hover_color='red',
                              command=remover_tarefa)
button_remove.place(x=180, y=60)


# entrada de tarefas
entrada_tarefas = ctk.CTkEntry(app, font=fontP,
                             width=300, height=50)
entrada_tarefas.place(x=25, y=100)






# Lista de tarefas
ctk.CTkLabel(app, text='TO-DO',
             text_color='white',
             font=fontH3).place(x=155, y=160)



lista_tarefas = Listbox(app, font=fontP,
                        width=30, height=10,
                        bg='#3e3e3e', fg='white')
lista_tarefas.place(x=40, y=200)

app.mainloop()