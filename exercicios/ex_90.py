'''import os
lista = []
while True:
    print('Selecione uma opção!')
    opcao = input('[i]nserir [a]pagar [l]istar: ').lower()
    try:
        opcao = str(opcao)
    except:
        print('entrou no except')
        continue
    if opcao in 'ial' and len(opcao) == 1:
        if opcao == 'l' and len(lista) == 0:
            os.system('cls')
            print('nada para listar')
        if opcao == 'l' and len(lista) >= 1:
            os.system('cls')
            for i,v in enumerate(lista):
                print(i,v)
        if opcao == 'i':
            os.system('cls')
            lista.append(input('Valor: '))
        if opcao == 'a':
            os.system('cls')
            apagar = input('Insira o indice do produto que deseja apagar: ')
            try:
                apagar = int(apagar)
            except:
                print('Índice inválido')
            if apagar > len(lista) or apagar < 0:
                print('Este índice não condiz com a lista')
            if apagar <= len(lista) or apagar == 0:
                os.system('cls')
                lista.pop(apagar)
    else:
        print('opção inválida por favor digite uma opção válida!')'''

#--------------------------------------------------------------------------------------------- Codigo do professor 
"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')
    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('clear')
        if len(lista) == 0:
            print('Nada para listar')
        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')
    