import contas, pessoas


class Banco:
    def __init__(
        self,
        agencias: list[int] | None = None,
        clientes: list[pessoas.Pessoa] | None = None,
        contas: list[contas.Conta] | None = None,
    ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _chega_agencia(self, conta):
        if conta.agencia in self.agencias:
            return True
        return False

    def _chega_cliente(self, cliente):
        if cliente in self.clientes:
            return True
        return False

    def _chega_conta(self, conta):
        if conta in self.contas:
            return True
        return False

    def _checa_se_conta_e_do_cliente(self, conta, cliente):
        if conta is cliente.conta:
            return True
        return False

    def autenticar(self, cliente: pessoas.Pessoa, conta: contas.Conta):
        return (
            self._chega_agencia(conta)
            and self._chega_cliente(cliente)
            and self._chega_conta(conta)
            and self._checa_se_conta_e_do_cliente(conta, cliente)
        )

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f"({self.agencias!r}, {self.clientes!r}, {self.contas!r})"
        return f"{class_name} {attrs}"


if __name__ == "__main__":
    import contas

    c1 = pessoas.Cliente("Luiz", 30)
    cc1 = contas.ContaCorrente(111, 222, 0, 0)
    c1.conta = cc1
    c2 = pessoas.Cliente("Pedro", 28)
    cp1 = contas.ContaPoupanca(333, 666, 10)
    c2.conta = cp1
    banco = Banco()
    banco.clientes.extend([c1, c2])
    banco.contas.extend([cc1, cp1])
    banco.agencias.extend([111, 222])

    if banco.autenticar(c1, cc1):
        cc1.depositar(10)
        print(c1.conta)
