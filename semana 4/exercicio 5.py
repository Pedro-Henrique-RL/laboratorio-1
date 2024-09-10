carteira = str(input("Qual a sua carteira de motorista? "))

carteiraA = "Motos e triciclos"
carteiraB = "Carros de passeio"
carteiraC = "Veiculos de carga acima de 3,5 ton"
carteiraD = "Veiculos com mais de 8 passageiros"
carteiraE = "Veiculos com unidade acoplada acima de 6 ton"

if carteira == "carteiraA":
    print(carteiraA)
elif carteira == "carteiraB":
    carteira = carteiraB
    print(carteiraB)
elif carteira == "carteiraC":
    print(carteiraC)
elif carteira == carteiraD:
    print(carteiraD)
elif carteira == "carteiraE":
    print(carteiraE)
else:
    print("Digite uma carteira real")
