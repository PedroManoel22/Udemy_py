from itertools import combinations, permutations

pessoas = ['Pedro', 'Isabel', 'Ana', 'Antonio', 'Kiara']    

print('Combinação:')
print(*list(combinations(pessoas, 2)), sep='\n') # Cobinar itens de um iterador, onde a ordem não importa. 'pessoas' é o iterador, e '2' é o grupo de combinações 
print()

print('Permutação:')
print(*list(permutations(pessoas, 2)), sep='\n') # Permutar itens de um iterador, onde a ordem importa. 'pessoas' é o iterador, e '2' é o grupo de permutações

print()

# função para combinar e permutar os itens de um iterador

def print_iter(iterador):

    print(*list(iterador), sep='\n')
    print()

print('Combinação com função:')
print_iter(combinations(pessoas, 3))
print('Permutação com função:')
print_iter(permutations(pessoas, 3))