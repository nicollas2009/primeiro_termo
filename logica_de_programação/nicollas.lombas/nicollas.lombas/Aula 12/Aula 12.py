 #Interface Gráfica com  TKINTER
# Componentes Principais (Widgets)

# tk: Janela principal
# Label: Texto ou rotulo
# Button: Um botão clicável 
# Entry: Um campo de entrada de texto
#bold: negrito
import tkinter as tk
from tkinter import messagebox

# 1. Criar a janela principal
janela = tk.Tk()
janela.title("Minha Primeira Janela GUI")
janela.geometry("800x400") #Largura x Altura

#2. criar a função que o botão ira execultar
def mostrar_mensagem():
    messagebox.showinfo('sucesso!', 'Você clicou no botão')

#3. Criar os componentes
lbl_titulo_pagina = tk. Label(janela, text='Bem vindo a aula de interface grafica!', font=('Arial',14, 'bold'))
lbl_titulo_pagina = tk. Label(janela, text='Aula 12', font=('Arial',14, 'bold'))
btn_clique_pagina = tk.Button(janela, text="Clique Aqui", font=("Arial", 14), bg="#2e46cc", fg="white", command=mostrar_mensagem)
btn_fechar_janela = tk.Button(janela, text="Fechar", font=("Arial", 14), bg="#e74c3c", fg="white", command=janela.destroy)




#4. Posicionar os componentes na janela
lbl_titulo_pagina.pack(pady=20)  #pady adiciona um espaçamento verticial
btn_clique_pagina.pack(pady=10)
btn_fechar_janela.pack(pady=10)

# 5. Rodar o loop da interface
janela.mainloop()
