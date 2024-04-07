lista = [23, 34, 32, 12, 56, 76, 67, 87, 88, 21, 33, 50, 49]

listaCount = len(lista)

# for lista in range(5):
#     print('Ana')
    

# for x in range(listaCount):
#     print(f'Posição:{x} Valor: {lista[x]}')

listaPar = []
listaImpar = []

for x in lista:
    if x%2 == 0:
        # print(f'Valor par:{x}')
        listaPar.insert(0,x)
        listaPar.sort()

    else:
        listaImpar.insert(0,x)
        listaImpar.sort()
        

print(f'Valores Ímpares:{listaImpar}')
print(f'Valores Pares:{listaPar}')
# for x in lista:
#     if x%2 != 0:
#         print(f'Valores ímpares:{x}')

