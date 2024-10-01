soma_salarios = 0
maior_idade = 0
menor_idade = 999
mulheres_ate_10000 = 0
pessoas = 0

while pessoas < 10:
    idade = int(input("Informe a idade: "))
    sexo = input("Informe o sexo (M/F): ").upper()
    salario = float(input("Informe o salário: "))

    soma_salarios += salario

    if idade > maior_idade:
        maior_idade = idade

    if idade < menor_idade:
        menor_idade = idade

    if sexo == 'F' and salario <= 10000:
        mulheres_ate_10000 += 1

    pessoas += 1

media_salarios = soma_salarios / 10

print(f"Média de salário do grupo: R${media_salarios:.2f}")
print(f"Maior idade: {maior_idade} anos")
print(f"Menor idade: {menor_idade} anos")
print(f"Quantidade de mulheres com salário até R$10000,00: {mulheres_ate_10000}")
