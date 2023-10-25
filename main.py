from time import sleep

print("Programado por Juliano Martins de Souza\n\n")

print("Bem vindo ao Poa's Bank ".center(60))

menu = """
                          Menu: 

                    (1) => Deposito
                    (2) => Saque
                    (3) => Extrato
                    (0) => Sair

    Digite p número que corresponde ao serviço desejado:
"""

LIMITE_SAQUE = 500  # Constante, valor não deve ser alterado
saque_diario = 3

extrato = ""
saldo = 0.0
print("=-" * 30)
while True:
    opcao = int(input(menu))
    print("=-" * 30)


    if opcao == 0:  # Opção para sair do sistema
        print("=-" * 30)
        print("Obrigado por visitar o Poa's Bank".center(60))
        sleep(1)
        break

    elif opcao == 1:    # Opção para realizar depósito
        valor = input("Digite o valor a depositar: ")
        valor = float(valor)

        if valor > 0:   # Verifica se o depósito será realizado com valores positivos
            saldo += valor
            print("=-" * 30)
            extrato += f"Deposito: R$ {valor:.2f}. Saldo atual R$ {saldo:.2f}\n"
            sleep(1)
        else:
            print("Valor de depósito inválido")

    elif opcao == 2:    # Opção para realizar saque
        if saque_diario > 0:
            valor = input("Digite o valor a sacar: ")
            valor = float(valor)

            if valor <= LIMITE_SAQUE:
                if valor <= saldo:
                    saldo -= valor
                    saque_diario -= 1
                    print("=-" * 30)
                    extrato += f"Saque: R$ {valor:.2f}. Saldo atual: R$ {saldo:.2f}\n"
                    sleep(1)
                else:
                    print("Saldo insuficiente")
                    sleep(1)
            else:
                print("Limite diário de saque excedido, favor consultar a gerência")
                print("=-" * 30)
                sleep(1)

        else:
            print("Limite de saque diários excedidos, duvidas, favor consultar a gerência")
            print("=-" * 30)
            sleep(1)

    elif opcao == 3:
        if extrato is None or len(extrato) == 0:
            print("Não há registros de movimentações nesta conta.")
            print("=-" * 30)
            sleep(1)
        else:
            print(f"Extrato:".center(60))
            print(extrato)
            print("=-" * 30)
            sleep(1)

    else:
        print("ERRO! \n Valor digitado é inválido")
        sleep(1)
