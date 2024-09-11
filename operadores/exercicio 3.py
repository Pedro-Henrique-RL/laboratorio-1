# Faça um algoritmo que leia as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. 
# Também solicite qual a % de frequência e aula, verifique e apresente a seguinte mensagem:
# Aprovado: Nota maior ou igual a 7,0 e frequência igual ou superior a 75%.
# Exame: Nota maior ou igual a 4,0 e menor que 7,0 e frequência superior a 75%.
# Reprovado: Nota inferior a 4,0 ou frequência menor que 75%.

nota1 = int(input("Digite sua primeira nota: "))
nota2 = int(input("Digite sua segunda nota: "))

media = (nota1 + nota2) / 2

frequencia = int(input("Digite sua frequencia(em %): "))

if media >= 7 and frequencia >= 75:
    print("Aprovado")
elif media >= 4 and frequencia >= 75:
    print("Exame")
elif media < 4 or frequencia < 75:
    print("Reprovado")
