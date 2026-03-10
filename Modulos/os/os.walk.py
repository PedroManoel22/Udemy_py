# os.walk para navegar de caminhos de forma recursiva, entra em todas as pastas
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
import os
from itertools import count

caminho = os.path.join("C:", "\\Users", "Pedro", "Desktop", "exemplo")
counter = count()

print()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)

    # Pasta atual
    print(the_counter, "pasta_atual: ", root)

    # subdiretórios
    for dir_ in dirs:
        print("  ", the_counter, "Dir: ", dir_)

    # arquivos do diretório atual
    for file in files:
        print("  ", the_counter, "File: ", file)
        # caminho_completo_arquivo = os.path.join(root, file)  # caminho completo do arquivo
        # print("    ", the_counter, "File: ", caminho_completo_arquivo)
        # os.unlink(caminho_completo_arquivo)  # tome cuidado, pois aqui vai excluir todos os arquivos, enão tem lixeira

print()
