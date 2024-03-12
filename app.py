import customtkinter

import mysql.connector

import func

#customtkinter.set_appearance_mode("Dark")
#customtkinter.set_default_color_theme("dark-blue")


janela = customtkinter.CTk()
janela.geometry("500x300")

def clique():
    print("Produto Registrado!")

texto = customtkinter.CTkLabel(janela, text="Registro de Produto")
texto.pack(padx=10, pady=10)

produto = customtkinter.CTkEntry(janela, placeholder_text="Qual é o produto?")
produto.pack(padx=10, pady=10)

preco = customtkinter.CTkEntry(janela, placeholder_text="Qual é o valor?")
preco.pack(padx=10, pady=10)

tipo = customtkinter.CTkEntry(janela, placeholder_text="Qual é o tipo?")
tipo.pack(padx=10, pady=10)

def registrar():
    p = produto.get()
    t = tipo.get()
    v = preco.get()

    conect = func.conexao('vendas')
    func.create(p, t, v, conect)

    print("Registro realizado")

#button = customtkinter.CTkButton(janela, text="Registrar", command= lambda: func.create(p, t, v, conect))
button = customtkinter.CTkButton(janela, text="Registrar", command= lambda: registrar())
button.pack(padx=10, pady=10)


janela.mainloop()