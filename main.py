import os

LIMITE_SAQUE = 500  # Constante, valor não deve ser alterado
saque_diario = 3

extrato = ""
saldo = 0.0


# Método realiza deposito na conta
# Validação: Não aceito valores iguais ou inferior a zero
def deposito(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito: R$ {valor:.2f}; Saldo: R$ {saldo:.2f}\n"
        print("=-" * 30)
        print("Deposito realizado com sucesso")
        print("=-" * 30)
        return saldo, extrato
    else:
        print("=-" * 30)
        print("Valor inválido para depósito".center(60))
        print("Em caso de duvidas, favor entrar em contato com seu gerente de conta".center(60))
        print("=-" * 30)
        return None


# Método realiza saque da conta
# Validação: Limite de três saques por dia
# Validação: Limite de R$ 500,00 por saque
def saque(valor, saldo, extrato, saque_diario):
    if valor <= LIMITE_SAQUE:
        if saque_diario > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}; Saldo: R$ {saldo:.2f}\n"
            saque_diario -= 1
            print("=-" * 30)
            print("Saque realizado com sucesso")
            print("=-" * 30)
            return saldo, extrato
        else:
            print("=-" * 30)
            print("Limite de saque diário excedido")
            print("=-" * 30)
            return None
    else:
        print("=-" * 30)
        print("Valor soliticado acima do permitido")
        print("=-" * 30)
        return None


# Método retorna o extrato
# Validação: Verifica se o extrato possui lançamento para impressão
def mostrar_extrato(extrato):
    if extrato is None or len(extrato) == 0:
        return "Não há movimentação neta conta".center(60)
    else:
        return extrato


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
    match opcao:
        case 0:
            print("Obrigado por visitar o Poa's Bank".center(60))
            print("=-" * 30)
            break

        # Realização de depósito
        case 1:
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
        case 2:
            print("Digite o valor a sacar: ".center(60))
            valor = input()
            valor = float(valor)
            saldo, extrato = saque(valor, saldo, extrato, saque_diario)

        # Retorna o extrato atualizado ao cliente
        case 3:
            print(f"Extrato:".center(60))
            texto = mostrar_extrato(extrato)
            print(texto)
            print("=-" * 30)

        # Cadastra novos clientes
        case 4:
            continue

        # Cadastra nova conta
        case 5:
            continue

        case _:
            print("ERRO! \n Valor digitado é inválido")
