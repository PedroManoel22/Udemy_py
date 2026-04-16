# 2. Cadastro em Lote de Clientes (executemany)
# Contexto: Você recebeu uma lista de novos usuários de um sistema legado e precisa importá-los.

# Tarefa: Dada a lista de tuplas abaixo, insira todos os registros de uma vez na tabela clientes (colunas: nome e email).

# novos_clientes = [('Ana', 'ana@email.com'), ('Beto', 'beto@email.com'), ('Caio', 'caio@email.com')]

# Dica Profissional: Utilize o executemany para demonstrar que você sabe como ganhar performance em inserções múltiplas.
import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = "clientes.db"
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = "clientes"


novos_clientes = [
    ("Ana", "ana@email.com"),
    ("Beto", "beto@email.com"),
    ("Caio", "caio@email.com"),
]

# Conectando ao banco de dados

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# criando a tabela

cursor.execute(
    f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} (nome TEXT PRIMARY KEY, email TEXT)"
)

connection.commit()

# Insierindo os clientes

sql = f"INSERT INTO {TABLE_NAME} (nome, email) VALUES (?, ?)"
cursor.executemany(sql, novos_clientes)

connection.commit()

cursor.close()
connection.close()
