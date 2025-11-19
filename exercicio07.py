"""
    Faça um algoritmo que leia dois valores booleanos (lógicos)
    e determine se ambos são VERDADEIRO ou FALSO
"""

a = input("Informe True ou False: ").lower() == "true"
b = input("Informe True ou False: ").lower() == "true"

if a and b:
    print("Ambos são VERDADEIRO.")
elif not a and not b:
    print("Ambos são FALSO.")
else:
    print("Condições diferentes.")