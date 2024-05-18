import sqlite3


conexao = sqlite3.connect('bancoaula.db')
cursor = conexao.cursor()

# cursor.execute('CREATE TABLE IF NOT EXISTS clientes('
#                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#                'nome TEXT,'
#                'idade INT'
#                 ')')



# cursor.execute('INSERT INTO clientes (nome,idade) values ("Douglas", 25)')
# cursor.execute('INSERT INTO clientes (nome,idade) values ("Luis", 13)')
# cursor.execute('DELETE FROM clientes WHERE id ("Luis", 13)')



cursor.execute('SELECT * FROM clientes')

conexao.commit()

for linha in cursor.fetchall():
    print(linha)


cursor.close()
conexao.close()
