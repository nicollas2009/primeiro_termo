# Sistema de Elevador de Prédio
# O prédio possui 10 andares, sendo o térreo o andar 0. O elevador pode se mover para cima ou para baixo, e tem a capacidade de transportar até 5 pessoas.
# O elevador começa no andar 0 e pode ser chamado por qualquer pessoa em qualquer andar.
# O elevador deve se mover para o andar onde a pessoa chamou, e depois para o andar destino da pessoa.
# O elevador deve exibir mensagens indicando o andar atual, o número de pessoas no elevador, e as ações realizadas (subindo, descendo, parando). O programa deve continuar rodando até que o usuário decida encerrar.






print("Bem-vindo ao Elevador Python!")
andar_atual = 0
pessoas = 0  

while True:
    try:
        
        print(f"\nElevador no andar {andar_atual}. Pessoas a bordo: {pessoas}/5")
        novas_pessoas = int(input("Quantas pessoas vão entrar? "))
        if novas_pessoas < 0 or (pessoas + novas_pessoas) > 5:
            raise ValueError("Capacidade máxima de 5 pessoas excedida ou número inválido.")
        
       
        origem = int(input("Digite o andar onde você está (0-10): "))
        if origem < 0 or origem > 10:
            raise ValueError("Andar de origem inválido. Use de 0 a 10.")

    
        if andar_atual != origem:
            acao = "SUBINDO" if origem > andar_atual else "DESCENDO"
            print(f"[{acao}] Elevador se movendo do andar {andar_atual} para o andar {origem} (Chamada)...")
            andar_atual = origem
            print(f"[PARANDO] Chegamos ao andar {andar_atual}! Entrando {novas_pessoas} pessoas.")
        
        pessoas += novas_pessoas

        
        destino = int(input("Digite o andar de destino (0-10): "))
        if destino < 0 or destino > 10:
            raise ValueError("Andar inválido. Por favor, digite um número entre 0 e 10.")
        
        
        if destino != andar_atual:
            acao = "SUBINDO" if destino > andar_atual else "DESCENDO"
            print(f"[{acao}] Elevador se movendo do andar {andar_atual} para o andar {destino}...")
            andar_atual = destino
            print(f"[PARANDO] Chegamos ao andar {andar_atual}!")
        else:
            print(f"[PARANDO] Você já está no andar {destino}!")

        
        print(f"Desembarcando {pessoas} pessoas...")
        pessoas = 0 

        
        print("\nMapa do Prédio:")
        for listagem in range(11):
            print(f"Andar {listagem:02d} - {'[X]' if listagem == andar_atual else '[ ]'}")

        if input("\nDeseja escolher outro andar? (s/n): ").lower() != 's':
            print("Obrigado por usar o Elevador Python! Até a próxima!")
            break

    except ValueError as erro:
        print(f"Erro: {erro}. Tente novamente.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}. Tente novamente.")
        print("Programa encerrado.")
        break



