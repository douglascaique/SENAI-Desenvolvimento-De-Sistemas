from Aula3.funcaoPagamento import *

horasTrabalhadas = input('Quantas horas trabalhadas: ')
valorHora = input('Qual o valor por hora?: ')
totalSalario = calcularPagamento(horasTrabalhadas, valorHora)

print(f'O valor dos seus rendimentos é de: R${totalSalario}')