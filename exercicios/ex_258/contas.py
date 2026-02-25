from abc import ABC, abstractmethod
from rich import print


class Conta(ABC):
    def __init__(self, agencia: int, num_conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.num_conta = num_conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor: float) -> float: ...

    def depositar(self, valor: float) -> float:
        self.saldo += valor
        self.detalhes(f"Desposito de {valor:.2f}")
        return self.saldo

    def detalhes(self, msg="") -> None:
        print(f"O seu saldo é de {self.saldo:.2f} [green]{msg}[/]")
        print("--")

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f"({self.agencia!r}, {self.num_conta!r}, {self.saldo!r})"
        return f"{class_name} {attrs}"


class ContaPoupanca(Conta):
    def sacar(self, valor: float):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f"(SAQUE {valor})")
            return self.saldo

        print("[red]\nNão foi possível fazer o seu saque![/]\n")
        self.detalhes(f"[red](SAQUE NEGADO {valor})[/]")
        return self.saldo


class ContaCorrente(Conta):
    def __init__(self, agencia, num_conta, saldo=0, limite=0):
        super().__init__(agencia, num_conta, saldo)
        self.limite = limite

    def sacar(self, valor: float):
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f"(SAQUE {valor})")
            return self.saldo

        print("[red]\nNão foi possível fazer o seu saque![/]\n")
        print(f"Seu limite é de {-self.limite:.2f}")
        self.detalhes(f"[red](SAQUE NEGADO {valor})[/]")
        return self.saldo

    def __repr__(self):
        class_name = type(self).__name__
        attrs = (
            f"({self.agencia!r}, {self.num_conta!r}, {self.saldo!r}, "
            f"{self.limite!r})"
        )
        return f"{class_name} {attrs}"


if __name__ == "__main__":
    cp1 = ContaPoupanca(111, 222, 100)
    cp1.sacar(1)
    cp1.depositar(1)
    cp1.sacar(1)
    cp1.sacar(1)
    print("##")
    cc1 = ContaCorrente(111, 222, 0, 100)
    cc1.sacar(1)
    cc1.depositar(1)
    cc1.sacar(1)
    cc1.sacar(1)
    cc1.sacar(98)
    cc1.sacar(1)
    print("##")
