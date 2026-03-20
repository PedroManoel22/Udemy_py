# Usamos a pathlib para trabalhar com caminho, pastas e arquivos de forma que um código
# funcione em Windows, Linux e Mac.

from pathlib import Path
from shutil import rmtree

print()
pasta = Path()
print(pasta.absolute())

print()
pasta = Path(__file__)
print(pasta)

print()
pasta = Path(__file__).parent
print(pasta)

print()

ideias = pasta / "ideias.txt"
print(ideias)

print()

caminho_arquivo = Path.home() / "Desktop" / "arquivo.txt"


# arquivo.touch()  # -> criando o arquivo
# print(arquivo)


# arquivo.write_text("Olá, mundo!")
# print(arquivo.read_text())

# caminho_arquivo.unlink()  # -> excluindo o arquivo

# with open(caminho_arquivo, "+a") as file:
#     file.write("Uma linha\n")
#     file.write("Outra linha\n")

# print(caminho_arquivo.read_text())


# Criando pasta
caminho_pasta = Path.home() / "Desktop" / "python_e_legal"

caminho_pasta.mkdir(exist_ok=True)  # Se existir a pasta ele não faz nada

subpasta = caminho_pasta / "subpasta"

subpasta.mkdir(exist_ok=True)

outro_arquivo = subpasta / "arquivo.txt"
outro_arquivo.touch()
outro_arquivo.write_text("OI")

mais_arquivo = caminho_pasta / "arquivo.txt"
mais_arquivo.touch()
mais_arquivo.write_text("Olá tudo bem ?")


# Apagando pasta
# caminho_pasta.rmdir()  # -> A pasta tem que está vazia para que der certo ( tem que ser de forma recursiva )

files = caminho_pasta / "files"
files.mkdir(exist_ok=True)

for i in range(10):
    file = files / f"file_{i}.txt"

    if file.exists():
        file.unlink()

    else:
        file.touch()

    with file.open("+a") as text_file:
        text_file.write("Olá mundo\n")
        text_file.write(f"file_{i}.txt")


# entrando na pasta e excluindo

rmtree(caminho_pasta)
