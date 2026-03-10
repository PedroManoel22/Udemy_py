# os.listdir para navegar em caminhos
# C:\Users\Pedro\Desktop\exemplo
# caminho = r"C:\\Users\\Pedro\\Desktop\\exemplo"  # para windows

import os

caminho = os.path.join("C:", "\\Users", "Pedro", "Desktop", "exemplo")
# print(caminho)

print()
for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)
    if not os.path.isdir(caminho_completo_pasta):
        continue

    for imagem in os.listdir(caminho_completo_pasta):
        print("  ", imagem)  # mostra o nome do arquivo

print()
