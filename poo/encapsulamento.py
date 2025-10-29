# Public -> pode ser usado em qualquer lugar
# Protected -> Não deve ser usado fora da classe ou suas subclasses
# Private -> Só pode ser usado na classe em que foi declarado, "name mangling (desfiguração de nomes)"
# Note que conseguimos acessar os atributos/métodos privados e protegidos
# mas isso é um convenção, ou seja, viu um '_' é protegido e não se deve usar fora da classe ou subclasses
# viu '__' só usa na propria classe gerada

class SeiLa:
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido' # não é para acessar fora da classe
        self.__private = 'isso é privado'
    

    def metodo_publico(self):
        return 'metodo_publico'


    def _metodo_protected(self): # não é para acessa fora da classe 
        return '_metodo_protected'
    
    def __metodo_private(self):
        return '__metodo_private'


x = SeiLa()
print(x.public)
print(x.metodo_publico())
print(x._protected) # não podemos acessar esta isntância fora da classe
print(x._metodo_protected()) # não podemos acessa este método fora da classe
print(x._SeiLa__metodo_private()) # esse método é só pode ser usado na classe