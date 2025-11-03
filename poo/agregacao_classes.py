# Relações entre classes: associação, agregação e composição
# Associação é um tipo de relação onde os objetos
# estão ligados dentro do sistema.
# Essa é a relação mais comum entre objetos e tem subconjuntos
# como agregação e composição (que veremos depois).
# Geralmente, temos uma associação quando um objeto tem
# um atributo que referencia outro objeto.
# A associação não especifica como um objeto controla
# o ciclo de vida de outro objeto.
# Carrinho de compras agrega produtos
class CarrinhoDeCompras:
    def __init__(self):
        self._produtos = []
    
    def total(self):
        return sum([p.preco  for p in self._produtos])

    def inserir(self, *produtos):
       #self._produtos.extend(produtos)
       self._produtos += produtos

    def listar(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

carrinho = CarrinhoDeCompras()
p1, p2 = Produto('Caneta', 1.5), Produto('Camisa', 50)
carrinho.inserir(p1, p2)
carrinho.listar()
print(carrinho.total())
