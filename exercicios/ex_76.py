'''
Faça um jogo ao qual o usuário tem que adivinhar a palavra secreta.
Você vai propor a palavra secreta e vai dar a possiblidade do usuário digitar apenas uma letra.
Quando o usuário digitar a letra, você vai conferir se a letra digitada está na palavra secreta.
Se a letra digitada estiver na palavra secreta, exiba a letra.
Se a letra digitada não estiver na palavra secreta exiba *.
Faça a contagem de tentativas do seu usuário.
'''
import os
palavra_secreta = 'teclado'
num_tentativas = 1
letras_acertadas = ''
while True:
    letra_digitada = input('Digite uma letra: ')
    if len(letra_digitada) > 1:
        print('Você digitou mais de uma letra!')
        continue
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
           palavra_formada += '*'
    if palavra_formada == palavra_secreta:
        os.system('cls')
        break
    print(f'Palavra Formada: {palavra_formada}')
    num_tentativas += 1
   
print(f'Parabens você acertou a palavra secreta!\n'
      f'A palavra secreta era {palavra_secreta}\n'
      f'Você aceretou com {num_tentativas} tentativas!')
