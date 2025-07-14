import pandas as pd
base_dados = pd.read_csv('dados_sensores.csv')
base_dados = base_dados.drop(['nivel', 'pressao'], axis=1)
print(base_dados)