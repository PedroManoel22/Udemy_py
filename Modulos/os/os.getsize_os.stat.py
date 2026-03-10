# os.path.getsize e os.stat para dados dos arquivos

import math
import os
from itertools import count

caminho = os.path.join("C:", "\\Users", "Pedro", "Desktop", "exemplo")
counter = count()


def formata_tamanho(tamanho_em_bytes: int, base: int = 1024):
    """Formata um tamanho, de bytes para o tamanho apropriado"""

    # Original:
    # https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python

    # Se o tamanho for menor ou igual a 0, 0B.
    if tamanho_em_bytes <= 0:
        return "0B"

    # Tupla com os tamanhos
    #                      0    1     2     3     4     5
    abreviacao_tamanhos = "B", "KB", "MB", "GB", "TB", "PB"

    # Logaritmo -> https://brasilescola.uol.com.br/matematica/logaritmo.htm
    # math.log vai retornar o logaritmo do tamanho_em_bytes
    # com a base (1000 por padrão), isso deve bater
    # com o nosso índice na abreviação dos tamanhos

    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))

    # Por quanto nosso tamanho deve ser dividido para
    # gerar o tamanho correto.

    potencia = base**indice_abreviacao_tamanhos

    # Nosso tamanho final

    tamanho_final = tamanho_em_bytes / potencia

    # A abreviação que queremos

    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]

    return f"{tamanho_final:.2f} {abreviacao_tamanho}"


print()

print()

if __name__ == "__main__":
    print(formata_tamanho(1_000))
    print(formata_tamanho(1_000_000))
    print(formata_tamanho(1_000_000_000))


for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)

    # Pasta atual
    print(the_counter, "pasta_atual: ", root)

    # subdiretórios
    for dir_ in dirs:
        print("  ", the_counter, "Dir: ", dir_)

    # arquivos do diretório atual
    for file in files:
        caminho_completo_arquivo = os.path.join(
            root, file
        )  # caminho completo do arquivo
        # tamanho_arquivo = os.path.getsize(caminho_completo_arquivo) # pegando o tamanho do arquivo
        stats = os.stat(
            caminho_completo_arquivo
        )  # aqui também pegamos o tamanho do arquivo
        tamanho = stats.st_size
        print("  ", the_counter, "File: ", file, formata_tamanho(tamanho))

        # print("    ", the_counter, "File: ", caminho_completo_arquivo)
        # os.unlink(caminho_completo_arquivo)  # tome cuidado, pois aqui vai excluir todos os arquivos, enão tem lixeira
