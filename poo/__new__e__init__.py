# __new__ cria o objeto e retorna o novo objeto, por isso recebe cls.
# __init__ inicializa a instância, por isso recebe self, __init__ não retorna nada (None)
# object é a super classe de uma classe, isso quer dizer que minha classe herda de object
# Como por exemplo abaixo: class A(object)

class A:
    def __new__(cls, *args, **kwargs):
        instancia = super().__new__(cls)
        return instancia

    def __init__(self, x):
        self.x = x
        print('Sou o init')

    def __repr__(self):
        return 'A()'


a = A(123)
print(a.x)