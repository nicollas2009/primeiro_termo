# Projeto 1:
# Projeto: Precisamos de um algoritmo para gerenciamento de cancelas para um shopping.
# Toda entrada e saída irá ser sinalizada
# Valores para entrada e permanência do veículo deverá ser pergutado
# As entrada deverão ser registradas por placa.
#
# Passo 1:  
# Perguntar informações sobre o veiculo ou forma acesso
# Pressionar o botao para emitir ticket
# Verificar se possui TAG para acesso liberado
# Se possuir erros informar ao usuário

# Passo 2:
# Verificar tempo de permanência
# Valor a ser cobrado

# Passo 3:
# Saída como será?
# Calcular tempo de permanência
# Se for TAG gerar na fatura da TAG
# Pagar ticket
# Devolver ticket na saída

# Passo 4:
# Gerar relatório de entradas e saídas
# Tratamento de Erros
# Revisão do código

while True:
    try:
        print("----- Seja Bem-Vindo(a) Ao Shopping Big -----")
        print("----- Digite as informações abaixo -----")

        placa = input("Digite a placa do veículo: ")
        modelo = input("Digite o modelo do veículo: ")
        cor = input("Digite a cor do veículo: ")2525
2525
        print("Novo Veículo Cadastrado:")
        print(f"Placa: {placa} | Modelo: {modelo} | Cor: {cor}")

        print("------------------------------------------------")

        print("Escolha o método de entrada.")
        print("Nossos sistemas: Ticket / Tag / Interfone")

        metodo_entrada = input("Digite o sistema de entrada: ")

        print(f"O sistema de entrada escolhido foi '{metodo_entrada}'.")

        if metodo_entrada == "Ticket":

            print("Sistema selecionado com sucesso.")
            print("Pague antes de sair.")

            hora_entrada = float(input("Digite a hora de entrada: "))
            hora_saida = float(input("Digite a hora da saída: "))

            if hora_saida < hora_entrada:
                    print("ERRO: Hora de saída não pode ser menor que a entrada.")

            else:
                    valor_estacionamento = 15

                    total_permanencia = hora_saida - hora_entrada
                    total_estacionamento = total_permanencia * valor_estacionamento

                    print(f"Tempo de permanência: {total_permanencia} horas")
                    print(f"Valor a ser cobrado: R$ {total_estacionamento}")

                    print("Devolver Ticket")
                    print("Saída liberada!")

        elif metodo_entrada == "Tag":

            print("TAG identificada com sucesso.")
            print("Sua permanência será cobrada na fatura.")

        elif metodo_entrada == "Interfone":

            print("Liberando acesso pelo interfone.")
            print("Sua saída deverá ser feita também pelo interfone.")

        else:

            print("ERRO: Método de entrada inválido.")

    except ValueError:
      print("Erro Encontrado, Tente Novamente.")
        continue

# ----------------------------------------------------------------------------------------

relatorio = input("")

print("--------------------------------------------------")
print("--------------------RELATÓRIO---------------------")
print("--------------------------------------------------")

