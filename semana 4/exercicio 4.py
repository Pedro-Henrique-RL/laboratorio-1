'''
Faça um algoritmo que leia dois valores. Posteriormente leia uma opção do menu:  
1. Somar os dois valores.
2. Subtrair os dois valores.
3. Multiplicar os dois valores.
4. Dividir os dois valores
'''

numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite um numero: "))


print("1. Somar os dois valores.")
print("2. Subtrair os dois valores.")
print("3. Multiplicar os dois valores.")
print("4. Dividir os dois valores")

opcao = int(input("Escolha uma opção: "))

if opcao == 1:
    soma = numero1 + numero2
    print(soma)
elif opcao == 2:
    subtrair = numero1 - numero2
    print(subtrair)
elif opcao == 3:
    multiplicacao = numero1 * numero2
    print(multiplicacao)
elif opcao == 4:
    divisao = numero1 / numero2
    print(divisao)
else:
    print("Escolha uma opção valida")
