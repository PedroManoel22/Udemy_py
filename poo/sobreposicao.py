# super() é a super classe na sub classe
# Classe Principal (Pessoa)
#    -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

# class MinhaString(str):
#     def upper(self):
#         print('chamou o upper')
#         retorno = super().upper()
#         print('depois do upper')
#         return retorno


# string = MinhaString('Oi hehe')
# print(string.upper())


class A:
    atributo_a = 'valor a'
    def __init__(self, atributo):
        self.atributo = atributo
        

    def metodo(self):
        print('A')




class B(A):
    atributo_b = 'valor b'
    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa
    
    def metodo(self):
        print('B')


class C(B):
    atributo_c = 'valor c'

    # def __init__(self, atributo, outra_coisa):
    #     super().__init__(atributo, outra_coisa)

    def __init__(self, *args, **kwargs):
        print('OIIII, estou em c')
        super().__init__(*args, **kwargs)
    
    def metodo(self):
        super().metodo() # B
        # super(B, self).metodo() # A
        # super(A, self).metodo() # object
        print('C')


c = C('atributo_A', 'outra coisa')
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
c.metodo()
print(c.atributo)
print(c.outra_coisa)