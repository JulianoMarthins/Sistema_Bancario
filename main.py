from banco import operacoes
from banco import cliente
from banco import conta
import textwrap

LIMITE_SAQUE = 500  # Constante, valor não deve ser alterado
saque_diario = 3

extrato = ""
saldo = 0.0
contador_contas_criadas = 1

clientes = []
contas = []

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
                    (6) => Clientes cadastrados
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

            saldo, extrato = operacoes.deposito(valor=valor, saldo=saldo, extrato=extrato)

        # Realização de saque
        case 2:
            print("Digite o valor a sacar: ".center(60))
            valor = input()
            valor = float(valor)
            saldo, extrato, saque_diario = operacoes.saque(valor, saldo, extrato,
                                                           saque_diario, LIMITE_SAQUE)

        # Retorna o extrato atualizado ao cliente
        case 3:
            print(f"Extrato:".center(60))
            texto = operacoes.mostrar_extrato(extrato)
            print(texto)
            print("=-" * 30)

        # Cadastra novos clientes
        case 4:
            print("Cadastro de cliete: ".center(60))
            print("Digite os dados do cliente: ".center(60))
            cliente_cadastrado = cliente.cadastrar_cliente()
            clientes.append(cliente_cadastrado);
            print('=-' * 30)
            
        # Cadastra nova conta
        case 5:
            print("Abertura de conta")

            conta_aberta, contador_contas_criadas = conta.criar_conta(contas, contador_contas_criadas)
            contas.append(conta_aberta)
            
            conta.associacao_conta(contas=contas, clientes=clientes)


            continue

        case 6:
            print(clientes)
           

        case _:
            print("ERRO! \n Valor digitado é inválido")
