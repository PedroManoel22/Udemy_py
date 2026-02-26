from dataclasses import dataclass, field, fields


@dataclass()
class Pesssoa:
    nome: str = field(default="MISSING")
    sobrenome: str = "Not sent"
    idade: int = 0
    enderecos: list[str] = field(
        default_factory=list
    )  # cria um valor padrão para variáveis mutáveis


if __name__ == "__main__":
    p1 = Pesssoa()
    # print(fields(p1)) # meta dados da instância
    print(p1)
