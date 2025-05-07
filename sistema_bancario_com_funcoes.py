import textwrap

def menu():
    menu = """

    [d]  Depositar
    [s]  Sacar
    [e]  Extrato
    [nu] Novo Usuário
    [nc] Nova Conta
    [lc] Listar Contas
    [q]  Sair


    => """

    return input(textwrap.dedent(menu))

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    print(f"numero_saques: {numero_saques}")
    if numero_saques >= limite_saques:
        print("A quantidade de saques diária foi atingida, não é possível sacar.")
    elif valor > limite:
            print(f"O valor máximo permitido para saque é de R$ {limite:.2f}.")        
    elif valor > saldo:
        print(f"O valor solicitado excede o saldo disponível para saque.")
    elif valor > 0:
            numero_saques += 1
            saldo -= valor
            extrato += f"Saque realizado no valor de R$ {valor:.2f}\n"
    else:
        print("O valor informado é invávlido. Saque não efetuado.")

    return saldo, extrato, numero_saques

def deposito(saldo, valor, extrato, /):
    if valor < 0:
        print("O valor do depósito deve ser maior que 0.")
    else:
        saldo += valor
        extrato += f"Depósito realizado no valor de R$ {valor:.2f}\n"
        
    return saldo, extrato

def mostrar_extrato(saldo, /, *, extrato):
    print("\n#######################Extrato Bancário#######################")
    print("\nNão foram relizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("\n##############################################################")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nEste usuário já foi cadastrado.")
        return
    
    nome = input("Informe o nome: ")
    data_nascimento = input("Informe a data de nascimento: dd-mm-aaaa ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("Usuário cadastrado com sucesso.")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta_corrente(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do titular da conta: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        return {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario
        }
    
    print("CPF não encontrato na base de dados.")

def listar_contas_correntes(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("*" * 100)
        print(textwrap.dedent(linha))

def main():
    AGENCIA = "0001"
    LIMITE_SAQUES = 3

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    valor_deposito = 0
    valor_saque = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            valor_deposito = float(input("Informe o valor a ser depositado: "))

            saldo, extrato = deposito(saldo, valor_deposito, extrato)

        elif opcao == "s":
            valor_saque = float(input("Informe o valor a ser sacado: "))

            saldo, extrato, numero_saques = saque(
                saldo=saldo,
                valor=valor_saque,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )           
        
        elif opcao == "e":
            mostrar_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta_corrente(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == "lc":
            listar_contas_correntes(contas)
        
        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()