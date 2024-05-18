Nome_Lista = [4, "computador", [9,8,7], 'Python', 11.5]
lista = [4,5,8,2,1,0.1]

# Len = Retorna o menor valor da lista
print(len(Nome_Lista))

# min = retorna o menor valor da lista
print(min(lista))

# max = retorna o maior valor da lista
print(max(lista))

# sum = retorna a soma dos valores da lista
print(sum(lista))

# append = adiciona um valor no final da lista
lista.append(10)
print(lista)

# insert = adiciona um valor em uma posição específica
lista.insert(0, 3)
print(lista)
lista.insert(3, 6)
print(lista)

# del = deleta um valor da lista
del lista[2]
print(lista)

# sort = ordena a lista em ordem crescente
lista.sort()
print(lista)

# reverse = inverte a ordem da lista
lista.reverse()
print(lista)


#teste de valores

print(7 in lista)
print(3 in lista)