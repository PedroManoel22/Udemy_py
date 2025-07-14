"""
 Faça um programa que peça ao usuário para digitar um número inteiro,
 informe se este número é par ou ímpar. Caso o usuário não digite um número
 inteiro, informe que não é um número inteiro.
"""
num = input('Digite um número inteiro: ')
if num.isdigit():
    num = int(num)
    if num % 2 == 0:
        print(f'O número {num} é par!')
    else:
        print(f'O número {num} é impar!')
else:
    print(f'{num} não é um número inteiro')
"""
 Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
 descrito, exiba a saudação apropriada. Ex. 
 Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
 """
hora = input('Que horas são: ')
hora = int(hora)
bom_dia = hora <= 11 and hora >= 0
boa_tarde = hora >= 12 and hora <= 17
boa_noite = hora >= 18 and hora <= 23
if bom_dia:
    print('Bom dia')
if boa_tarde:
    print('Boa tarde')
if boa_noite:
    print('Boa noite')
"""
 Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
 menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
 "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu primeiro nome: ')
nome_curto = len(nome) <= 4
nome_normal = len(nome) >= 5 and len(nome) <= 6
nome_grande = len(nome) > 6
if nome_curto:
    print('Seu nome é curto!')
if nome_normal:
    print('Seu nome é normal!')
if nome_grande:
    print('Seu nome é muito grande!')
