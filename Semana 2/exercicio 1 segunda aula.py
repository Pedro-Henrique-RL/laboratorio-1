porHora = 35.00
horasPorMes = int(input("Digite as horas que trabalhou no mês: "))
valorFinal = porHora * horasPorMes 

print("Salario no Mês: ", valorFinal)

if valorFinal <= 1000:
    total = valorFinal + 300
    print("Salario com bonus: ",total)
else:
    print("Salario", valorFinal)
