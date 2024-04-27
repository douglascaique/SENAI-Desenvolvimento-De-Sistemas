# 7 - Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.
# Exiba o valor do desconto e o preço a pagar.

price = float(input('Insira o valor da mercadoria em R$:'));
percentualDesconto = float(input('Insira o percentual do desconto:'));

valorDesconto = (percentualDesconto / 100 ) * price

totalAPagar = price - valorDesconto;

print("O valor do desconto é R$:", valorDesconto)
print("O preço a pagar é R$:", totalAPagar)
