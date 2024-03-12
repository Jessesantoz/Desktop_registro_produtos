import tkinter

janela = tkinter.Tk()
janela.geometry("500x300")

def clique():
    print("Fazer login")

texto = tkinter.Label(janela, text="Fazer Login")
texto.pack(padx=10, pady=10)

button = tkinter.Button(janela, text="Login", command=clique)
button.pack(padx=10, pady=10)

janela.mainloop()