 # listas

carros = ['GOL', 'BMW', 'PEUGEOT', 'TESLA']

carros[2] = 'FERRARI'
carros[3] = 'FIAT'

# for x in carros:
#     print(x)

timePrincipal = ['RONALDINHO', 'CAFU', 'RAI', "TAFAREL"]
timeReserva = ['RUAN', 'SAMER', 'RAQUEL', 'ALANA', 'JONATHAN']


# time = timePrincipal + timeReserva


# timePrincipal.extend(timeReserva)
# print(timePrincipal)

# append() insere dados no final da lista
# timeReserva.append('DOUGLAS')
# print(timeReserva)

#insert() inserir em local exato
timePrincipal.insert(0,'EVERTON')
print(timePrincipal)

#del(nomedalista[index]) deleta um item especifico da lista
# del(timePrincipal[1])
# print(timePrincipal)

# desmembrar '...'

jogador1, jogador2, jogador3, jogador4, jogador5 = timePrincipal

print(f'Jogador 1 = {jogador1}')
print(f'Jogador 1 = {timePrincipal[0]}')
