import customtkinter as ctk
import os

app = ctk.CTk('#101010')
app.minsize(300,400)
app.maxsize(800,800)
app.title('Automatizador')




# funções

def desligaPC():
    os.system('shutdown /s /t 30')

def reiniciaPC():
    os.system('shutdown /r /t 0')

def logoffPC():
      os.system('shutdown -l')



# tittle
ctk.CTkLabel(app, text='AutomatizaJá', font=('Istok Web', 40, "italic"), text_color="white",bg_color='#106010').pack(pady=10)


# desligar
desligar = ctk.CTkButton(app,text='Desligar', width=150, height=30, command=desligaPC)
desligar.pack(pady=10)


# reiniciar
reiniciar = ctk.CTkButton(app,text='Reiniciar', width=150, height=30, command=reiniciaPC)
reiniciar.pack(pady=10)


# logoff
logoff = ctk.CTkButton(app,text='LogOff', width=150, height=30, command=logoffPC)
logoff.pack(pady=10)



# Roda app

app.mainloop()