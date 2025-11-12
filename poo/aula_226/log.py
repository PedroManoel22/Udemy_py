# Abstração
# Herança - é um
class Log:
    def log(self, msg):
        raise NotImplementedError('Implemente o método log')
    

    def log_error(self, msg):
        return self.log(f'Error: {msg}')


class LogFileMixin(Log):
    def log(self, msg):
        print(msg)


class LogPrintMixin(Log):
    def log(self, msg):
        print(f'{msg} {self.__class__.__name__}')


if __name__ == '__main__':
    l = LogPrintMixin()
    l.log('Qualquer coisa')