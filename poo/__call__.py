# Método especial __call__
# callable é algo que pode ser executado em parênteses
# Em classes normais, __call__ faz a instância de uma classe "callable"

class CallMe:
    def __init__(self, phone):
        self.phone = phone
    
    def __call__(self, nome): # faz a instância ser executavel
        print(f'{nome} está Chamando,', self.phone)


call1 = CallMe('12316545612')
call1('Pedro')
        