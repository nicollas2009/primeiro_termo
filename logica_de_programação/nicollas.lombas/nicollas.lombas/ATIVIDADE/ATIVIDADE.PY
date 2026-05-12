# Atividade 1: Mensagem de Boas-Vindas
# Crie um script que use a função print() para exibir a mensagem "Bem-vindo ao mundo da
# programação em Python!".

# print('Bem-vindo a o mundo da programação em python!')


# Atividade 2: Informações Pessoais
# Escreva um programa que imprima seu nome completo em uma linha e sua idade em outra linha.
# Exemplo de saída:
# Fulano de Tal
# 30

# pergunta1 = input('Digite seu nome')
# pergunta2 = int(input('Digite a sua idade'))

# print(('Seu nome e sua idade são:' ,pergunta1, pergunta2))


# Atividade 3: Calculadora de Soma e Subtração
# Crie um script que exiba o resultado da soma de 135 com 246 e o resultado da subtração de 512
# por 128. Cada resultado deve ser exibido em uma linha separada.
# ● Dica: Use o print() diretamente com os operadores (print(135 + 246)).
# ● Obs: Realize também a mesma situação com variáveis

# (print(135 + 246))
# (print(512 - 128))


# Atividade 4: Multiplicação e Divisão
# Escreva um programa que mostre o resultado da multiplicação de 15 por 8 e o resultado da
# divisão de 78 por 3.

# (print(15 * 8))
# (print(78 / 3))


# Atividade 5: Potenciação
# Calcule e exiba o resultado de "5 elevado à 3a potência" (53).
# ● Dica: O operador de potenciação em Python é **.

# print("5 Elevado a 3 é:  ")
# print(5**3)


# Atividade 6: Concatenando Palavras
# Crie um script que declare o seu primeiro nome em uma string e seu sobrenome em outra. Use
# o operador + para concatenar (juntar) as duas strings e exibir seu nome completo.
# ● Exemplo: print("Maria" + " " + "Silva")

# input("Nome" + " " + "Sobre nome")


# Atividade 7: Cálculo de Eficiência (OEE)
# ● Peça a quantidade de peças produzidas e a quantidade de peças defeituosas. Calcule
# e exiba a taxa de aproveitamento (peças boas / total).

# total = int(input('peças produsidas'))
# defeituosa = int(input('peças defeituosa'))

# print('a taxa de aproveitamento foi ', defeituosa / total)



# Atividade 8: Descrição com Cálculos
# Crie um script que exiba a seguinte frase, substituindo os cálculos pelos seus resultados:
# "Eu tenho 25 anos e, em 10 anos, terei 35 anos."
# ● Dica: Use a vírgula dentro do print() para combinar strings e cálculos.
# ● Ex: print("Texto", 25 + 10).

# idade = int(input('diga sua idade'))

# print("você tera", idade + 10)


# Atividade 9: Orçamento de Viagem (Cálculo com float)
# Imagine que você está planejando uma viagem. O custo do hotel é de R$ 250.50 por noite e
# o custo da passagem é R$ 412.00. Calcule e exiba o custo total para uma viagem por noites.
# ● Ex: Fórmula: (custo_hotel * 3) + custo_passagem

#  dias = int(input('digite os dias:  '))

# valor_hotel = 250
# valor_passagem = 412

# total_hospedagem = valor_hotel * dias
# total_total = total_hospedagem + valor_passagem

# print(f"Custo total da hospedagem ({dias} Dias): R$", total_hospedagem)
# print("Custo total da passagem: R$", valor_passagem)
# print("Custo total da viagem: R$", total_total)


# Atividade 10: Desafio - Mini Relatório
# Crie um script que imprima um pequeno relatório. Use print() várias vezes para formatar a
# saída de forma organizada.
# ● Exemplo de saída:

# ==========================
# Relatório de Vendas
# ==========================
# Produto: Notebook Gamer
# Quantidade vendida: 15
# Preço unitário: R$ 5499.50
# Total de vendas: R$ 82492.50
# ==========================

# Dados do relatório
# produto = "Notebook Gamer"
# quantidade = 15
# preco_unitario = 5499.50
# total_vendas = quantidade * preco_unitario

# # Impressão do relatório
# print("Relatório de Vendas")
# print(f"Produto: {produto}")
# print(f"Quantidade vendida: {quantidade}")
# print(f"Preço unitário: R$ {preco_unitario:.2f}")
# print(f"Total de vendas: R$ {total_vendas:.2f}")

