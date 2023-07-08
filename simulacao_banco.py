menu = """
********Menu********
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
********************
"""

saldo = 0
limite = 500
extrato = f""""""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("""A opção escolhida foi: Depósito""")

        try:
            valor_deposito = float(input(f"""Digite o valor que deseja depositar: \n"""))

            if valor_deposito > 0:
                extrato += f"""***Fora feito o deposito no valor de: R$ {valor_deposito:.2f}*** \n"""
                saldo += valor_deposito
            else:
                print("""O valor do deposito não pode ser negativo!\n""")

        except ValueError:
            print("""O valor inserido não é um número compatível.""")

    elif opcao == "s":
        print("""A opção escolhida foi: Saque""")

        try:
            valor_saque = float(input(f"""Saldo atual: {saldo:.2f} \nDigite o valor que deseja sacar:\n"""))
            if LIMITE_SAQUES <= numero_saques:
                print("""Você já atingiu o limite de saques diários""")

            elif valor_saque > limite:
                print("O valor de saque não pode ser maior que o limite de saque!")

            elif valor_saque > saldo:
                print("O valor a ser sacado não pode ser maior que o saldo da conta.")

            else:
                extrato += f"""***Fora feito um saque no valor de: {valor_saque:.2f}*** \n"""
                saldo -= valor_saque
                numero_saques += 1
                print(f"""Quantidades de saques disponiveis: {LIMITE_SAQUES - numero_saques}""")
        except ValueError:
            print("O valor inserido não é um número compatível.")

    elif opcao == "e":
        print("""A opção escolhida foi: Extrato""")
        extrato += f"""***extrato gerado, saldo em conta durante o extrato: R$ {saldo:.2f} \n"""
        print(extrato)

    elif opcao == "q":
        print("Obrigado por usar nosso sistema!")
        break

    else:
        print("A opção escolhida não é compatível, por favor selecione uma opção disponivel no menu.")
