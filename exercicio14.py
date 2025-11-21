"""
    Faça um algoritmo que receba um valor A e B, 
    e troque o valor de A por B e o valor de B por A e imprima na tela os valores.
"""

a = int(input("Informe o valor de A: "))
b = int(input("Informe o valor de B: "))

a, b = b, a

print(f"A agora vale {a}")
print(f"B agora vale {b}")