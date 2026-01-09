# Conta (ABC)
#     ContaCorrente
#     ContaPoupanca

# Pessoa (ABC)
#     Cliente
#         Clente -> Conta

# Banco
#     Banco -> Cliente
#     Banco -> Conta

# Dicas:
# Criar classe Cliente que herda da classe Pessoa (Herança) ✔️
#     Pessoa tem nome e idade (com getters) ✔️
#     Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
# Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
#     ContaCorrente deve ter um limite extra ✔️
#     Contas têm agência, número da conta e saldo ✔️
#     Contas devem ter método para depósito ✔️
#     Conta (super classe) deve ter o método sacar abstrato (Abstração e
#     polimorfismo - as subclasses que implementam o método sacar)
# Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
# Banco será responsável autenticar o cliente e as contas da seguinte maneira:
#     Banco tem contas e clentes (Agregação)
#     * Checar se a agência é daquele banco
#     * Checar se o cliente é daquele banco
#     * Checar se a conta é daquele banco
# Só será possível sacar se passar na autenticação do banco (descrita acima)
# Banco autentica por um método.

from abc import ABC, abstractmethod
class Conta(ABC):
    @abstractmethod
    def sacar(self, valor):
        ...

class Pessoa(ABC):
    def __init__(self, nome: str, idade: int):
        self._nome = nome
        self._idade = idade
    
    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, valor):
        # valide antes de salvar
        ...
    
    @nome.setter
    def nome(self, valor):
        # valide antes de salvar
        ...


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    

class ContaCorrente(Conta):
    def __init__(self, agencia: int, num_conta: int, saldo: float, limite_extra = 1000):
        super().__init__()
        self.agencia = agencia
        self.num_conta = num_conta
        self.saldo = saldo
        self.limite_extra = limite_extra
    
    def depositar(self, valor: float):
        print(f'\n\033[1;32mFoi depoisitado R${valor}!\033[m\n')
        self.saldo += valor


class ContaPoupanca(Conta):
    def __init__(self, agencia, num_conta, saldo):
        super().__init__()
        self.agencia = agencia
        self.num_conta = num_conta
        self.saldo = saldo

    def depositar(self, valor):
        print(f'\n\033[1;32mFoi depoisitado R${valor}!\033[m\n')
        self.saldo += valor



    

    
    
   


pessoa1 = Pessoa('Pedro', 36)
conta_corrente = ContaCorrente(123456, 123, 1245.25)
print(conta_corrente.agencia)
print(conta_corrente.num_conta)
print(conta_corrente.saldo)
conta_corrente.depositar(2000)
print(conta_corrente.saldo)
conta_corrente.depositar(2000)
print(conta_corrente.saldo)




   

        