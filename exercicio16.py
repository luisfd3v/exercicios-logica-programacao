"""
    Faça um algoritmo que leia três valores que representam os três lados de um triângulo 
    e verifique se são válidos, determine se o triângulo é equilátero, isósceles ou escaleno.
"""

valor1 = int(input("Informe um valor: "))
valor2 = int(input("Informe um segundo valor: "))
valor3 = int(input("Informe um terceiro valor: "))


if (valor1 < valor2 + valor3) and (valor2 < valor1 + valor3) and (valor3 < valor1 + valor2):
    
    if valor1 == valor2 == valor3:
        print("Triângulo Equilátero")
    elif valor1 == valor2 or valor1 == valor3 or valor2 == valor3:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")

else:
    print("Os valores informados não formam um triângulo.")
