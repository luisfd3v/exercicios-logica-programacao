"""
    Faça um algoritmo que leia o ano em que uma pessoa nasceu,
    imprima na tela quantos anos, meses e dias essa pessoa ja viveu.
    Leve em consideração o ano com 365 dias e o mês com 30 dias.
    (Ex: 5 anos, 2 meses e 15 dias de vida)
"""
from datetime import datetime

ano_nascimento = int(input("Informe o ano em que você nasceu: "))

ano_atual = datetime.now().year
anos = ano_atual - ano_nascimento
dias = anos * 365
horas = dias * 24
minutos = horas * 60

print(f"Você já viveu {anos} anos, {dias} dias, {horas} horas, {minutos} minutos.")