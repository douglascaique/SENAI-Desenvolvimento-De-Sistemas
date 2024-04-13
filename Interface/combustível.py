import customtkinter as ctk
from tkinter import *
from tkinter import messagebox

ctk.set_appearance_mode('default')

#tela
app = ctk.CTk('#FFA51F')
app.geometry('800x400')
app.title('GasoCalc v1.0')



#funções ---------------
    #função calc

def calculaCombustivel():
    distancia = int(inputDistancia.get())
    consumo = int(inputConsumo.get())
    preco = float(inputConsumo.get())
    
    resultado = (distancia/consumo)*preco
    
    messagebox.showinfo('O gasto da viagem será de R$:', f'{resultado:.2f}')




#-----------------------

#title
ctk.CTkLabel(app, text="GasoCalc", font=('Istok Web', 35, 'bold'), text_color='#291400').pack(pady=10)

#distância
ctk.CTkLabel(app, text="Distância (Km)", font=('Istok Web', 16, 'bold'), text_color='black').pack(pady=10)
inputDistancia = ctk.CTkEntry(app, placeholder_text='Digite quantos Km foram rodados', width=300)
# inputDistancia.place()
inputDistancia.pack()


#consumo
ctk.CTkLabel(app, text="Consumo (L)", font=('Istok Web', 16, 'bold'), text_color='black').pack(pady=10)
inputConsumo = ctk.CTkEntry(app, placeholder_text='Quantos Km por Litro', width=300)
inputConsumo.pack()


#preçoCombustivel
ctk.CTkLabel(app, text="Preço R$ do Combustível", font=('Istok Web', 16, 'bold'), text_color='black').pack(pady=10)
inputPriceCombustivel = ctk.CTkEntry(app, placeholder_text='Valor do combustível R$', width=300)
inputPriceCombustivel.pack()

#btnCalcular
buttonCalc = ctk.CTkButton(app, text="Calcular", width=109, height=34, text_color='#000000',font=('Istok Web', 16, 'bold') , fg_color='#FFD2A9', command=calculaCombustivel)
buttonCalc.pack(pady=15)




app.mainloop()