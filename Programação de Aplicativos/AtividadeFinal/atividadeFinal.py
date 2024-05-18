import sqlite3

conexao = sqlite3.connect('bancoAtvFinal.db')
cursor = conexao.cursor()

# cursor.execute('CREATE TABLE IF NOT EXISTS clientes('
#                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#                'nome TEXT,'
#                'idade INT,'
#                'senha TEXT,'
#                'email TEXT'
#                 ')')

# cursor.execute('CREATE TABLE IF NOT EXISTS produtos('
#                'idProduto INTEGER PRIMARY KEY AUTOINCREMENT,'
#                'nomeProduto TEXT,'
#                'peso INT,'
#                'cor TEXT,'
#                'tamanho TEXT'
#                 ')')

# cursor.execute('CREATE TABLE IF NOT EXISTS servicos('
#                'idServico INTEGER PRIMARY KEY AUTOINCREMENT,'
#                'nomeServico TEXT,'
#                'localServico TEXT,'
#                'nomeCliente TEXT,'
#                'valorServico INT'
#                 ')')






# cursor.execute('INSERT INTO clientes (nome,idade,senha,email) values ("Douglas", 25, "1234", "teste@teste.com")')
# cursor.execute('INSERT INTO clientes (nome,idade,senha,email) values ("Milena", 27, "1234", "teste@teste.com")')
# cursor.execute('INSERT INTO clientes (nome,idade,senha,email) values ("Lucca", 7, "1234", "teste@teste.com")')
# cursor.execute('INSERT INTO clientes (nome,idade,senha,email) values ("Jaci", 73, "1234", "teste@teste.com")')

# cursor.execute('DELETE FROM clientes WHERE id = 4')



# cursor.execute('INSERT INTO produtos (nomeProduto,peso,cor,tamanho) values ("Garrafa", 00.5, "Verde", "10cm")')
cursor.execute('INSERT INTO produtos (nomeProduto,peso,cor,tamanho) values ("Luvas", 0800, "Vermelho", "10cm Cada")')
cursor.execute('INSERT INTO produtos (nomeProduto,peso,cor,tamanho) values ("Pente", 025, "Preto", "20cm")')

# cursor.execute('SELECT * FROM clientes')
cursor.execute('SELECT * FROM produtos')
# cursor.execute('SELECT * FROM servicos')


conexao.commit()

for linha in cursor.fetchall():
    print(linha)

cursor.close()
conexao.close()