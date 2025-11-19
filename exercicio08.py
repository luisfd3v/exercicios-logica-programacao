"""
    Faça um algoritmo que leia três valores inteiros deiferentes e imprima na tela os valores em ordem decrescente.
"""

valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite um segundo valor: "))
valor3 = int(input("Digite um terceiro valor: "))

lista_valores = [valor1, valor2, valor3]
lista_valores_decrescente = sorted(lista_valores)

print(f"A ordem decrescente dos valores é: {lista_valores_decrescente}")