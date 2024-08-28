anoNascimento = int(input("Digite o seu ano de nascimento:"))
anoAtual = 2024
idade = anoAtual - anoNascimento

if idade >= 18:
    print("Você pode votar")
else:
    print("Você não pode votar")
