'''
Um professor quer fazer um algoritmo para testar se uma questão de múltipla escolha está certa. Para isso, leia a questão assinalada pelo aluno e verifique:
A - resposta errada
B - resposta certa
C - resposta errada
D - resposta errada
'''
print("1- alternativa A")
print("2- alternativa B")
print("3- alternativa C")
print("4- alternativa D")

opcao = int(input("Escolha uma alternativa:"))

if opcao == 2:
    print("Alternatica correta")
else:
    print("Alternativa errada")
