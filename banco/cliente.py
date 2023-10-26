def cadastrar_cliente():
    cpf = input("CPF: ").replace('-', '').replace('.', '')

    if cpf not in clientes:
        nome = input("Nome: ")
        nascimento = input("Data de nascimento => [dd/mm/aaaa]: ")
        rua = input("Rua: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        estado = input("UF: ")

        endereco = [rua, bairro, cidade, estado]
        cadastro = {'nome': nome, 'cpf': cpf, 'nascimento': nascimento, 'endereco': endereco}

        return cadastro
    
    else:
        print("CPF já cadastrado. Em caso de dúdivdas, favor falar com seu gerente de conta")
        return None
            