import sqlite3

from main import DB_FILE, TABLE_NAME

# CRUD - Create Read     Update    Delete
# SQL -  INSERT SELECT   UPDATE    DELETE


connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# Deletar a tabela inteira
cursor.execute(f"DELETE FROM {TABLE_NAME}")

# Zerar o id da tabela
cursor.execute(f"DELETE FROM sqlite_sequence WHERE name='{TABLE_NAME}'")

# Cria a tabela
cursor.execute(
    f"CREATE TABLE IF NOT EXISTS {TABLE_NAME}"
    "("
    "id INTEGER PRIMARY KEY AUTOINCREMENT,"
    "name TEXT,"
    "weight REAL"
    ")"
)

connection.commit()

# Registrar valores nas colunas da tabela

sql = f"INSERT INTO {TABLE_NAME}(name, weight) VALUES(?, ?)"
cursor.execute(sql, ["Pedro", 45])

# inserindo vários valores
cursor.executemany(sql, [["Pedro", 62], ["Luiz", 5]])  # Também podemos usar tuplas

connection.commit()


if __name__ == "__main__":
    print(sql)
    # Deletando o id 2 -> sempre lembre de colocar o where no delete
    cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE ID = '3'")

    connection.commit()

    cursor.execute(f"SELECT * FROM {TABLE_NAME}")

    for row in cursor.fetchall():
        _id, name, weight = row
        print(f"id: {_id} | name: {name} | weight: {weight}")

    # Fechando a conexão
    cursor.close()
    connection.close()
