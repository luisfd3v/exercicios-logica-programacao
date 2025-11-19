"""
    Faça um algoritmo que leia o valor do salário mínimo e o valor do salário de um usuário,
    calcule quantos salários mínimos esse usuário ganha e imprima na tela o resultado.
    (Base para o salário mínimo R$ 1.293,20).
"""

salario_minimo = 1293.20
salario_usuario = float(input("Informe o seu salário: "))

calculo_salarios = salario_usuario / salario_minimo

print(f"O usuário recebe {calculo_salarios} salário(s) mínimo(s)")