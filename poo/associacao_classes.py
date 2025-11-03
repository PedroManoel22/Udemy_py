class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

    @property # se comporta como um atributo 
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta

class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome
    
    def escrever(self):
        return f'{self.nome} está escrevendo'


escritor = Escritor('Pedro')
caneta = FerramentaDeEscrever('caneta')
maquina = FerramentaDeEscrever('Máquina')
escritor.ferramenta = maquina
print(escritor.ferramenta.escrever())
print(caneta.escrever())
print(f'{escritor.nome} está escrevendo com {escritor.ferramenta.escrever()}')

