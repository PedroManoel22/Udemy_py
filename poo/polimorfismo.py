# Polimorfismo -> é o princípio que permite que classes derivadas de uma mesma
# superclasse tenham métodos iguais (com mesma assinatura) mas com comportamentos diferentes
# Princípios SOLID -> L = Liskov Substitution Principle:
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma classe sem quebrar a aplicação

from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, msg):
        self.msg = msg
    
    @abstractmethod
    def enviar(self) -> bool:
        ...

class NotificacaoEmail(Notificacao):
    def enviar(self):
        print('Email: enviando - ', self.msg)
        return True

class NotificacaoSMS(Notificacao):
    def enviar(self):
        print('SMS: enviando - ', self.msg)
        return False


# n = NotificacaoEmail('Testando')
# n.enviar()

def notificar(notificacao: Notificacao):
    notificacao_enviada =   notificacao.enviar()

    if notificacao_enviada:
        print('Notificação enviada')
    
    else:
        print('Notificação não enviada')

notificacao_email = NotificacaoEmail('Testando email')
notificar(notificacao_email)

notificacao_sms = NotificacaoSMS('Testando sms')
notificar(notificacao_sms)
        