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
from dados import produtos

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)} for p in deepcopy(produtos) # não é necessário este deepcopy
    ]
print('Lista original:')
print(*produtos, sep='\n')
print()
print('Preços com 10% de aumento:')
print(*novos_produtos, sep='\n')

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

print()
print('Produtos ordenados por nome, (do maior para o menor):')
produtos_ordenados_por_nome = sorted(deepcopy(produtos), key= lambda p : p['nome'], reverse=True)
print(*produtos_ordenados_por_nome, sep='\n')


# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

print()
print('Produtos ordenados por nome, (do menor para o maior):')
produtos_ordenados_por_nome = sorted(deepcopy(produtos), key= lambda p : p['nome'])
print(*produtos_ordenados_por_nome, sep='\n')


