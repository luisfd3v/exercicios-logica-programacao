"""
    Faça um algoritmo que leia três notas obtidas por um aluno, e imprima na tela a média das notas.
"""

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))

media_nota = (nota1 + nota2 + nota3) / 3

print(f"A média das notas é: {media_nota}")