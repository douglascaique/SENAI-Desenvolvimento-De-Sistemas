# 6 – Faça um programa que leia o salário de um colaborador e quanto ele irá receber de aumento.
# Mostre o resultado do salário acrescentando o aumento digitado.

salarioColaborador = int(input('Insira o valor do salário em R$:'));
aumentoColaborador = int(input('Insira o valor do aumento de salário em R$:'));

salarioNovo = salarioColaborador + aumentoColaborador;

print('O novo salário do colaborador é de R$', salarioNovo);