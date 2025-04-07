import sqlite3

conn = sqlite3.connect("users.db")
cursos = conn.cursor()

# Criar a Tabela de Usúarios
