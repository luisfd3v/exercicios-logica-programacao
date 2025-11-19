"""
    Faça um algoritmo que leia dois valores inteiros A e B,
    se os valores de A e B forem iguais, deverá somar os dois valores.
    Caso contrário devera multiplicar A por B.
    Ao final de qualquer um dos cálculos deve-se atribuir o resultado a uma variável C e imprimir seu valor na tela.
"""

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))

c = a + b if a == b else a * b
print(f"O valor de C é {c}")