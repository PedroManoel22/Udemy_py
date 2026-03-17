# Copiar -> shutil.copy
# Copiar árvore recursivamente -> shutil.copytree
# Apagar árvore recursivamente -> shutil.rmtree
# Apagar arquivos -> os.unlink
# Renomear/Mover -> shutil.move ou os.rename

import os
import shutil

HOME = os.path.expanduser("~")  # pegando a home do usuário
DESKTOP = os.path.join(HOME, "Desktop")
PASTA_ORIGINAL = os.path.join(DESKTOP, "exemplo")
NOVA_PASTA = os.path.join(DESKTOP, "Nova_pasta")

# apagando a pasta de forma recursiva
# shutil.rmtree(NOVA_PASTA)

# toma cuidado a excluir coisas com python, pois não vai para a lixeira do computador

# copiando pastas de um jeito mais fácil heheh
# shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)

# Renomeando ou movendo pasta

shutil.move(NOVA_PASTA, "HEHEH")
