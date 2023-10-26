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
        return saldo, extrato


# Método realiza saque da conta
# Validação: Limite de três saques por dia
# Validação: Limite de R$ 500,00 por saque
def saque(valor, saldo, extrato, saque_diario, LIMITE_SAQUE):
    if valor <= LIMITE_SAQUE:
        if saque_diario > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}; Saldo: R$ {saldo:.2f}\n"
            saque_diario -= 1
            print("=-" * 30)
            print("Saque realizado com sucesso")
            print("=-" * 30)
            return saldo, extrato, saque_diario
        else:
            print("=-" * 30)
            print("Limite de saque diário excedido")
            print("=-" * 30)
            return saldo, extrato, saque_diario
    else:
        print("=-" * 30)
        print("Valor soliticado acima do permitido")
        print("=-" * 30)
        return saldo, extrato, saque_diario


# Método retorna o extrato
# Validação: Verifica se o extrato possui lançamento para impressão
def mostrar_extrato(extrato):
    if extrato is None or len(extrato) == 0:
        return "Não há movimentação neta conta".center(60)
    else:
        return extrato
