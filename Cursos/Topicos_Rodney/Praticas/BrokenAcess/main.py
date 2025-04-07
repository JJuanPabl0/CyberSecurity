import sqlite3

conn = sqlite3.connect("users.db")
cursos = conn.cursor()

# Criar a Tabela de Usúarios
cursos.execute("""
CREATE TABLE IS NOT EXISTS users(
    id INTENGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    password TEXT NOT NULL             
);
""")


