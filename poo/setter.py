class Caneta:
    def __init__(self, cor):
        self._cor = cor
    
    @property
    def cor(self): # aqui se comporta como um atributo e não como um método
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        if valor == 'rosa':
            raise ValueError (f'"{valor}". Essa cor eu não aceito')
        self._cor = valor

        


caneta = Caneta('Azul')
print(caneta.cor)
caneta.cor = 'Rosa'
print(caneta.cor)
