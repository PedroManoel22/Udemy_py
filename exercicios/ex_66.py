#Calculadora com while
'''while True:
    n1 = int(input('Primeiro Número: '))
    n2 = int(input('Segundo Número: '))
    opcao = str(input('Digite o operador: [+], [-], [*] ou [/]: '))
    if opcao == '+':
            print(f'A soma de {n1} e {n2} = {n1+n2}')
    if opcao == '-':
            print(f'A subtração de {n1} e {n2} = {n1-n2}')
    if opcao == '*':
            print(f'A multiplicação de {n1} e {n2} = {n1*n2}')
    if opcao == '/':
        print(f'A divisão de {n1} e {n2} = {n1/n2}')
    continuar = str(input('Deseja continuar [S], [N]? ')).upper().startswith('N')
    if continuar:
        break
print('Volte sempre!')
'''
while True:
    num1 = input('Digite o primeiro número: ')
    num2 = input('Digite o segundo número: ')
    operador = input('Digite o operador [+], [-], [*], [/]: ')
    numeros_validos = None
    num1_float = 0
    num2_float = 0
    try:
        num1_float = float(num1)
        num2_float = float(num2)
        numeros_validos = True
    except:
        numeros_validos = None
    if numeros_validos is None:
        print('Um ou ambos dos números são inválidos!')
        continue
    operadores_validos = '-+*/'
    if operador not in operadores_validos:
        print('Operador inválido!')
        continue
    if len(operador) > 1:
        print('Digite apenas um operador!')
        continue
    print('Realizando a conta confira abaixo:')
    if operador == '+':
        print(f'{num1_float:.1f} + {num2_float:.1f} = {num1_float+num2_float:.1f}')
    elif operador == '-':
        print(f'{num1_float:.1f} - {num2_float:.1f} = {num1_float-num2_float:.1f}')
    elif operador == '*':
        print(f'{num1_float:.1f} * {num2_float:.1f} = {num1_float*num2_float:.1f}')
    elif operador == '/':
        print(f'{num1_float:.1f} * {num2_float:.1f} = {num1_float*num2_float:.1f}')  
    sair = input('Deseja continuar? [S] ou [N]: ').upper().startswith('N')
    if sair:
        break
print('Volte sempre! :)')
