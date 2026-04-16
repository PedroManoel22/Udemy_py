# 5. O Script de Seleção Inteligente
# Contexto: Você precisa buscar dados, mas quer que o Python te entregue algo mais útil que uma simples tupla.

# Tarefa: Configure o row_factory = sqlite3.Row. Faça um SELECT * na sua tabela de clientes.

# Ação: Percorra o resultado com um for e imprima uma frase formatada usando as chaves: f"O cliente {row['nome']} usa o email {row['email']}".

import sqlite3

DB_FILE = "SQLite/exs_extras/Script_selecao_inteligente/clientes.db"
TABLE_NAME = "clientes"


# Conectando ao servidor
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Selecionando toda a tabela

cursor.execute(f"SELECT * FROM {TABLE_NAME}")

print()

for row in cursor.fetchall():
    print(f"O cliente {row[0]} usa o email {row[1]}")

print()

cursor.close()
conn.close()
