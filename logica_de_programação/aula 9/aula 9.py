 #Exercícios de Programação Python: "O Caça-Erros"

# ----------------------------------------------------

# 1. O Problema da Idade

# Erro
# idade = input("Digite sua idade:")
# if idade >= 18:
#     print("Você é maior de idade")

# Corrigido
# idade = int(input("Digite sua idade"))
# if idade >= 18:
#     print("Você é maior de idade")

# Melhorado
# idade = int(input("Digite sua idade:"))
# if idade >= 18:
#     print("Você é maior de idade")
# else:
#     print("Você é menor de idade")

# ----------------------------------------------------

# 2. A Escrita Fiel

# Erro
# nome = "Mariana"
# print("Seja bem-vinda, nome!")

# Corrigido
# nome = "Mariana"
# print(f"Seja bem-vinda, {nome}!")

# Melhorado
# nome = input("Digite Seu Nome:  ")
# print(f"Seja bem-vinda, {nome}!")

# ----------------------------------------------------

# 3. Falta de Espaço

# Erro
# numero = 10
# if numero > 5:
# print("O número é maior que cinco.")
# else:
# print("O número é menor ou igual a cinco.")

# Corrigido
# numero = 10
# if numero > 5:
#     print("O número é maior que cinco.")
# else:
#     print("O número é menor ou igual a cinco.")

# Melhorado
# numero = float(input("Digite um número: "))
    
# if numero > 5:
#         print("O número é maior que cinco.")
# elif numero == 5:
#         print("O número é exatamente cinco.")
# else:
#         print("O número é menor que cinco.")


# ----------------------------------------------------

# 4. Esquecimento Fatal

# Erro
# usuario = "aluno123"
# if usuario == "aluno123"
# print("Login realizado com sucesso.")

# Corrigido
# usuario = "aluno123"
# if usuario:
#     print("Login realizado com sucesso.")

# Melhorado
# usuario = input("Digite o nome de usuario:  ")
# if usuario == "aluno123":
#     print("Login realizado com sucesso.")
# else:
#     print("Usuário inválido.")

# ----------------------------------------------------

# 5. Atribuição vs. Comparação

# Erro
# clima = "ensolarado"
# if clima = "chuvoso":
# print("Leve um guarda-chuva!")

# Corrigido
# clima = "ensolarado"
# if clima == "chuvoso":
#     print("Leve um guarda-chuva!")
# else:
#     print("O clima está bom, não precisa de guarda-chuva.")


# Melhorado
# clima = input("Como está o clima? (ensolarado/chuvoso): ")
# if clima == "chuvoso":
#     print("Leve um guarda-chuva!")
# elif clima == "ensolarado":
#     print("Aproveite o sol!")
# else:
#     print("Clima incerto, melhor prevenir.")

# ----------------------------------------------------

# 6. Misturando Alhos com Bugalhos

# Erro
# pontos = 50
# print("Parabéns! Você fez " + pontos + " pontos.")

# Corrigido
# pontos = 50
# print("Parabéns! Você fez", pontos, "pontos.")

# Melhorado
# pontos = 50
# print(f"Parabéns! Você fez {pontos} pontos.")


# ----------------------------------------------------

# 7. A Ordem dos Fatores
# O sistema deve dar "Excelente" para notas 9 ou 10.

# Erro
# nota = 9.5
# if nota >= 7:
# print("Aprovado")
# elif nota >= 9:
# print("Excelente!")

# Corrigido
# nota = float(input("Digite sua nota: "))
# if nota >= 9:
#     print("Excelente!")
# elif nota >= 7:
#     print("Aprovado")
# else:
#     print("Reprovado")

# Melhorado
# nota = float(input("Digite sua nota (0-10): "))

# if 9 <= nota <= 10:
#     print(f"Nota {nota}: Excelente!")
# elif 7 <= nota < 9:
#     print(f"Nota {nota}: Aprovado")
# elif 0 <= nota < 7:
#     print(f"Nota {nota}: Reprovado")
# else:
#     print("Nota inválida! Digite um valor entre 0 e 10.")

# ----------------------------------------------------

# 8. O Contador de 1 a 5
# Objetivo: Mostrar na tela os números 1, 2, 3, 4 e 5.

# Erro
# for i in range(5):
# print(i)

# Corrigido
# for i in range(5):
#     print(i)

# Melhorado

# numero = int(input("Digite o número:  "))
# for i in range(numero):
#     print(i)

# ----------------------------------------------------

# 9. O Loop Eterno

# Erro
# tentativas = 1
# while tentativas <= 3:
# print("Tentando conectar...")

# Corrigido
# tentativas = 1
# while tentativas <= 3:
#     print("Tentando conectar...")
#     tentativas = tentativas + 1
# print("Fim das tentativas.")

# Melhorado
# for i in range(1, 4):
#     print(f"Tentativa {i}: Conectando...")

# print("Fim das tentativas.")

# ----------------------------------------------------

# 10. A Senha Teimosa
# O programa deve pedir a senha até que o usuário digite "python123"

# Erro
# senha = ""
# while senha == "python123":
# senha = input("Digite a senha secreta: ")
# print("Acesso concedido!")

# Corrigido
# while True:
#     senha = input("Digite a senha secreta: ")
#     if senha == "python123":
#         break
#     print("Senha incorreta. Tente novamente.")

# print("Acesso concedido!")


# Melhorado
# tentativas = 3
# while tentativas > 0:
#     senha = input(f"Digite a Senha ({tentativas} tentativas restantes): ")
#     if senha == "python123":
#         print("Acesso concedido!")
#         break
#     tentativas -= 1
# else:
#     print("Acesso bloqueado. Muitas tentativas falhas.")
