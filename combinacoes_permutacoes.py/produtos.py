# geralmente se refere ao produto cartesiano, que é o conjunto de todos os pares ordenados formados por elementos dos conjuntos de dados, 
# ou a um conjunto de itens (ou kit), onde múltiplos produtos são vendidos juntos como uma unidade completa
from itertools import product

def print_iter(iterador):
    
    print(*list(iterador), sep='\n')
    print()


camisas = [
            ['preta', 'branca'],
            ['p', 'm', 'g'],
            ['masculino', 'feminino', 'unissex'],
            ['algodão', 'poliéster']

            ]

print('camisas empacotadas:')
print()
print_iter(product(camisas))
print()

print('camisas desempacotadas:')
print()
print_iter(product(*camisas))