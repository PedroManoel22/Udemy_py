from functools import partial

def print_inter(lista):

    for i in lista:

        print(i)

    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def aumetar(valor, porcetagem):

    return round(valor * porcetagem, 2)


aumetar_dez = partial(aumetar,porcetagem=1.1)
novos_produtos = [{**p, 'preco': aumetar_dez(p['preco'])} for p in produtos]

print_inter(produtos)
print_inter(novos_produtos)