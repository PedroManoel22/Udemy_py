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

    with connection.cursor() as cursor:
        # SQL
        sql = f"INSERT INTO {TABLE_NAME} (nome, idade) VALUES (%s, %s)"
        data = (
            ("João", 30),
            ("Maria", 25),
            ("Pedro", 35),
            ("Fernando", 28),
            ("Ana", 22),
            ("Carla", 27),
            ("Lucas", 32),
            ("Mariana", 24),
            ("Rafael", 29),
            ("Sofia", 26),
        )

        result = cursor.executemany(sql, data)

        # print(result)  # número de linhas afetadas

    connection.commit()
