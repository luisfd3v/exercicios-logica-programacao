"""
    Faça um algoritmo que leia um valor qualqer e imprima na tela com um reajuste de 5%.
"""

valor = float(input("Informe um número: "))
valor_reajuste = valor + valor * 0.05

print(f"Com reajuste de 5% é {valor_reajuste}")