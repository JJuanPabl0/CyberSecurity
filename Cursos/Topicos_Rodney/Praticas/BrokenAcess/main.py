import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Criar a Tabela de Usuários
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    password TEXT NOT NULL
);
""")


# Inserir um usuário teste
cursor.execute("INSERT INTO users(name, password) VALUES ('juanAdmin', '1234')")
conn.commit()
conn.close()

print('Banco de Dados Criado com Sucesso!')

