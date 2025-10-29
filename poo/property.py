# @property - um getter no modo Pythônico
# getter - um método para obter um atribut
# @property é uma propriedade do objeto, ela é um método que se comporta como um atributo
# geralmente é usada nas seguintes situações:
# - Como getter
# - p/ evitar quebra código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código clinte - é o código que usa seu código

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor # antes era "cor" e agora é "cor_tinta"

    
    @property
    def cor(self): # não é um método, é um atributo, O property permite que um método seja acessado como atributo, sem a necessidade de chamarmos como uma função
        return self.cor_tinta


caneta = Caneta('Preta')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)


    