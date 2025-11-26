# https://docs.python.org/3/library/exceptions.html

class MyError(Exception):
    ...


class OutroError(Exception):
    ...

def levantar():
    exception_ = MyError('a', 'b', 'c')
    exception_.add_note('Olha a nota 1')
    exception_.add_note('Você errou isso')
    raise exception_

try:
    levantar()
except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args    )
    print()
    exception_ = OutroError('Lançando novamente')
    exception_.add_note('Mais notas')
    raise exception_ from error