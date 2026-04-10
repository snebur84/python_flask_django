import sqlite3

def inicializar_banco():
    conexao = sqlite3.connect('estoque_papelaria.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            quantidade INTEGER NOT NULL DEFAULT 0,
            preco REAL NOT NULL
        )
    ''')

    cursor.execute("SELECT COUNT(*) FROM produtos")
    if cursor.fetchone()[0] == 0:
        produtos_iniciais = [
            ('Caderno 10 Matérias', 50, 25.90),
            ('Caneta Azul', 200, 1.50),
            ('Borracha Branca', 80, 0.80)
        ]
        cursor.executemany(
            'INSERT INTO produtos (nome, quantidade, preco) VALUES (?, ?, ?)', 
            produtos_iniciais
        )
        print("Dados iniciais inseridos com sucesso!")

    conexao.commit()
    conexao.close()
    print("Banco de dados e tabela prontos para uso.")

if __name__ == '__main__':
    inicializar_banco()