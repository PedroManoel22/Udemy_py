import time
import random
import pandas as pd

def gerar_dados_sensor(sensor_nome):
    """Simula a leitura de um sensor."""
    if sensor_nome == "temperatura":
        return round(random.uniform(20, 80), 2) # Temperatura entre 20 e 80 graus
    elif sensor_nome == "pressao":
        return round(random.uniform(100, 500), 2) # Pressão entre 100 e 500 kPa
    elif sensor_nome == "vazao":
        return round(random.uniform(0, 10), 2) # Vazão entre 0 e 10 m³/s
    elif sensor_nome == "nivel":
        return round(random.uniform(0, 100), 2) # Nível entre 0 e 100%
    else:
        return None

def coletar_dados(sensores, intervalo=1):
    """Coleta dados dos sensores simulados."""
    dados = {sensor: [] for sensor in sensores}
    timestamps = []
    try:
        while True:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            timestamps.append(timestamp)
            for sensor in sensores:
                valor = gerar_dados_sensor(sensor)
                dados[sensor].append(valor)
            print(f"Dados coletados em {timestamp}:")
            for sensor in sensores:
                print(f"  {sensor}: {dados[sensor][-1]}")
            time.sleep(intervalo)
    except KeyboardInterrupt:
        print("\nColeta de dados interrompida.")
        df = pd.DataFrame(dados, index=timestamps)
        df.index.name = 'Timestamp' 
        return df
sensores_para_monitorar = ["temperatura", "pressao", "vazao", "nivel"]
df_dados = coletar_dados(sensores_para_monitorar, intervalo=0.5) # Coleta a cada 1/2 segundos
if df_dados is not None:
    print("\n--- Dados Coletados Finais (Após Interrupção) ---")
    print(df_dados.head())
    df_dados.to_csv("dados_sensores.csv", index=True) 
    print("Dados salvos em 'dados_sensores.csv' (delimitador: vírgula)")

