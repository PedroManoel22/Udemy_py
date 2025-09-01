# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

from itertools import zip_longest

# Da menor lista para a maior lista

def zipper(cidade, estado):
   
   return list(zip(cidade, estado))


cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']

print(zipper(cidades, estados))

# Da maior lista para a menor 

print(list(zip_longest(cidades, estados)))
print(list(zip_longest(cidades, estados, fillvalue='Sem cidade'))) # fillvalue = onde não tem valor ele troca o valor None para 'Sem cidade'


