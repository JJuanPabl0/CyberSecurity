import sqlite3

## Conectar com Banco de Dados. (se não existir, será criado)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Criar a Tabela de Usúarios

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    password TEXT NOT NULL
);
""")

# Inserir usúario Teste
cursor.execute("INSERT INTO users(name, password) VALUES ('admin', '1234')")
conn.commit()
conn.close()

print('Banco de Dados criado com sucesso!')