import customtkinter as ctk
from tkinter import *
from tkinter import messagebox



#funções

receita = 0
despesa = 0
resultado = 0

# def receita():
#     receita = entrada_receita.get() + entrada_receitaBonus.get()
#     return receita
        
# def despesa():
#     despesa = entrada_despesa.get() + entrada_despesa.get() + entrada_despesa1.get() + entrada_despesa2.get() + entrada_despesa3.get()
#     return despesa

def calcula_financeiro():
        receita = float(entrada_receita.get()) + float(entrada_receitaBonus.get())
        despesa = float(entrada_despesa.get()) + float(entrada_despesa1.get()) + float(entrada_despesa2.get()) + float(entrada_despesa3.get())
        
        resultado = (receita - despesa)
        
        messagebox.showinfo('Saldo final: R$', f'{resultado:.2f}')
        
        

            
# ----- default style
ctk.set_appearance_mode('dark')
app = ctk.CTk()
app.geometry('1200x600')
app.title('Fiancier v1.0')

#----root style
fontH1 = ('Arial', 24, 'bold')
fontH2 = ('Arial', 18, 'bold')
fontH3 = ('Arial', 14, 'bold')
fontP = ('Arial', 12, 'bold')

# Title
ctk.CTkLabel(app,text='Financier',
             text_color='white',font=fontH1).pack(pady=5)

ctk.CTkLabel(app,text='Nos campos abaixo, \n adicione suas informações financeiras',
             text_color='white',font=fontH2).pack(pady=5)



# ENTRADAS
# entrada de Receita Fixa

ctk.CTkLabel(app, text='Quanto ganho por mês:',
             text_color='white',
             font=fontH3).place(x=30, y=95)
entrada_receita = ctk.CTkEntry(app, font=fontP,
                             width=150, height=25)
entrada_receita.place(x=40, y=120)

entrada_receitaBonus = ctk.CTkEntry(app, font=fontP,
                             width=150, height=25)
entrada_receitaBonus.place(x=40, y=150)


# Botão para adicionar
button_adicionar = ctk.CTkButton(app, text='Adicionar Receitas',
                              font=fontH3, text_color='white',
                               fg_color='green', cursor='hand2',
                              width=135,corner_radius=5, hover_color='darkgreen'
                              )
button_adicionar.place(x=250, y=150)





# DESPESAS


# entrada de Receita Fixa

ctk.CTkLabel(app, text='Gastos fixos por mês:',
             text_color='white',
             font=fontH3).place(x=800, y=95)


entrada_despesa = ctk.CTkEntry(app, font=fontP,
                             width=150, height=25)
entrada_despesa.place(x=800, y=120)

entrada_despesa1 = ctk.CTkEntry(app, font=fontP,
                             width=150, height=25)
entrada_despesa1.place(x=800, y=150)

entrada_despesa2 = ctk.CTkEntry(app, font=fontP,
                             width=150, height=25)
entrada_despesa2.place(x=800, y=180)

entrada_despesa3 = ctk.CTkEntry(app, font=fontP,
                             width=150, height=25)
entrada_despesa3.place(x=800, y=210)


# Botão para adicionar
button_adicionar = ctk.CTkButton(app, text= 'Adicionar Gastos ',
                              font=fontH3, text_color='white',
                               fg_color='green', cursor='hand2',
                              width=140,corner_radius=5, hover_color='darkgreen'
                              )
button_adicionar.place(x=1000, y=150)










button_adicionar = ctk.CTkButton(app, text= 'Calcular ',
                              font=fontH3, text_color='white',
                               fg_color='green', cursor='hand2',
                              width=200,height=40,corner_radius=5, hover_color='darkgreen',
                              command=calcula_financeiro
                              )
button_adicionar.place(x=500, y=400)




app.mainloop()