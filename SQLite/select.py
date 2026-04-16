import sqlite3

from main import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f"SELECT * FROM {TABLE_NAME}"
)  # * -> all, limit -> limita a quantidade de resultados

for row in cursor.fetchall():
    _id, name, weight = row
    print(f"id: {_id} | name: {name} | weight: {weight}")


cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE ID = '3'")

print()

row = cursor.fetchone()  # fetchone -> pega apenas um resultado
print(row)


cursor.close()
connection.close()
