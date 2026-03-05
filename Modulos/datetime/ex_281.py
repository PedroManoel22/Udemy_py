# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime
from dateutil.relativedelta import relativedelta

valor_emprestimo = 1_000_000
anos = 5
fmt = "%d/%m/%Y"
data_emprestimo = datetime(2020, 12, 20)
data_emprestimo_fmt = data_emprestimo.strftime(fmt)
data_final = data_emprestimo + relativedelta(years=anos)
data_final_fmt = data_final.strftime(fmt)
print(f"\nData do empréstimo: {data_emprestimo_fmt}")
print(f"Data final: {data_final_fmt}\n")

meses_total = 5 * 12

valor_parcela = valor_emprestimo / meses_total

for i in range(1, meses_total + 1):
    parcela = data_emprestimo + relativedelta(months=i)
    parcela_fmt = parcela.strftime(fmt)

    print(f"{parcela_fmt} R$ {valor_parcela:.2f}")

print(
    f"\nVocê pegou R${valor_emprestimo:,.2f} para pagar em {anos} anos ({meses_total} meses) em parcelas de R$ {valor_parcela:.2f}\n"
)
