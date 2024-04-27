# 9 - Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
# O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.
# O valor da prestação mensal não pode ser superior a 30% do salário.
# Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.


valorCasa = float(input('Qual o valor da casa a ser comprada?'))
salario = float(input('Qual o seu salário?'))
quantoTempo = float(input('Por quantos anos você deseja pagar?'))

mesesAPagar = quantoTempo * 12
prestacao = valorCasa / mesesAPagar

if prestacao > (salario * 0.30):
    print('Empréstimo não aprovado. O valor da prestação mensal é superior a 30% do salário. valor de R$:', prestacao)
else:
    print('Empréstimo aprovado! Valor da prestação mensal será de R$', prestacao)
