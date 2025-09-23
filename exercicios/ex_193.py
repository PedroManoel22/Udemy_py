from os import system

tarefas = []
comandos = ['listar', 'desfazer', 'refazer', 'limpar']
tarefa_2 = []

def listar(tarefas):
    if not tarefas:
        if opcao ==  'listar':
            print('Não a nada para listar')
            print()
            return
    print('TAREFAS:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas):
    if not tarefas:
        print('Não a nada para desfazer')
        print()
        return
    tarefa = tarefas.pop()
    tarefa_2.append(tarefa)
    return tarefa


def refazer(tarefas):
    if not tarefas:
        print('Não a nada para refazer')
        print()
        return
    tarefa = tarefa_2.pop()
    tarefas.append(tarefa)
    return tarefa



while True:
    
    print('Comandos: listar, desfazer, refazer e limpar')
    opcao = input('Digite uma tarefa ou comando: ').lower()
    print()

    if opcao in comandos:
            if opcao ==  'listar':
                listar(tarefas)

            if opcao == 'desfazer':
                desfazer(tarefas)
                listar(tarefas)
                
            if opcao == 'refazer':
                refazer(tarefas)
                listar(tarefas)
               
            if opcao == 'limpar':
                system('cls')

    else:
        tarefas.append(opcao)
        listar(tarefas)
        