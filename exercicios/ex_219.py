# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor
    
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


# carro 1
carro1 = Carro('Celta')
chevrolet = Fabricante('Chevrolet')
motor1 = Motor('1.0')
carro1.fabricante = chevrolet
carro1.motor = motor1
print(carro1.nome, carro1.fabricante.nome, carro1.motor.nome)

# carro 2
carro2 = Carro('Uno')
fiat = Fabricante('Fiat')
motor2 = Motor('1.4')
carro2.fabricante = fiat
carro2.motor = motor2
print(carro2.nome, carro2.fabricante.nome, carro2.motor.nome)
