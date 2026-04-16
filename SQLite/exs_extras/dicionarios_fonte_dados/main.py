# 4. Dicionários como Fonte de Dados
# Contexto: Em APIs modernas, os dados geralmente chegam como dicionários (JSON).

# Tarefa: Crie um dicionário representando um produto: meu_produto = {'nome': 'Mouse Gamer', 'preco': 120.50}.

# Ação: Insira esse dicionário na tabela usando placeholders nomeados (ex: :nome e :preco) em vez de interrogações.

# Dica Pythônica: Isso torna o código muito mais legível e menos propenso a erros de ordem de colunas.

import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = "loja.db"
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = "produto"

meu_produto = {"nome": "Mouse Gamer", "preco": 120.50}

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# criando a tabela
cursor.execute(f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} (nome TEXT, preco REAL)")

connection.commit()

# Adicionando elemento com placeholders nomeados
sql = f"INSERT INTO {TABLE_NAME}(nome, preco) VALUES (:nome, :preco)"
cursor.execute(sql, meu_produto)

connection.commit()

cursor.close()
connection.close()
