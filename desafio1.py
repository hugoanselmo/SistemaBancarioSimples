
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=> """

saldo = 0
limite = 500
extrato = ""
numero_Saques = 0
LIMITE_SAQUES = 3
valor_deposito = 0
valor_saque = 0

while True:

    opcao = input(menu)

    if opcao == "d":
        valor_deposito = input("Informe o valor a ser depositado: ")
        if float(valor_deposito) < 0:
            print("O valor do depósito deve ser maior que 0.")
        else:
            saldo += float(valor_deposito)
            extrato += f"Depósito realizado no valor de R$ {float(valor_deposito):.2f}\n"

    elif opcao == "s":
        if numero_Saques < 3:
            valor_saque = input("Informe o valor a ser sacado: ")
            if float(valor_saque) > limite:
                print(f"O valor máximo permitido para saque é de R$ {limite:.2f}.")        
            elif float(valor_saque) > saldo:
                print(f"O valor solicitado excede o saldo disponível para saque.")
            else:
                if float(valor_saque) > 0:
                    numero_Saques += 1
                    saldo -= float(valor_saque)
                    extrato += f"Saque realizado no valor de R$ {float(valor_saque):.2f}\n"

        else:
            print("A quantidade de saques diária foi atingida, não é possível sacar.")

        
    
    elif opcao == "e":
        print("\n#######################Extrato Bancário#######################")
        print("\nNão foram relizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n##############################################################")

    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")