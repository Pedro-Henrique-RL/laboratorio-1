moradores = 0
elevador_a = 0
elevador_b = 0
elevador_c = 0

while moradores < 10:
    elevador = input("Informe o elevador que utiliza com mais frequência (A, B ou C): ").upper()

    if elevador == 'A':
        elevador_a += 1
    elif elevador == 'B':
        elevador_b += 1
    elif elevador == 'C':
        elevador_c += 1
    else:
        print("Entrada inválida. Informe A, B ou C.")
        continue

    moradores += 1

porcentagem_a = (elevador_a / 10) * 100
porcentagem_b = (elevador_b / 10) * 100
porcentagem_c = (elevador_c / 10) * 100

print(f"\nTotal de pessoas que utilizam o elevador A: {elevador_a} ({porcentagem_a:.2f}%)")
print(f"Total de pessoas que utilizam o elevador B: {elevador_b} ({porcentagem_b:.2f}%)")
print(f"Total de pessoas que utilizam o elevador C: {elevador_c} ({porcentagem_c:.2f}%)")
