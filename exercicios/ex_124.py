from time import sleep
import os
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
] 
total_acertadas = 0
for itens in perguntas:
    total_respostas = len(itens)
    os.system('cls')
    print(itens['Pergunta'])
    if itens['Opções']:
        for i in range(len(itens['Opções'])):
            if itens['Opções'][i] == itens['Resposta']:
                 indice_resposta_correta = i
            print(f'{i}) {itens['Opções'][i]}')
    resposta_usuario = int(input('Insira a opção correta aqui: '))
    if resposta_usuario == indice_resposta_correta:
        print('Parabéns você acertou!')
        total_acertadas += 1
        sleep(1)
    else:
        print('Você erroou!')
        print('Vamos para a proxima pergunta....')
        sleep(1)
print(f'Fim do jogo você acertou {total_acertadas} perguntas de {total_respostas}')
print('Obrigado e volte sempre!')
