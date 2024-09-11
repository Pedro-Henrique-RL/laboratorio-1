# Crie um programa que leia o nome, o salário e o tempo de serviço de um funcionário e informe se ele tem direito a receber um aumento. 
# O funcionário deve ter pelo menos 5 anos de serviço e o salário não pode ser superior a R$ 2.000,00 para receber o aumento de 10%. Caso contrário, o aumento é de 5%.

nome = input("Nome: ")
salario = float(input("Digite seu salario: "))
tempoServico = float(input("Digite seu tempo de serviço:"))

if tempoServico >= 5 and salario >= 2000:
    salarioNovo = salario * 0.10
    salario = salario + salarioNovo
    print("Você recebeu um aumento de 10%, seu salario é: ", salario)
else:
    salarioNovo = salario * 0.05
    salario = salario + salarioNovo
    print("Você recebeu um aumento de 10%, seu salario é: ", salario)
