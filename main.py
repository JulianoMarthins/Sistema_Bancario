from time import sleep

print()
print("Programado por Juliano Martins de Souza\n".center(60))

print("=-" * 30)
print()
print("Bem vindo ao Poa's Bank ".center(60))

menu = """
                          Menu: 

                    (1) => Deposito
                    (2) => Saque
                    (3) => Extrato
                    (0) => Sair

    Digite p número que corresponde ao serviço desejado:

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
"""

LIMITE_SAQUE = 500  # Constante, valor não deve ser alterado
saque_diario = 3

extrato = ""
saldo = 0.0

while True:
    opcao = int(input(menu))
    print("=-" * 30)

    # Fechar o programa
    if opcao == 0:

        print("Obrigado por visitar o Poa's Bank".center(60))
        print("=-" * 30)
        sleep(2)
        break

    # Realização de depósito
    elif opcao == 1:

        print("Digite o valor a depositar: ".center(60))
        valor = input()
        valor = float(valor)

        # Validação, depósito só ocorre com valores positivos
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}. Saldo atual R$ {saldo:.2f}\n"
            print("Deposito realizado com sucesso".center(60))
            print("=-" * 30)
            sleep(1)

        else:
            print("Valor de depósito inválido".center(60))
            print("=-" * 30)
            sleep(1)

    # Realização de saque
    elif opcao == 2:
        if saque_diario > 0:
            print("Digite o valor a sacar: ".center(60))
            valor = input()
            valor = float(valor)

            # Validação, verifica se o valor do saque está abaixo do limite por operação
            if valor <= LIMITE_SAQUE:

                # Validação, verifica se há saldo em conta para o saque
                if valor <= saldo:
                    saldo -= valor
                    saque_diario -= 1
                    print("=-" * 30)
                    extrato += f"Saque: R$ {valor:.2f}. Saldo atual: R$ {saldo:.2f}\n"
                    sleep(1)

                else:
                    print("Saldo insuficiente".center(60))
                    print("=-" * 30)
                    sleep(1)

            else:
                print("Limite diário de saque excedido, favor consultar a gerência".center(60))
                print("=-" * 30)
                sleep(1)

        else:
            print("Limite de saque diários excedidos, duvidas, favor consultar a gerência".center(60))
            print("=-" * 30)
            sleep(1)

    # Retorna o extrato atualizado ao cliente
    elif opcao == 3:

        # Validação, nega impressão do extrato caso o mesmo esteja sem informações
        if extrato is None or len(extrato) == 0:
            print("Não há registros de movimentações nesta conta.".center(60))
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
