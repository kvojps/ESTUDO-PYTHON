import sqlite3

# Importante já ter a tabela criada no sqlite.
# Faça download do DB browser (SQLite)

class AgendaDB:
    def __init__(self, arquivo):
        self.conexao = sqlite3.connect(arquivo)
        self.cursor = self.conexao.cursor()

    def inserir(self, nome, telefone):
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)'
        self.cursor.execute(consulta,(nome, telefone))
        self.conexao.commit()

    def editar(self, nome, telefone, id):
        consulta = 'UPDATE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(consulta,(nome, telefone, id))
        self.conexao.commit()
        

    def excluir(self, id):
        consulta = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consulta,(id,))
        self.conexao.commit()
          

    def listar(self):
        self.cursor.execute('SELECT * FROM agenda')
        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, valor):
        consulta = 'SELECT * FROM agenda WHERE nome LIKE ? '
        self.cursor.execute(consulta, (f'%{valor}%',))
        self.conexao.commit()

    def fechar(self):
        self.cursor.close()
        self.conexao.close()

if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')
    agenda.listar()
