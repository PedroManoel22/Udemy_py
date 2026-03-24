# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.

import locale
import string
from datetime import datetime
from pathlib import Path

CAMINHO_ARQUIVO = Path(__file__).parent / "email.txt"

locale.setlocale(locale.LC_ALL, "")  # Deixa o locale no padrão do sistema


def converte_para_brl(numero: float) -> str:
    brl = locale.currency(numero, grouping=True)
    # grouping -> agrupar as casas decimais com '.'
    return brl


data = datetime(2022, 12, 28)
# print(data)

dados = dict(
    nome="João",
    valor=converte_para_brl(1_234_456),
    data=data.strftime("%d/%m/%Y"),
    empresa="O. M.",
    telefone="+55 (11) 7890-5432",
)

# print(json.dumps(dados, indent=2, ensure_ascii=False))
# print(dados)

with open(CAMINHO_ARQUIVO, "r") as file_obj:
    texto = file_obj.read()
    template = string.Template(texto)
    print(template.substitute(dados))
