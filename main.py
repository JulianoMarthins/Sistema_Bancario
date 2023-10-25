LIMITE_SAQUE = 500  # Constante, valor não deve ser alterado
saque_diario = 3

extrato = ""
saldo = 0.0


# Método abaixo realiza deposito na conta. Validação: Aceito valores acima de zero
def deposito(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito: R$ {valor:.2f}; Saldo: R$ {saldo:.2f}\n"
        print("Deposito realizado com sucesso")
        print("=-" * 30)
        return saldo, extrato
    else:
        print("Valor inválido para depósito".center(60))
        print("Em caso de duvidas, favor entrar em contato com seu gerente de conta".center(60))
        print("=-" * 30)
        return None






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
                    (4) => Cadastrar um novo cliente
                    (5) => Cadastrar conta bancária
                    (0) => Sair

    Digite o número que corresponde ao serviço desejado:

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
"""



while True:
    opcao = int(input(menu))
    print("=-" * 30)

    # Fechar o programa
    if opcao == 0:

        print("Obrigado por visitar o Poa's Bank".center(60))
        print("=-" * 30)

        break

    # Realização de depósito
    elif opcao == 1:
        while True:
            try:
                print("Digite o valor a depositar: ".center(60))
                valor = input()
                valor = float(valor)
                break
            except Exception as e:
                print("Digite um valor válido: ")

        saldo, extrato = deposito(valor=valor, saldo=saldo, extrato=extrato)



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


                else:
                    print("Saldo insuficiente".center(60))
                    print("=-" * 30)


            else:
                print("Limite diário de saque excedido, favor consultar a gerência".center(60))
                print("=-" * 30)


        else:
            print("Limite de saque diários excedidos, duvidas, favor consultar a gerência".center(60))
            print("=-" * 30)


    # Retorna o extrato atualizado ao cliente
    elif opcao == 3:

        # Validação, nega impressão do extrato caso o mesmo esteja sem informações
        if extrato is None or len(extrato) == 0:
            print("Não há registros de movimentações nesta conta.".center(60))
            print("=-" * 30)


        else:
            print(f"Extrato:".center(60))
            print(extrato)
            print("=-" * 30)


    else:
        print("ERRO! \n Valor digitado é inválido")







