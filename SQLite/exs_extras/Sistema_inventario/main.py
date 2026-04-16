# 1. O Sistema de Inventário (Tabela e Inserção Única)
# Contexto: Você precisa criar um banco para uma loja de tecnologia.

# Tarefa: Crie um arquivo loja.db. Crie uma tabela produtos com as colunas id (Primary Key), nome (Text) e preco (Real).

# Ação: Insira um único produto (ex: "Teclado Mecânico", 250.00) utilizando o método .execute() com placeholders (os ?).

import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = "loja.db"
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = "produtos"

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# criando a tabela = id nome preço
cursor.execute(
    f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} (id INTEGER PRIMARY KEY, nome TEXT, preco REAL)"
)

connection.commit()

sql = f"INSERT INTO {TABLE_NAME}(id, nome, preco) VALUES (?, ?, ?)"

cursor.executemany(sql, [[1, "Teclado Mecânico", 250.00]])

connection.commit()

cursor.close()
connection.close()
