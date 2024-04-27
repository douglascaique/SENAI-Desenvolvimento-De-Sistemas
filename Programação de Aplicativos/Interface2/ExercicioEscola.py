import customtkinter
from tkinter import *




app = customtkinter.CTk('#101010') #cria e da cor para janela
app.geometry("1000x800")
app.title('Sistema Escolar V 1.0')



# FunçãoResultado

def calculaMedia():
    media = (float(input1Unidade.get()) + float(input2Unidade.get()) + float(input3Unidade.get()))/3
    return media


def resultadoMedia():
    media = calculaMedia()
    if (media >= 7):
        saidaResult.insert(0, f'A média do aluno {inputNome.get()} é de {media:.2}. Você foi APROVADO')
    else:
        saidaResult.insert("Recuperação", f'A média do aluno {inputNome.get()} é de {media:.2}')
    
        





#labels/input
customtkinter.CTkLabel(app,
                       text="Sistema Escolar V 1.0",
                       font=('Istok Web', 58, "bold"),
                       text_color='#FFFFFF').pack()


#InputName


inputNome = customtkinter.CTkEntry(app,
                                   placeholder_text='Digite o seu nome',
                                   width=400)
inputNome.pack(pady=10)


#Nota1Unidade

input1Unidade = customtkinter.CTkEntry(app,
                                       placeholder_text='Digite sua nota da 1ª Unidade',
                                       width=400)
input1Unidade.pack(pady=10)

#Nota2Unidade


input2Unidade = customtkinter.CTkEntry(app,
                                       placeholder_text='Digite sua nota da 2ª Unidade',
                                       width=400)
input2Unidade.pack(pady=10)


#Nota3Unidade

input3Unidade = customtkinter.CTkEntry(app, placeholder_text='Digite sua nota da 3ª Unidade', width=400)
input3Unidade.pack(pady=10)



# ButtonResult
buttonResult = customtkinter.CTkButton(app, text="Resultado",
                                       font=('Istok Web', 20, "bold"),
                                       width=200, height=30,
                                       text_color='White',
                                       bg_color='#2FB201',
                                       fg_color='#2FB201',
                                       command=resultadoMedia)
buttonResult.pack(pady=10)

# ButtonLimpar
buttonLimpar = customtkinter.CTkButton(app, text="Limpar",
                                       font=('Istok Web', 20, "bold"),
                                       width=200, height=30,
                                       text_color='White',
                                       fg_color='red',
                                       bg_color='red',
                                       command=resultadoMedia)
buttonLimpar.pack(pady=10)


saidaResult = customtkinter.CTkEntry(app, width=400, height=50, )
saidaResult.pack(pady=30)


# Roda app
app.mainloop()