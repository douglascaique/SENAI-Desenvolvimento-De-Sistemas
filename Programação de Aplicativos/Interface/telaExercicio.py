import customtkinter


customtkinter.set_appearance_mode("dark")           # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")       # Themes: blue (default), dark-blue, green

app = customtkinter.CTk('#D9D9D9') #cria e da cor para janela
app.geometry("500x338")
app.title('PomoDoug V1.0')


# funções
def button_function():
    print("button pressed")
    
        
    
# #checkbox
# checkbox_1 = customtkinter.CTkCheckBox(app, text='teste')

#labels/input
customtkinter.CTkLabel(app, text="Tela de Acesso", font=('Istok Web', 22, "bold"),
text_color='#000000').pack(pady=10)

#login
customtkinter.CTkLabel(app, text="Login", font=('Istok Web', 18, "bold"),
text_color='#000000').pack(pady=10)

inputLogin = customtkinter.CTkEntry(app, placeholder_text='Digite o seu login', width=300)
inputLogin.pack()

#senha
customtkinter.CTkLabel(app, text="Senha", font=('Istok Web', 18, "bold"),
text_color='#000000').pack(pady=10)

inputSenha = customtkinter.CTkEntry(app, placeholder_text='Digite a sua senha', width=300, show="❤️")
inputSenha.pack()


# Button
buttonAcesso = customtkinter.CTkButton(app, text="Acessar", width=150, text_color='white', border_color='black', border_width=3, command=button_function)
buttonAcesso.pack(pady=15)




# # label/entry
# customtkinter.CTkLabel(text="Login")
# customtkinter.CTkLabel.grid(row=0, column=0, padx=20, pady=20,sticky="ew")

# inputName = customtkinter.CTkEntry(placeholder_text='douglascaique')
# inputName.grid(row=0, column=1, columnspan=3,padx=20,pady=20, sticky='ew')




app.mainloop()