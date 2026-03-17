# os + shutil - Copiando arquivos com Python
# 1 - Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
import os
import shutil

HOME = os.path.expanduser("~")  # pegando a home do usuário
DESKTOP = os.path.join(HOME, "Desktop")
PASTA_ORIGINAL = os.path.join(DESKTOP, "exemplo")
NOVA_PASTA = os.path.join(DESKTOP, "Nova_pasta")

print(NOVA_PASTA)

os.makedirs(
    NOVA_PASTA, exist_ok=True
)  # cria a pasta, exist_ok=True -> só cria a pasta se ela não existir

for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir_ in dirs:
        caminho_novo_diretorio = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
        )

        print(caminho_novo_diretorio)
        os.makedirs(
            caminho_novo_diretorio, exist_ok=True
        )  # cria a pasta, exist_ok=True -> só cria a pasta se ela não existir

    for file in files:
        caminho_arquivo = os.path.join(root, file)
        caminho_novo_arquivo = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), file
        )
        shutil.copy(caminho_arquivo, caminho_novo_arquivo)
