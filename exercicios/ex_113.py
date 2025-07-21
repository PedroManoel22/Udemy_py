# Crie uma função que multiplica todos os argumentos não nomeados recebidos
# Retorne o total para uma variável e mostre o valor da variável


def multiplica(*args):
    total = 1
    for n in args:
        total *=  n
    return total
resultado = multiplica(1, 2, 3, 4, 5)
print(resultado)
resultado = multiplica(2, 3, 7, 8)
print(resultado)


# Crie uma função que fala se um número é par ou ímpar.
# Retorne se o valor é par ou ímpar


def par_impar(x):
    if x % 2 == 0:
        return f'O número {x} é par!'
    return f'O numero {x} é ímpar!'
resultado = par_impar(9)
print(resultado)


#Aqui é o mesmo exercício de par ou impar mas com vários argumentos não nomeados

def par_impar(*x):
    for n in x:
        if n % 2 == 0:
            print(f'O número {n} é par!') 
        else:
            print(f'O número {n} é ímpar!')
par_impar(36, 10, 1, 12, 17, 24, 18, 19)
