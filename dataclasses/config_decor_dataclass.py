from dataclasses import dataclass


@dataclass(order=True)  # "frozen=True" deixa a dataclass congelada
class Pesssoa:
    nome: str
    sobrenome: str


if __name__ == "__main__":
    p1 = Pesssoa("Luiz", "fernandinho")
    print(p1)
