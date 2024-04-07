numeros = [23, 34, 32, -12, 56, 76, -6, 87, -8, 21, 33, -5, 49]

listaPositivos = []
listaNegativos = []



for x in numeros:
    if x >= 0:
        listaPositivos.insert(0,x)
    else:
        listaNegativos.insert(0,x)



print(f'Soma da lista: {sum(numeros)}')



print(f'Lista com números positivos: {listaPositivos}')
print(f'Quantos números positivos: {len(listaPositivos)}')

print(f'Lista com números negativos: {listaNegativos}')
print(f'Quantos números negativos: {len(listaNegativos)}')