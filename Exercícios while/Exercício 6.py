pessoas = 0
maiores_de_18 = 0

while pessoas < 10:
    idade = int(input("Informe a idade: "))

    if idade >= 18:
        maiores_de_18 += 1

    pessoas += 1

print(f"Quantidade de pessoas com idade maior ou igual a 18 anos: {maiores_de_18}")
