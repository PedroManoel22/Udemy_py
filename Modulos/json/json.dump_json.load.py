import json
from pathlib import Path

# Pega o caminho da pasta onde o arquivo atual está
PASTA_ATUAL = Path(__file__).parent
NOME_ARQUIVO = "aula177.json"
CAMINHO_ABSOLUTO = PASTA_ATUAL / NOME_ARQUIVO
# print(CAMINHO_ABSOLUTO)

filme = {
    "title": "O senhor dos Anéis: A Sociedade do Anel",
    "original_title": "The Lord og the Rings: The Fellowship of the Ring",
    "is_movie": True,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
    "budget": None,
}

# Escrevendo o "filme" em um arquivo.json
with open(CAMINHO_ABSOLUTO, "w", encoding="utf-8") as file_object:
    json.dump(filme, file_object, ensure_ascii=False, indent=2)

# Lendo um arquivo.json
with open(CAMINHO_ABSOLUTO, "r") as file_object:
    filme_json = json.load(file_object)
    print(filme_json)
