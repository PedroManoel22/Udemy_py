# Variáveis de ambiente com Python
# Para variáveis de ambiente
# Windows PS: $env:VARIAVEL="VALOR" | dir env:
# Linux e Mac: export NOME_VARIAVEL="VALOR" | echo $VARIAVEL
# Para obter o valor das variáveis de ambiente
# os.getenv ou os.environ['VARIAVEL']
# Para configurar variáveis de ambiente
# os.environ['VARIAVEL'] = 'valor'
# Ou usando python-dotenv e o arquivo .env
# pip install python-dotenv
# from dotenv import load_dotenv
# load_dotenv()
# https://pypi.org/project/python-dotenv/
# OBS.: sempre lembre-se de criar um .env-example

# import os

# from dotenv import load_dotenv

# load_dotenv()  # Por padrão busca o .env na raiz

# # print(os.environ) # vendo todas as variaveis de ambiente

# print(
#     os.getenv("BD_PASSWORD")
# )  # lendo a variavel de ambiente chamada de BD_PASSWORD, que está no .env

a = 7
print(a.__str__())
