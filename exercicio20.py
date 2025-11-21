"""
    Faça um algoritmo que receba um valor inteiro e imprima na tela a sua tabuada.
"""

tabuada = int(input("Informe um número inteiro: "))

for x in range(11):
    print(f"A tabuada de {tabuada} x {x} = {tabuada * x}")