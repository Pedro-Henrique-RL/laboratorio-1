# Fazer um algoritmo que leia diversos números e mostre quantas vezes o número 10 foi digitado. O laço de repetição deve parar quando o usuário digitar 0. 

num = 1
contador = 0

while num != 0:
    num = int(input("Digite um numero: "))
    if num == 10:
        contador += 1
    elif num == 0:
        print("Saindo do programa")
print(f"O numero 10 foi escolhido :{ contador} vezes")
