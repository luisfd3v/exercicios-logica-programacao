"""
    Faça algoritmo que leia o nome e a idade de uma pessoa
    e imprima na tela o nome da pessoa e se ela é maior ou menor de idade. 
"""

nome = str(input("Informe o seu nome: "))
idade = int(input("Informe sua idade: "))

is_maior_idade = "maior de idade" if idade >= 18 else "menor de idade"

print(f"{nome} é {is_maior_idade}")