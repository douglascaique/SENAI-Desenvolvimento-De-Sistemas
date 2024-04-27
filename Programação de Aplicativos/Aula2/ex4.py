# 4 – Escreva um programa que pergunte a quantidade de km percorridos por um carro
# alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.


quantosDias = int(input('Por quantos dias você alugou o carro?: '))
quantosKm = int(input('Quantos KM percorridos de carro?: '))

priceDay = quantosDias * 60;
priceKm = quantosKm * 0.15;

resultadoRodado = priceDay + priceKm

print('O preço total a ser pago pelo aluguel é de R$:', resultadoRodado, '.')
