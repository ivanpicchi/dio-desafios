#DESAFIO: Criar sistema bancário com um MENU com as seguintes OPERAÇÕES: [s] sacar, [d] depositar, [e] visualizar extrato e [q] sair.
#Todos os depositos devem ser armazenados em uma variável e exibidos no extrato
#Limite de saques diários = 3 --> limite de R$500,00 por saque 
#Se não tiver saldo em conta, exibir mensagem informando "Não será possivel sacar o dinheiro por falta de saldo". [ok]
#Extrato deve listar TODOS os depósitos e saques na conta [ok]
#Formato dos valores --> R$ XXXX.XX [ok]
#Apenas é permitido valores POSITIVOS de DEPÓSITO [ok]

#MENU
menu = '''
Bem vindo ao Banco Teste V1.0b -- Ivan Picchi

-----MENU-----
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
--------------

Selecione uma das operações: '''

#VARIÁVEIS

saldo = 0
limite = 500
extrato = []
n_saque = 0
LIMITE_SAQUES = 3 #Limite FIXO de 3 saques por dia

while True: #Loop infinito
    opcao = input(menu) #opção selecionada no menu
    
    if opcao == 'd': #operação de DEPÓSITO
        print('Depósito')
        deposito = float(input("Digite o valor a depositar: R$" ))
        if deposito <= 0: #Restrição de valor negativo para DEPÓSITOe
            print(f'O valor R${deposito:.2f} não é um valor permitido para a operação de depósito.')
            print('Reinicie o programa e escolha outra operação ou valor válido')
        else:
            saldo += deposito
            deposito_extrato = f"(+ R${deposito:.2f})"
            extrato.append(deposito_extrato)
            print(f'Foi realizado o depósito no valor de R${deposito:.2f}. Seu saldo atual é R${saldo:.2f}')

    
    elif opcao == 's':
        if opcao == 's': #operação de SAQUE
            print("Saque")
            saque = float(input("Digite o valor a sacar: R$" ))            
            if n_saque >= 3: #Condicional de 3 saques por dia
                print(f'Você excedeu a quantidade diária de saque: {LIMITE_SAQUES:.2f}. Fale com o gerente de sua conta para analisar a situação.')
            elif saque > 500: #Condicional de R$500 por saque
                print(f'Você excedeu seu limite de saque: R${limite:.2f}. Fale com o gerente de sua conta para analisar a situação.')
            elif saque > saldo: #Condicional valor do saque maior que o saldo
                print(f'Saldo insuficiente: o valor de R${saque:.2f} é maior que o seu saldo atual de R${saldo:.2f}')            
            else: #Condição na qual o saque é permitido
                saldo -= saque
                n_saque += 1
                saque_extrato = f"(- R${saque:.2f})"
                extrato.append(saque_extrato)
                print(f'Foi realizado o saque no valor de R${saque:.2f}. Seu saldo atual é R${saldo:.2f}')
                
                


    elif opcao == 'e': #operação de SAQUE
        if opcao == 'e':
            print("Extrato")
            for op in extrato:
                print(op)
        print(f'''
              --------------------------------------------------------
                O seu saldo atual é de: R${saldo:.2f}                    
                Você ainda pode realizar {LIMITE_SAQUES - n_saque} saques hoje. 
              --------------------------------------------------------
              ''')
                

    elif opcao == 'q':
        print('Obrigado por utilizar nosso banco e volte sempre!')
        break

    else: print("Operação inválida: por favor, selecione novamente a operação desejada")
