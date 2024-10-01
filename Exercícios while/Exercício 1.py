# Uma empresa de pesquisa deseja saber a média de altura e idade das pessoas, para isso, crie um algoritmo que apresente o seguinte menu:
# 1. Cadastrar pessoa
# Neste item, deve-se ler a altura e idade da pessoa.
# 2. Mostrar média parcial de altura e idade
# 3. Sair

# Após o usuário digitar 3, deve-se mostrar a média de altura
# e idade oficial.

opcao = 0
somaAltura = 0
somaIdade = 0
contador = 0


while opcao != 3:
    print("1 - Cadastrar pessoa")
    print("2. Mostrar média parcial de altura e idade")
    print("3 - Sair")
    opcao = int(input("Digite a opção desejada:"))

    if opcao == 1:
        idade = int(input("Digite a idade: "))
        altura = float(input("Digite a altura: "))
        somaAltura = somaAltura + altura
        somaIdade = somaIdade + idade
        contador = contador + 1
    elif opcao == 2:
        mediaAltura = somaAltura / contador
        mediaIdade = somaIdade / contador
        print("A media da altura é: ", mediaAltura, "e a media da altura é: ", mediaIdade)
    elif opcao == 3:
        mediaAltura = somaAltura / contador
        mediaIdade = somaIdade / contador
        print("A media da altura é: ", mediaAltura, "e a media da altura é: ", mediaIdade)
        print("Até mais!")
    else:
        print("Escolha uma das opçoes")
