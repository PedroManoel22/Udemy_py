# from log import LogFileMixin, LogPrintMixin

# lp = LogPrintMixin()
# lp.log_error('Qualquer coisa!')
# lp.log_sucess('Que legal!')
# lf = LogFileMixin()
# lf.log_error('Qualquer coisa!')
# lf.log_sucess('Que legal!')


from eletronico import Smartphone

galaxy_S = Smartphone('Galaxy S')
iphone = Smartphone('Iphone')

galaxy_S.ligar()
iphone.desligar()
