class MyOpen:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print('Abrindo arquivo...')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8') # Este retorno vai para a variavel "arquivo"
        return self._arquivo

    def __exit__(self, class_exception, expeption_, traceback_):
        print('Fechando arquivo...')
        self._arquivo.close()

        # raise class_exception(*expeption_.args).with_traceback(traceback_) # levanta a mesma mensagem da exceção

        # print(class_exception)
        # print(expeption_)
        # print(traceback_)

        # return True # Tratei o erro, ignorando 
        expeption_.add_note('Minha nota heheh')



with MyOpen('aula149.txt', 'w') as arquivo: # o retorno do  __enter__ vai para esta variável chamada de "arquivo"
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n', 123)
    arquivo.write('Linha 4\n')
    print('WITH', arquivo)