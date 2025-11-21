"""
    Faça um algoritmo que leia o valor de um produto e determine o valor que deve ser pago, 
    conforme a escolha da forma de pagamento pelo comprador e imprima na tela o valor final do produto a ser pago. 
    Utilize os códigos da tabela de condições de pagamento para efetuar o cálculo adequado.

    Tabela de Código de Condições de Pagamento
    1 - À Vista em Dinheiro ou Pix, recebe 15% de desconto
    2 - À Vista no cartão de crédito, recebe 10% de desconto
    3 - Parcelado no cartão em duas vezes, preço normal do produto sem juros
    4 - Parcelado no cartão em três vezes ou mais, preço normal do produto mais juros de 10%
"""

valor_produto = float(input("Informe o valor do produto: "))

pagamento_dinheiro_pix = valor_produto - (valor_produto * 0.15)
pagamento_cartao_credito = valor_produto - (valor_produto * 0.10)
pagamento_duas_parcelas = valor_produto
pagamento_tres_parcelas_mais = valor_produto + (valor_produto * 0.10)

print(f"Valor à vista no Dinheiro ou Pix R${pagamento_dinheiro_pix:.2f}.")
print(f"Valor à vista no cartão de crédito R${pagamento_cartao_credito:.2f}.")
print(f"Valor parcelado no cartão em duas vezes R${valor_produto:.2f}.")
print(f"Valor parcelado no cartão em três vezes ou mais R${pagamento_tres_parcelas_mais:.2f}.")

