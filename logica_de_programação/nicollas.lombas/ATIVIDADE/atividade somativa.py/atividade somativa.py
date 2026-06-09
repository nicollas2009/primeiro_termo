# Foco: print, input, operações matemáticas e f-strings
# 1. Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:
# "Operador [Nome] registrado no Turno [Turno]. Boa jornada!"
# import tkinter as tk
# from tkinter import messagebox


# def janela_bemvindo():
#     nome = nome_usuario.get().strip()
#     turno = turno_usuario.get().strip().upper()  
    
#     if nome == "":
#         messagebox.showwarning("Aviso", "Por favor, digite seu nome :)")
#         return
        
#     if turno == "" or turno not in ["A", "B", "C"]:
#         messagebox.showwarning("Aviso", "Por favor, digite um turno válido (A, B ou C) :)")
#         return
        
    
#     mensagem_final = f"Operador {nome} registrado no Turno {turno}. Boa jornada!"
#     messagebox.showinfo("Registro Concluído", mensagem_final)


# janela = tk.Tk()
# janela.title("Registro de Operador")
# janela.geometry("350x200")
# janela.configure(bg="black")

# lbl_nome = tk.Label(janela, text="Nome do Operador:", bg="blue", font=("Arial", 10, "bold"))
# lbl_nome.grid(row=0, column=0, pady=10, padx=10, sticky="w")

# nome_usuario = tk.Entry(janela, font=("Arial", 12))
# nome_usuario.grid(row=0, column=1, pady=10, padx=10)


# lbl_turno = tk.Label(janela, text="Turno (A, B ou C):", bg="blue", font=("Arial", 10, "bold"))
# lbl_turno.grid(row=1, column=0, pady=10, padx=10, sticky="w")

# turno_usuario = tk.Entry(janela, font=("Arial", 12))
# turno_usuario.grid(row=1, column=1, pady=10, padx=10)


# btn_mensagem = tk.Button(janela, text="Registrar", command=janela_bemvindo, font=("Arial", 10, "bold"))
# btn_mensagem.grid(row=2, column=0, columnspan=2, pady=15)

# janela.mainloop()


#. 2 Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e
#exiba quantas peças serão produzidas em um turno de 8 horas.

# import tkinter as tk
# from tkinter import messagebox

# def calcular_producao():
    
#     pecas_por_hora_n = pecas_hora.get()

    
#     if pecas_por_hora_n == "":
#         messagebox.showwarning("Aviso", "Preencha a quantidade de peças!")
#         return

    
#     try:
#         pecas_por_hora = int(pecas_por_hora_n)
#     except ValueError:
#         messagebox.showerror("Erro", "Digite apenas números inteiros para as peças.")
#         return

    
#     turno_horas = 8
#     total_produzido = pecas_por_hora * turno_horas

    
#     messagebox.showinfo(
#         "Resultado da Produção",
#         f"Produção por hora: {pecas_por_hora} peças\n"
#         f"Duração do turno: {turno_horas} horas\n"
#         f"Total produzido no turno: {total_produzido} peças"
#     )


# janela = tk.Tk()
# janela.title("Cálculo de Produção")
# janela.geometry("450x200")
# janela.configure(bg="lightblue")


# lbl_pecas = tk.Label(janela, text="Peças produzidas em 1 hora:")
# lbl_pecas.grid(row=0, column=0, padx=10, pady=20)


# pecas_hora = tk.Entry(janela)
# pecas_hora.grid(row=0, column=1, padx=10, pady=20)

# btn_calcular = tk.Button(
#     janela,
#     text="Calcular Turno (8h)",
#     command=calcular_producao
# )
# btn_calcular.grid(row=1, column=0, columnspan=2, pady=20)


# janela.mainloop()

# 3.Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar
# ≈ 14.5 PSI) e exiba com duas casas decimais.

# import tkinter as tk
# from tkinter import messagebox

# def converter_para_psi():
    
#     valor_digitado = entry_bar.get()

    
#     if valor_digitado == "":
#         messagebox.showwarning("Aviso", "Digite a quantidade de Bar")
#         return

#     try:
       
#         bar = float(valor_digitado)
#         fator_psi = 14.5
#         psi = bar * fator_psi 
        
       
#         messagebox.showinfo("Resultado", f"{bar} Bar equivale a {psi:.2f} PSI")
        
#     except ValueError:
       
#         messagebox.showerror("Erro", "Por favor, insira apenas números válidos (use ponto para decimais).")


# janela = tk.Tk()
# janela.title("Conversor de Bar para PSI")
# janela.geometry("400x150")
# janela.configure(bg="lightblue")


# lbl_bar = tk.Label(janela, text="Quantidade de Bar:", bg="lightblue", font=("Arial", 10))
# lbl_bar.grid(row=0, column=0, padx=10, pady=20)


# entry_bar = tk.Entry(janela, font=("Arial", 10))
# entry_bar.grid(row=0, column=1, padx=10, pady=20)


# btn_calcular = tk.Button(
#     janela,
#     text="Calcular PSI",
#     command=converter_para_psi,
#     font=("Arial", 10, "bold")
# )
# btn_calcular.grid(row=1, column=0, columnspan=2, pady=10)

# janela.mainloop()



# 4. Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média
# aritmética simples delas.
  

# import tkinter as tk
# from tkinter import messagebox

# def calcular_media():
   
#     n1 = float(entry_nota1.get())
#     n2 = float(entry_nota2.get())
#     n3 = float(entry_nota3.get())
    
   
#     media = (n1 + n2 + n3) / 3
    
   
#     messagebox.showinfo(
#         "Média de Qualidade",
#         f"A média das notas é: {media}"
#     )

# janela = tk.Tk()
# janela.title("Média de Qualidade")
# janela.geometry("350x200")


# lbl_1 = tk.Label(janela, text="Nota 1:")
# lbl_1.grid(row=0, column=0, padx=10, pady=10)
# entry_nota1 = tk.Entry(janela)
# entry_nota1.grid(row=0, column=1, padx=10, pady=10)


# lbl_2 = tk.Label(janela, text="Nota 2:")
# lbl_2.grid(row=1, column=0, padx=10, pady=10)
# entry_nota2 = tk.Entry(janela)
# entry_nota2.grid(row=1, column=1, padx=10, pady=10)


# lbl_3 = tk.Label(janela, text="Nota 3:")
# lbl_3.grid(row=2, column=0, padx=10, pady=10)
# entry_nota3 = tk.Entry(janela)
# entry_nota3.grid(row=2, column=1, padx=10, pady=10)


# btn_calcular = tk.Button(janela, text="Calcular Média", command=calcular_media)
# btn_calcular.grid(row=3, column=0, columnspan=2, pady=10)

# janela.mainloop()


# 5. Termostato Inteligente: Peça a temperatura de um motor.
# ● Abaixo de 40°C: "Baixa carga".
# ● Entre 40°C e 70°C: "Normal".
# ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".