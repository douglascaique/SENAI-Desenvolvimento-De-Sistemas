# while

#
# x = 1;
#
#
# while x <= 5:
#     print('o valor de x é de ', x)
#     if x == 2:
#         break
#     x += 1
#     print('Fim do While')

'''
while True:

    num1= input('Insira um número:')
    num2 = input('Insira outro número:')
    operador = input('Qual o tipo de operação? (+, -, /, *):')

    if not num1.isnumeric() or not num2.isnumeric():
        print('Insira apenas números!')
        continue

    num1 = int(num1)
    num2 = int(num2)

    # operadores

    if operador == '+':
        print('O resultado da soma é:', num1 + num2)
    elif operador == '-':
        print('O resultado da subtração é:', num1 - num2)
    elif operador == '/':
        print('O resultado da divisão é:', num1 / num2)
    elif operador == '*':
        print('O resultado da multiplicação é:', num1 * num2)
    else:
        print('Operador inválido!')

    sair = input('Deseja sair? (S) Sim    (N) Não: ')
    if sair == 's' or 'S':
        break
'''

# for n in range(index , limite ,step):
for n in range(5,11,1):
    print(n)