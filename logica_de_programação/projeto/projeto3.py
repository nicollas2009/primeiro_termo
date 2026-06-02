# 1. Utilizar tomada de decisão para elaboração do algoritmo
# 2. Utilizar estruturas condicionais para executar instruções com base em uma
# condição
# 3. Criar estruturas de repetição para executar um conjunto de instruções várias
# vezes
# 4. Aplicar operadores lógicos para avaliar e combinar condições booleanas
# 5. Utilizar lógica de programação para a resolução de problemas

# Projeto de Revisão: Sistema de Empréstimo "Biblioteca Digital"
# Contexto: Você foi contratado para desenvolver o módulo de validação de
# empréstimos de livros de uma biblioteca comunitária. O sistema precisa coletar os dados
# do usuário, do livro e decidir se o empréstimo será aprovado, negado ou se haverá
# cobrança de taxa de segurança.
# Regras de Negócio (O que o sistema deve fazer):
# 1. Classificação do Usuário: A biblioteca atende [1] Alunos e [2] Comunidade
# Geral.
# 2. Limite de Dias: * Alunos podem ficar com o livro por até 14 dias de graça.
# ○ A Comunidade Geral pode ficar por até 7 dias de graça.
# 3. Taxa de Renovação: Se o usuário quiser ficar mais tempo do que o limite do seu
# perfil, será cobrada uma taxa fixa de R$ 5,00 por dia adicional.
# 4. Restrição de Categoria: Livros da categoria "Raros" não podem ser emprestados
# para a Comunidade Geral, apenas para Alunos.

import tkinter as tk
from tkinter import messagebox

def validar_emprestimo():

    nome = nome_usuario.get()
    tipo = tipo_usuario.get()
    categoria = categoria_livro.get()

    if nome == "" or tipo == "" or categoria == "":
        messagebox.showwarning("Aviso", "Preencha todos os campos!")
        return

    try:
        dias = int(dias_emprestimo.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite apenas números para os dias.")
        return

    
    if categoria.lower() == "raros" and tipo.lower() == "comunidade":
        messagebox.showerror(
            "Empréstimo Negado",
            "Livros raros só podem ser emprestados para alunos."
        )
        return

   
    if tipo.lower() == "aluno":
        limite = 14
    elif tipo.lower() == "comunidade":
        limite = 7
    else:
        messagebox.showerror(
            "Erro",
            "Digite Aluno ou Comunidade no campo Tipo de Usuário."
        )
        return

    
    if dias > limite:
        dias_extras = dias - limite
        taxa = dias_extras * 5

        messagebox.showinfo(
            "Empréstimo Aprovado",
            f"Usuário: {nome}\n"
            f"Livro: {categoria}\n"
            f"Dias solicitados: {dias}\n"
            f"Taxa de renovação: R$ {taxa:.2f}"
        )
    else:
        messagebox.showinfo(
            "Empréstimo Aprovado",
            f"Usuário: {nome}\n"
            f"Livro: {categoria}\n"
            f"Dias solicitados: {dias}\n"
            f"Sem cobrança de taxa."
        )






janela = tk.Tk()
janela.title("Biblioteca Digital")
janela.geometry("450x300")
janela.configure(bg="lightblue")


lbl_nome = tk.Label(janela, text="Nome:")
lbl_nome.grid(row=0, column=0, padx=10, pady=10)

nome_usuario = tk.Entry(janela)
nome_usuario.grid(row=0, column=1)


lbl_tipo = tk.Label(janela, text="Tipo (Aluno/Comunidade):")
lbl_tipo.grid(row=1, column=0, padx=10, pady=10)

tipo_usuario = tk.Entry(janela)
tipo_usuario.grid(row=1, column=1)


lbl_categoria = tk.Label(janela, text="Categoria (Comum/Raros):")
lbl_categoria.grid(row=2, column=0, padx=10, pady=10)

categoria_livro = tk.Entry(janela)
categoria_livro.grid(row=2, column=1)


lbl_dias = tk.Label(janela, text="Dias de empréstimo:")
lbl_dias.grid(row=3, column=0, padx=10, pady=10)

dias_emprestimo = tk.Entry(janela)
dias_emprestimo.grid(row=3, column=1)


btn_validar = tk.Button(
    janela,
    text="Validar Empréstimo",
    command=validar_emprestimo
)
btn_validar.grid(row=4, column=0, pady=20)


janela.mainloop()