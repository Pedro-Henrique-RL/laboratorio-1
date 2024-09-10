'''
Um sistema de uma loja de roupas permite que as peças de roupas sejam vendidas de três formas diferentes: 
À vista.
2 vezes.
3 vezes.
Para isso, o sistema deve ler o valor da peça, a opção de pagamento e apresentar o valor das parcelas.
'''

print("Bem vindo a lojinha da Fernanda")
print("1 - Pagar a vista")
print("2 - Pagar em 2x ")
print("3 - Pagar em 3x ")
opcao = int(input("Digite uma opção:"))

valorPeca = int(input("Digite o valor da peça:"))

if opcao == 1:
    valorFinal = valorPeca
    print("Valor da compra é:", valorPeca)
elif opcao == 2:
    valorFinal = valorPeca / 2
    print("Valor de cada parcela da peça será:", valorFinal)
elif opcao == 3:
    valorFinal = valorPeca / 3
    print("Valor de cada parcela da peça é:", valorFinal)
else:
    print("ERRO, igite uma opção valida")
