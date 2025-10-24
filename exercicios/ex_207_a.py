# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separado

import json

class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade


pessoa1 = Pessoa('Pedro', 'Manoel', 23)
pessoa2 = Pessoa('Ana', 'lucia', 53)
pessoa3 = Pessoa('João', 'Fernandinho', 16)
pessoas = [pessoa1.__dict__, pessoa2.__dict__, pessoa3.__dict__]

caminho_arquivo = 'exercicios/ex_207_a.json'
# criando JSON
def fazer_dump():
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        print('Estou fazendo o dump')
        json.dump(pessoas, arquivo,ensure_ascii=False, indent=2) # ident, serve para formatar o arquivo JSON

if __name__ == '__main__':
    fazer_dump()