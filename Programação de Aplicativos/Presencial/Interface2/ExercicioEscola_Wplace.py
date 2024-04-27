import customtkinter
import tkinter
from tkinter import messagebox


customtkinter.set_appearance_mode("dark")           # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")       # Themes: blue (default), dark-blue, green

app = customtkinter.CTk('#D9D9D9') #cria e da cor para janela
app.geometry("800x500")
app.title('Sistema Escolar V 1.0')



# FunçãoResultado

def calculaMedia():
    media = (float(input1Unidade.get()) + float(input2Unidade.get()) + float(input3Unidade.get()))/3
    return media


def resultadoMedia():
    media = calculaMedia()
    if (media >= 5):
        messagebox.showinfo("Média", f'A média do aluno {inputNome.get()} é de {media:.2}')
    
        





#labels/input
customtkinter.CTkLabel(app, text="Sistema Escolar V 1.0", font=('Istok Web', 58, "bold"),
text_color='#000000').place(x=100,y=1)


#InputName
customtkinter.CTkLabel(app, text="Nome:", font=('Istok Web', 25, "bold"),
text_color='#000000').place(x=200,y=100)

inputNome = customtkinter.CTkEntry(app, placeholder_text='Digite o seu nome', width=400)
inputNome.place(x=200, y=130)


#Nota1Unidade
customtkinter.CTkLabel(app, text="1ª Unidade", font=('Istok Web', 25, "bold"),
text_color='#000000').place(x=200, y=170)

input1Unidade = customtkinter.CTkEntry(app, placeholder_text='Digite sua nota da 1ª Unidade', width=400)
input1Unidade.place(x=200, y=200)

#Nota2Unidade
customtkinter.CTkLabel(app, text="2ª Unidade", font=('Istok Web', 25, "bold"),
text_color='#000000').place(x=200, y=240)

input2Unidade = customtkinter.CTkEntry(app, placeholder_text='Digite sua nota da 2ª Unidade', width=400)
input2Unidade.place(x=200, y=270)


#Nota3Unidade
customtkinter.CTkLabel(app, text="3ª Unidade", font=('Istok Web', 25, "bold"),
text_color='#000000').place(x=200, y=310)

input3Unidade = customtkinter.CTkEntry(app, placeholder_text='Digite sua nota da 3ª Unidade', width=400)
input3Unidade.place(x=200, y=340)



# ButtonResult
buttonResult = customtkinter.CTkButton(app, text="Resultado", font=('Istok Web', 20, "bold"), width=250, height=50, text_color='white', border_color='black', border_width=3, command=resultadoMedia)
buttonResult.place(x=300, y=400)


app.mainloop()