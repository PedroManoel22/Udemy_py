import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / "outro.csv"


# escrevendo como lista

# lista_clientes = [
#     ["Luiz Otávio", "Av 1, 22"],
#     ["João Silva", "R. 2, '1'"],
#     ["Maria Sol", "Av B, 3A"],
# ]

# with open(CAMINHO_CSV, "w", encoding="utf-8") as arquivo:
#     # colunas = lista_clientes[0].keys()
#     colunas = ["Nome", "Endereço"]
#     escritor = csv.writer(arquivo)

#     escritor.writerow(colunas)  # escrevendo

#     for cliente in lista_clientes:
#         escritor.writerow(cliente)


# Escrevendo como dicionário

lista_clientes = [
    {"Nome": "Luiz Otávio", "Endereço": "Av 1, 22"},
    {"Nome": "João Silva", "Endereço": "R. 2, '1'"},
    {"Nome": "Maria Sol", "Endereço": "Av B, 3A"},
]

with open(CAMINHO_CSV, "w", encoding="utf-8") as arquivo:
    colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(arquivo, fieldnames=colunas)

    escritor.writeheader()  # Escrevendo o cabeçalho

    for cliente in lista_clientes:
        escritor.writerow(cliente)  # Escrevendo as linhas
