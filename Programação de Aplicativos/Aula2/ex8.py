# 8 - Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, de 15%.



salarioColaborador = float(input('Insira o valor do salário em R$:'));


if salarioColaborador > 1250:
    aumento = salarioColaborador * 0.10;
    novoSalario = salarioColaborador + aumento;
else:
    aumento = salarioColaborador * 0.15;
    novoSalario = salarioColaborador + aumento;

print('o valor do aumento é de R$:', aumento)
print('o novo valor do salário é de R$:', novoSalario)
