# Mapeamento

# def dividir(x,y):
#     return x / y


# lista = [1, 2, 3, 7, 8]
# divisao = [dividir(numero, 2) for numero in lista]
# print(lista)
# print(divisao)
 
nomes = ['luiz', 'leandro', 'maria', 'pedro']
ultimo_maiusculo = [f'{nome[0:-1].lower()}{nome[-1].upper()}'
                    for nome in nomes
]
print(ultimo_maiusculo)