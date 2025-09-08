
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def print_bunito(x):

    for i in x:

        print(i)

    print()
def aumentar_preco(produto):

    return {**produto, 'preco': produto['preco'] + 1}

novos_produtos = list(map(aumentar_preco, produtos))

print_bunito(produtos)

print_bunito(novos_produtos)