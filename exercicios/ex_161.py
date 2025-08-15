# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

"""
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.10}
    for produto in produtos
]

print("Lista original (sem alteração):")
print(produtos)

print("\nLista de novos produtos (com preços aumentados):")
print(novos_produtos)
"""

# agora com deepcopy

from copy import deepcopy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


novos_produtos = deepcopy(produtos)

for produto in novos_produtos:
    produto['preco'] += produto['preco'] * 0.10

print("Lista original (sem alteração):")
print(produtos)

print("\nLista de novos produtos (com preços aumentados):")
print(novos_produtos)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_nome = deepcopy(novos_produtos)
for k, v in enumerate(produtos_ordenados_por_nome):
    print(k, v)

print('Produtos ordenados por nome:', produtos_ordenados_por_nome)
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)