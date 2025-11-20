"""
    Faça um algoritmo que leia quatro notas obtidas por um aluno,
    calcule a média das nota obtidas, imprima na tela o nome do aluno e se o aluno foi aprovado ou reprovado. 
    Para o aluno ser considerado aprovado sua média final deve ser maior ou igual a 7.
"""

nome = input("Informe o nome do aluno: ")
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
nota4 = float(input("Informe a quarta nota: "))

media_nota = (nota1 + nota2 + nota3 + nota4) / 4

is_aprovado = "Aprovado." if media_nota >= 7 else "Reprovado."

print(f"O aluno {nome} com média {media_nota:.2f} foi {is_aprovado}")