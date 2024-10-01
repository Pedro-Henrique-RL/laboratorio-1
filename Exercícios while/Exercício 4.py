soma_idades = 0
maiores_de_idade = 0
entre_10_e_30 = 0
pessoas = 0

while pessoas < 7:
    idade = int(input("Informe a idade: "))
    peso = float(input("Informe o peso (kg): "))

    soma_idades += idade

    if idade >= 18:
        maiores_de_idade += 1

    if 10 <= idade <= 30:
        entre_10_e_30 += 1

    pessoas += 1

media_idades = soma_idades / 7
porcentagem_10_30 = (entre_10_e_30 / 7) * 100

print(f"Média das idades: {media_idades:.2f} anos")
print(f"Maiores de idade: {maiores_de_idade}")
print(f"Porcentagem entre 10 e 30 anos: {porcentagem_10_30:.2f}%")
