# clean code - Aula 6
# para que User?
# como usar  ?   
# print('clean code -aula 6')
# aula = 6
# print(f'Estamos na aula {aula} de clean code')

#  1 exemplo
# Manipulação de arquivos e texto
# texto = "  Python é Muito legal!  "
# print(texto.strip().upper())    #"PYTHON"
# print(texto.strip().lower())     #python
# print(texto.strip().capitalize())  #"Python"
# print(texto.strip().title())     #Python
# print(texto.strip().replace("", "_"))   #"Python"
# print(texto.strip().split())    #["Python"]

# 2 exemplo
# Escrevendo
# with open("notas.txt", "w") as arquivo:
#     arquivo.write("Estudar Python hoje!")
#     arquivo.write("\nler sobre Clean code.")

# #lendo
# with open("notas.txt", "r") as arquivo:
#     conteudo = arquivo.read()

#     print(conteudo)


# EXERCICIO 1:
# crie um programa que peça ao usuario para inserir uma frase e,
# em seguida, exibir a frase com as seguintes trasformaçoes:
# - remova os espaços extras no inicio e no final da frase

# texto = input("digite a sua frase: ")

# print(texto.strip().replace("", "_"))


# Exercicio 2:
# crie um programa que leia o conteúdo de um arquivo de texto e conte quantas 
# vezes a palavra "Python" aparece no arquivo. Exiba o resultado para o usuario>

# print("Contagem de palavra em arquivos")
# with open("notas.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     contagem = conteudo.count("Python")
#     print(f"A contagem de palavras {contagem} é de...")


# Exercicio 3 (de comandos do sistema)

# import os #importa o módulo os para interagir com o sistema operacional
# #onde estou?
# print(os.getcwd())
# #listar arquivos na pasta
# print(os.listdir())
# print(os.listdir(".."))  #lista arquivos da pasta pai
# print(os.listdir("..\\.."))  
# print(os.listdir("C:\\Users"))
# print(os.listdir("C:\\Users\\Publico"))



# outros comandos uteis:
# Criar pasta
# os.mkdir("Aula 7")
# Renomear pasta 
# os.rename("Nova_Pasta", "pasta_renomeada")
# Excluir pasta
# os.rmdir("pasta_renomeada")


# Exercicio 4:
# crie um script que mostre o caminho da pasta atual.


# Exercicio 5:
# Liste os arquivos da pasta atual


# Exercicio 6:
#  Crie uma pasta chamada "projetos" e depois renomeie para "meus_projetos"fim, exclua a pasta

# os.mkdir("projetos")
# os.rename("projeto","meus_projetos")
# os.rmdir("meus_projeto")

#Exercicio 7
# crie um arquivo chamado 'log.txt' e escreva a mensagem depois, leia o conteudo do arquivo e exiba na tela


# with open("leg.txt", "w") as arquivo:
#     arquivo.write("log")



# pessoa = {
#     "nome": "Alice",
#     "idade": 30,
#     "cidade": "São Paulo",
#     "profissão": "Engenheira"
# }
# pessoa2 = {
#     "nome": "Bruno",
#     "idade": 25,
#     "cidade": "sp",
#     "profissão": 'Designer'
# }
# print(pessoa['cidade'])
# print(pessoa2['nome'], pessoa['idade'])

# Exemplo 2: Desligar o pc (comando para windows)

# with open('desliga.bat', 'w') as desligar:
#     desligar.write('shutdown -s -t 3600 -c \'desligamento programado para daqui a 1 hora. Salve seu trabalho!\'')
    # -s comando para desligar
    # -t tempo definir
    # -a cancelar desligamento