from os import system

# fazer uma função para cada comando

tarefas = []
comandos = ['listar', 'desfazer', 'refazer', 'limpar']
tarefa_2 = []

def listar(tarefas):
    if not tarefas:
        if opcao ==  'listar':
            print('Não a nada para listar')
            return
    print('TAREFAS:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()
    
        


while True:
    
    print('Comandos: listar, desfazer, refazer e limpar')
    opcao = input('Digite uma tarefa ou comando: ').lower()
    print()

    if opcao in comandos:
        if not tarefas:
            if opcao == 'desfazer':
                print('Não a nada para desfazer')
            
            if opcao == 'refazer':
                print('Não a nada para refazer')
        else:
            if opcao ==  'listar':
                listar(tarefas)

            if opcao == 'desfazer':
                tarefa = tarefas.pop()
                tarefa_2.append(tarefa)
            
            if opcao == 'refazer':
                tarefa = tarefa_2.pop()
                tarefas.append(tarefa)

            if opcao == 'limpar':
                system('cls')

    else:
        tarefas.append(opcao)
        

        print('TAREFAS:')
        