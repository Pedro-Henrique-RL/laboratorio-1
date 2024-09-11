# Faça um script que peça os 3 lados de um triângulo. O script deverá informar se os valores podem ser um triângulo. 
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

# Dicas:
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

lado1 = input("Digite o valor de um lado do triangulo: ")
lado2 = input("Digite o o valor do segundo lado do triangulo: ")
lado3 = input("Digite o valor do terceiro lado do triangulo: ")

if lado1 == lado2 == lado3:
    print("O triangulo é um equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("O triangulo é Isósceles")
else:
    print("O triangulo é Escaleno")
