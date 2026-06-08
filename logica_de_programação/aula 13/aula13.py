import tkinter as tk
from tkinter import messagebox

# .get() serve para buscar informação na caixa de texto
def janela_bemvindo():
    nome = nome_usuario.get()
    
    if nome == "":
        messagebox.showwarning("Aviso", "Digite seu nome :)")
    else:
        messagebox.showinfo("Bem-Vindo", f"Olá usuário, {nome} - Seja bem-vindo ao nosso sistema")
    
    idade = idade_usuario.get()
    
    if idade =="":
        messagebox.showwarning("Aviso", "Digite sua idade :)")

       
    


# Configurações da Janela
janela = tk.Tk()
janela.title("Exemplo 2")
janela.geometry("300x300")
janela.configure(bg="pink")

# Componentes
lbl_mensagem = tk.Label(janela, text="Digite seu nome :)")
lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)

nome_usuario = tk.Entry(janela, font=("Arial", 12))
nome_usuario.grid(row=0, column=1, pady=10, padx=10)

btn_mensagem = tk.Button(janela, text="Mensagem", command=janela_bemvindo)
btn_mensagem.grid(row=1, column=0, pady=10, padx=10)

lbl_mensagem = tk.Label(janela, text=" :)")
lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)


# Rodar interface
janela.mainloop()



