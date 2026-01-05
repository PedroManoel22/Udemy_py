# Em Python tudo é objeto (classes também)
# O tipo de uma classe é type
# Seu objeto é uma instância de sua classe
# Sua classe é uma instância de type (type é uma metaclass)
# type('name', (Bases,), __dict__) -> bases são as heranças

# class Oi:     é igual a -> Oi = type('Oi', (object,), {})
#     ...

Oi = type('Oi', (object,), {})

# Ao criar uma classe, por padrão as coisas acontecem nesssa ordem:
# __new__ da metaclass é chamado e cria a nova classe
# __call__ da metaclasse é chamado com os argumentos e chama:
#   __new__ da classe com os argumentos (cria a instância)
#   __init__ da classe com os argumentos
# __call__ da metaclass termina a execução

# métodos importantes da metaclass
# __new__ (mcs, name, bases, dict) -> (cria a classe)
# __call__(cls, *args, **kwargs) -> (cria e inicializa a instância)

'''teste = Oi()
print(isinstance(teste, Oi))
print(isinstance(Oi, object))
print(type(teste))
print(type(Oi))
'''
# mexendo com metaclasse

class Meta(type):
    def __new__ (mcs, name, bases, dict): # posso executar coisas antes da criação da classe 
        print('Metaclass new')
        cls = super().__new__(mcs, name, bases, dict)
        cls.attr = 123
        # print(cls.__dict__)

        if 'falar' not in cls.__dict__ or not callable(cls.__dict__['falar']):
            raise NotImplementedError('Implemente falar')
        
        return cls
    

    def __call__(cls, *args, **kwargs):
        instancia = super().__call__(*args, **kwargs)

        if 'nome' not in instancia.__dict__ :
                raise NotImplementedError('Crie o atributo nome')
        
        return instancia
    

class Pessoa(metaclass=Meta):

    def __new__(cls, *args, **kwargs): 
        print('Meu new')
        instancia = super().__new__(cls) 
        return instancia

    def __init__(self, nome):
        print('Meu init')
        # self.nome = nome
    
    def falar(self):
        print('falando....')


p1 = Pessoa('Jorginho')
print(p1.attr)
print(Pessoa.attr)

