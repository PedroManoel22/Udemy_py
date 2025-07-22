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
for i in perguntas:
    while True:
      os.system('cls')
      print(i['Pergunta'])
      print(i['Opções'])
      resposta_usuario = input('Insira sua resposta aqui: ')
      if resposta_usuario == i['Resposta']:
            print('Parabéns você acertou!')
            sleep(1)
            break
      elif resposta_usuario not in i['Opções']:
            print('Por favor coloque uma das opções que lhe mostrei ')
            print('Tente Novamente....')
            sleep(3)
      else:
            print('Você erroou!')
            print('Tente Novamente....')
            sleep(1)
            continue
print('Obbrigado e volte sempre!')
