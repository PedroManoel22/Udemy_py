from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia: int, num_conta: int, saldo: float, limite_extra = 1000):
        self.agencia = agencia
        self.num_conta = num_conta
        self.saldo = saldo
        self.limite_extra = limite_extra
    
    @abstractmethod
    def sacar(self, valor: int | float):
        ...
    
    def depositar(self, valor: float):
        print(f'\n\033[1;32mFoi depoisitado R${valor}!\033[m\n')
        self.saldo += valor
    
    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f'Desposito de {valor:.2f}')
    
    def detalhes(self,  msg=''):
        print(f'O seu saldo é de {self.saldo:.2f} \033[1;32m{msg}\033[m')