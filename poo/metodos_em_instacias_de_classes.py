# Método é uma função dentro da classe 
class Carro:
    def __init__(self, nome='sei lá'):
        self.nome = nome # inicializando, método __init__ sempre retorna None


    def acelerar(self):
        print(f'{self.nome} esta acelerando...')

fusca = Carro('Fusca')
print(fusca.nome)

celta = Carro('Celta')
print(celta.nome)
celta.acelerar()