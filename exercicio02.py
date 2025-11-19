"""
    Faça um algoritmo para receber um número qualquer
    e imprimir na tela se o número é par ou ímpar, positivo ou negativo.
"""

numero = int(input("Informe um número: "))

print(f"{numero} é um número par" if numero % 2 == 0 else f"{numero} é um número ímpar")
print(f"{numero} é um número positivo" if numero > 0 else f"{numero} é um número negativo")