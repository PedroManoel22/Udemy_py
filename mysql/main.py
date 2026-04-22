# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL

import os

import dotenv
import pymysql

TABLE_NAME = "customers"
dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ["MYSQL_HOST"],
    user=os.environ["MYSQL_USER"],
    password=os.environ["MYSQL_PASSWORD"],
    database=os.environ["MYSQL_DATABASE"],
)

# print(os.environ["MYSQL_DATABASE"])

# Conectando e desconectando ao servidor MySQL
with connection:
    with connection.cursor() as cursor:
        # SQL
        cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(50) NOT NULL, idade INT NOT NULL)"
        )

        # cuidado: TRUNCATE TABLE apaga os dados, mas mantém a estrutura da tabela
        cursor.execute(f"TRUNCATE TABLE {TABLE_NAME}")

    connection.commit()

    # Inserindo elementos na tabela
    # with connection.cursor() as cursor:
    #     # SQL
    #     sql = f"INSERT INTO {TABLE_NAME} (nome, idade) VALUES (%s, %s)"
    #     data = (
    #         ("João", 30),
    #         ("Maria", 25),
    #         ("Pedro", 35),
    #         ("Fernando", 28),
    #         ("Ana", 22),
    #         ("Carla", 27),
    #         ("Lucas", 32),
    #         ("Mariana", 24),
    #         ("Rafael", 29),
    #         ("Sofia", 26),
    #     )

    #     result = cursor.executemany(sql, data)
    #     # print(result)  # número de linhas afetadas
    # connection.commit()

    # Inserindo elementos na tabela usando dicionário
    with connection.cursor() as cursor:
        # SQL
        sql = f"INSERT INTO {TABLE_NAME} (nome, idade) VALUES (%(nome)s, %(idade)s)"
        data = (
            {"nome": "Luiz", "idade": 31},
            {"nome": "Carla", "idade": 27},
            {"nome": "Lucas", "idade": 32},
            {"nome": "Ana", "idade": 22},
            {"nome": "Fernando", "idade": 28},
            {"nome": "Maria", "idade": 25},
            {"nome": "Pedro", "idade": 35},
            {"nome": "Mariana", "idade": 24},
            {"nome": "Rafael", "idade": 29},
            {"nome": "Sofia", "idade": 26},
        )

        result = cursor.executemany(sql, data)

        # print(result)  # número de linhas afetadas

    connection.commit()

    # Lendo valores da tabela com SELECT

    with connection.cursor() as cursor:
        # SQL
        sql = f"SELECT * FROM {TABLE_NAME}"  # * -> todos os campos
        cursor.execute(sql)

        result = cursor.fetchall()

        for row in result:
            print(row)

    print("\n-----------------------------------------------")

    # Lendo valores da tabela com WHERE
    with connection.cursor() as cursor:
        # SQL
        sql = f"SELECT * FROM {TABLE_NAME} WHERE idade > %s"  # WHERE id = 2
        cursor.execute(sql, (27,))
        result = cursor.fetchall()

        for row in result:
            print(row)

    # Lendo valores da tabela com WHERE com BETWEEN
    print("\n-----------------------------------------------")

    with connection.cursor() as cursor:
        # SQL
        sql = f"SELECT * FROM {TABLE_NAME} WHERE id BETWEEN %s AND %s"
        cursor.execute(sql, (2, 4))
        result = cursor.fetchall()

        for row in result:
            print(row)

    # Deletando valores da tabela com DELETE
    print("\n-----------------------------------------------")
    print("Deletando Carla...")
    with connection.cursor() as cursor:
        # SQL
        sql = f"DELETE FROM {TABLE_NAME} WHERE nome = %s"
        cursor.execute(sql, ("Carla",))
    connection.commit()

    # Editando valores da tabela UPDATE
    print("\n-----------------------------------------------")
    print("Editando Ana...")
    with connection.cursor() as cursor:
        # SQL
        sql = f"UPDATE {TABLE_NAME} SET nome = %s, idade = %s WHERE id = %s"
        cursor.execute(sql, ("heheheh", 36, 4))
        connection.commit()

        cursor.execute(f"SELECT * FROM {TABLE_NAME}")

        for row in cursor.fetchall():
            print(row)
