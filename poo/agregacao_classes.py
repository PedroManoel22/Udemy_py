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
