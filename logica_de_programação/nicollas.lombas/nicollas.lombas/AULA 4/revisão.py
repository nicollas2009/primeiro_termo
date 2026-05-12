# # Perfil de Gamer: Peça o nick (nome) do jogador e o nível atual. Exiba: "O
# jogador [nick] está no nível [nível] e pronto para a partida!"

pergunta1 = input('Digite seu nike')
pergunta2 = int(input('Digite o seu nível atual'))

print (f'Ojogador {pergunta1} esta no nivel {pergunta2}')


# 2. Calculadora de Mesada: Peça o valor que o aluno ganha por semana e
# multiplique por 4 para mostrar quanto ele terá no final do mês.

pergunta = int(input("Digite o quanto você ganha por semana"))

calculo = int(pergunta*4)

print (f'você ganha no mês {calculo}')


# 3. Conversor de Internet: Peça um valor em Gigabytes (GB) e converta para
# Megabytes (MB) (multiplique por 1024).

pergunta = float("quantos Gigabytes você tem ")

calculo = pergunta*1024

print (f'você tem no  {calculo} de Megabytes')


# 4. Média de Notas: Peça as notas de Matemática e Português. Calcule e mostre a
# média final.

pergunta1 = float(input('qual foi sua nota da prova de matematica'))
pergunta2 = float(input('qual foi sua nota da prova de poetuguês'))

calculo = pergunta1+pergunta2
soma = calculo/2
print (f'sua media final foi de {soma}')



# 5. Seguidores: Peça a quantidade de seguidores atuais e quantos novos seguidores
# o aluno ganhou hoje. Exiba o total atualizado.

pergunta1 = int(input('qual foi a quantidade de seguidores atuais'))
pergunta2 = int(input('qual foi a quantidade de seguidores novos'))

soma = int(pergunta1 + pergunta2)
print (f'o total de seguidores que voce tem são {soma}')



# 6 Idade em Dias: Peça a idade do aluno e calcule aproximadamente quantos dias
# ele já viveu (idade * 365).

idade = int(input('qual é sua idade'))
calculo = int(idade*365)

print (f'o total de dias vivo são {calculo}')


# 7. Consumo de Lanche: Peça o preço do salgado e o preço do suco. Exiba o valor
# total da conta.

suco = int(input('qual o valor do suco'))
salgado = int(input('qual o valor do salgado'))

calculo = int(suco+salgado)

print (f'o valor do salgado mais o suco é {calculo}')



# 8. Ano de Nascimento: Peça o ano atual e a idade do aluno. Calcule e exiba o ano
# em que ele nasceu.

ano = int(input('qual é o ano'))
idade = int(input('qual a sua idade'))

calculo = int(ano-idade)

print (f'o ano que você naçeu foi {calculo}')



# 9.Filtro de Idade (TikTok): Peça a idade do usuário. Se for menor que 13, exiba
# "Acesso restrito". Se tiver entre 13 e 17, "Acesso moderado". Se for 18 ou
# mais, "Acesso liberado".

idade = int(input('qual sua idade'))

if idade < 13:
    print('você é criança')
elif idade < 18:
    print('você é um adolecente')
else:
    print('você é um adulto')       


# 10.Bateria do Celular: Crie um while que começa com a bateria em 100. A cada
# repetição, subtraia 10 e mostre: "Bateria em [valor]%". O loop para quando
# chegar em 10 e exibe: "Por favor, conecte o carregador!".

bateria = 100

while bateria > 10:
    bateria -= 10

    print(f'bateria em {bateria}%')

print('porfavor, conecte o carregador')    



# 11. Contagem de Curtidas: Use um for para simular a contagem de curtidas em uma
# foto. Peça ao usuário o limite de curtidas (ex: 5). O programa deve contar de 1 até
# esse número, printando: "Curtida no [i] recebida!".

limite = int(input("digite qual o limite de cortida"))

for i in range(1, limite + 1):
    print(f'curtida n {i} recebida')



# 12.Carrinho de Compras Online: Use um while para pedir nomes de produtos que o
# aluno quer comprar. O loop só para quando ele digitar "sair". No final, mostre
# quantas vezes ele adiciona itens ao carrinho (use um contador).

print('carrinho de compras revision')

contador_itens = 0
while True:
    produto = input('produto(ou digite"sair"para fechar):')

    if produto.lower() == 'sair':
        break

    if produto.strip() == '':
        continue

    contador_itens += 1
    print(f'{produto} adicionado com sucesso')

    print(f'\in checkout finalizado')
    print(f'você adicionou {contador_itens} item(ns) ao seu carrinho. Volte sempre')
    print('-' + 50)

    