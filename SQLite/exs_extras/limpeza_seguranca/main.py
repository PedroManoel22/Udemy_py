# 3. Limpeza de Segurança (DELETE e SQLite Sequence)
# Contexto: Após realizar testes, você precisa limpar sua tabela de "Logs" para deixá-la pronta para produção, começando o ID do zero.

# Tarefa: 1. delete todos os dados da tabela logs.
# 2. Execute o comando para resetar a tabela interna sqlite_sequence (visto na aula 393).

# Objetivo: Garantir que o próximo item inserido tenha o id = 1.

import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = "logs.db"
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = "logs"

clientes = [("123", "Pedro"), ("456", "Luiz"), ("789", "Ana"), ("369", "João")]

# Conectando ao servidor

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# Deletar a tabela inteira
cursor.execute(f"DELETE FROM {TABLE_NAME}")

# Zerar o id da tabela
cursor.execute(f"DELETE FROM sqlite_sequence WHERE name='{TABLE_NAME}'")


# Criando a tabela de logs para o exemplo

cursor.execute(
    f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} (id INTEGER PRIMARY KEY AUTOINCREMENT, login  TEXT, name TEXT)"
)

connection.commit()

# Inserindo os logs
sql = f"INSERT INTO {TABLE_NAME} (login, name) VALUES (?, ?)"
cursor.executemany(sql, clientes)

connection.commit()

cursor.close()
connection.close()
