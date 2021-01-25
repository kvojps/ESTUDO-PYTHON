import sqlite3

conexao = sqlite3.connect('basedados.db')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS clientes('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'nome TEXT,'
    'peso REAL'
    ')')

cursor.execute('INSERT INTO clientes (nome, peso) VALUES( ? , ?)', ('Maria', 80))
conexao.commit()

# cursor.execute('UPDATE clientes SET nome= ? WHERE id = ?',('Luciene', 2))
# cursor.execute('DELETE FROM clientes WHERE id =:id',{'id': 2})
# conexao.commit()

cursor.execute('SELECT * FROM clientes')

for linha in cursor.fetchall():
    print(linha)

cursor.close()
conexao.close()