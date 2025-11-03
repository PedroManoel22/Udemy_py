# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []
    
    def inserir_enderecos(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))
    
    def __repr__(self):
        # Usamos !r para garantir que 'self.nome' seja representado corretamente como string.
        return f"Cliente(nome={self.nome!r}, enderecos={self.enderecos!r})"
    
    def listar_enderecos(self):
        print(*self.enderecos, sep='\n')
    
    def __del__(self):
        print('Apagando, ', self.nome)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero
    
    def __del__(self):
        print('Apagando, ', self.rua, self.numero)
    
    def __repr__(self):
        return f"Endereço(rua='{self.rua}', numero={self.numero})"

cliente = Cliente('Pedro')
cliente.inserir_enderecos('Av.Brasil', 26)
cliente.inserir_enderecos('Rua1', 36)
cliente.listar_enderecos()

print()
print('Aqui termina meu código')
print()
        