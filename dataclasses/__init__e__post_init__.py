from dataclasses import dataclass


# post init
# @dataclass
# class Pesssoa:
#     nome: str
#     sobrenome: str

#     def __post_init__(self):
#         self.nome_completo = f"{self.nome} {self.sobrenome}"

#     # @property
#     # def nome_completo(self):
#     #     return f"{self.nome} {self.sobrenome}"

#     # @nome_completo.setter
#     # def nome_completo(self, valor):
#     #     nome, *sobrenome = valor.split()
#     #     self.nome = nome
#     #     self.sobrenome = " ".join(sobrenome)

# dataclasse com init


@dataclass(init=False)
class Pesssoa:
    nome: str
    sobrenome: str

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nome_completo = f"{self.nome} {self.sobrenome}"

    def __post_init__(self):  # Aqui vemos que o post init não é executado
        print("Pós init")


if __name__ == "__main__":
    p1 = Pesssoa("Luiz", "fernandinho")
    print(p1)
    print(p1.nome_completo)
