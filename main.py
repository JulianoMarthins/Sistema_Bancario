from banco import operacoes
from banco import cliente
from banco import conta

LIMITE_SAQUE = 500  # Constante, valor não deve ser alterado
saque_diario = 3

extrato = ""
saldo = 0.0

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
            """
                * Armazenar os usuários em uma lista
                * O usuário é composto por nome, data de nascimento, cpf, endereço -> dicionário
                * O endereço deve ter: Logradouro, numero, bairro, cidade, estado -> lista no endereco
                * Deve ser armazenado somente os números do CPF
                * Não pode ter CPF's repetidos
            """
            continue

        # Cadastra nova conta
        case 5:
            """
                * Armazenar em uma lista
                * Conta possuí: agência, número da conta, usuário
                * número da conta é seguêncial sendo a primeira o a conta número 1
                * O número da agência é fixo: "0001"
                * Usuário pode ter várias contas, mas uma conta pertencia a somente um usuário
                * Momento de criar a conta, deve ser vinculado obrigatóriamente a um usuário
                
                Obs: Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número de CPF
                informado para cada usuário da lista.
                
            """

            continue

        case _:
            print("ERRO! \n Valor digitado é inválido")
