numeros = 0
quantidade_30_90 = 0

while numeros < 10:
    numero = int(input("Informe um número: "))

    if 30 <= numero <= 90:
        quantidade_30_90 += 1

    numeros += 1

print(f"Quantidade de números entre 30 e 90: {quantidade_30_90}")
