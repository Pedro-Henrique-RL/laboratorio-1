# Faça um algoritmo que simule uma conta bancária:
# 1 - Sacar
# 2 - Depositar
# 3 - Saldo
# 4 - Sair

# No início o algoritmo deve solicitar o saldo atual.

saldoAtual = float(input("Digite o seu saldo atual: "))
opcao = 0

while opcao != 4:
    print("1 - Sacar")
    print("2 - Depositar")
    print("3 - Saldo")
    print("4 - Sair")
    opcao = int(input("Digite a opção desejada:"))

    if opcao == 1:

        sacar = float(input("Digite o valor que deseja sacar: "))
        if sacar > saldoAtual or sacar <= 0:
            print("Não é possivel fazer o saque")
        else:
            saldoAtual = saldoAtual - sacar
            print("O saldo disponivel na conta é: ", saldoAtual)
    elif opcao == 2:
        deposito = float(input("Digite o valor do deposito: "))
        saldoAtual = deposito + saldoAtual
        print("O saldo atual da conta é: ", saldoAtual)
    elif opcao == 3:
        print("O seu saldo atual é: ", saldoAtual)
    elif opcao == 4:
        print("Até mais!")
    else:
        print("Digite uma opção valida")
