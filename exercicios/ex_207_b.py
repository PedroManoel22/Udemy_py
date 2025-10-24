import json
from ex_207_a import Pessoa, caminho_arquivo
# lendo o arquivo Json
with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
    pessoas = json.load(arquivo)
    pessoa1 = Pessoa(**pessoas[0])
    pessoa2 = Pessoa(**pessoas[1])
    pessoa3 = Pessoa(**pessoas[2])
    print(pessoa1.nome, pessoa1.idade)
    print(pessoa2.nome, pessoa2.idade)
    print(pessoa3.nome, pessoa3.idade)
