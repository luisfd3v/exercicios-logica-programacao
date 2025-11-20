"""
    Faça um algoritmo que calcule o IMC (Índice de Massa Corporal) de uma pessoa,
    leia o seu peso e sua altura e imprima na tela sua condição de acordo com a tabela abaixo:
    
    Fórmula do IMC = peso / (altura)²
    Tabela Condições IMC
    Abaixo de 18,5   | Abaixo do peso          
    Entre 18,6 e 24,9 | Peso ideal (parabéns)  
    Entre 25,0 e 29,9 | Levemente acima do peso
    Entre 30,0 e 34,9 | Obesidade grau I 
    Entre 35,0 e 39,9 | Obesidade grau II (severa)
    Maior ou igual a 40 | Obesidade grau III (mórbida)
"""

peso = float(input("Informe o seu peso: "))
altura = float(input("Informe sua altura: "))

imc = peso / (altura ** 2)
imc = round(imc, 2)
# imc = 40

if imc < 18.5:
    print(f"{imc} | Abaixo do peso")
elif imc < 25:
    print(f"{imc} | Peso ideal")
elif imc < 30:
    print(f"{imc} | Levemente acima do peso")
elif imc < 35:
    print(f"{imc} | Obesidade grau I")
elif imc < 40:
    print(f"{imc} | Obesidade grau II")
else:
    print(f"{imc} | Obesidade grau III")