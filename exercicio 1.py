'''
Faça um algoritmo que leia dois valores e apresente:
O maior deles
O menor deles

Obs. o algoritmo deve verificar se os valores digitados são iguais
'''

numero1 = int(input("Digite um numero:"))
numero2 = int(input("Digite um numero:"))

if numero1 == numero2:
    print("São iguais")
elif numero1 > numero2:
    print(numero1)
elif numero1 < numero2:
    print(numero2)
