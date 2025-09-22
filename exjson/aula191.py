import json

# pessoa = {
#     'nome': 'Pedro',
#     'Sobrenome': 'Manoel',
#     'enderecos': [
#         {'rua': 'R1', 'numero': 32},
#         {'rua': 'R2', 'numero': 55}
#     ],
#     'altura': 1.8,
#     'numeros_preferidos': (2, 4, 6, 8, 10),
#     'dev': True,
#     'nada': None
# }


# # criando o Json
# with open('aula_191.json', 'w', encoding='utf8') as arquivo:
#     json.dump(pessoa, arquivo, indent=2) # ident, serve para formatar o arquivo JSON


# carregando o arquivo JSON
caminho_arquivo = 'C:\\Users\\Pedro\\Documents\\GitHub\\aula_191.json'
with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa['nome'])


