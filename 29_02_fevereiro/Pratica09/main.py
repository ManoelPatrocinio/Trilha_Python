import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# QUESTAO 1 IMPORTANDO DADOS

print("\n DADOS BRUTOS DO DATASET\n")

df_Belem_2003 = pd.read_csv("datasets/BELEM_2003.csv", sep=';', decimal=',' , encoding='latin-1') 
df_Belem_2013 = pd.read_csv("datasets/BELEM_2013.csv", sep=';', decimal=',' , encoding='latin-1') 
df_Belem_2023 = pd.read_csv("datasets/BELEM_2023.csv", sep=';', decimal=',' , encoding='latin-1') 

df_Belem_2003 = df_Belem_2003.where(pd.notna(df_Belem_2003), np.NaN)
df_Belem_2013 = df_Belem_2013.where(pd.notna(df_Belem_2013), np.NaN)
df_Belem_2023 = df_Belem_2023.where(pd.notna(df_Belem_2023), np.NaN)

df_Belem_2003 = df_Belem_2003.replace(-9999.0,np.NaN)
df_Belem_2013 = df_Belem_2013.replace(-9999.0,np.NaN)
df_Belem_2023 = df_Belem_2023.replace(-9999.0,np.NaN)

# Concatenando os dataframes em um único dataframe
df_concatenado_datetime = pd.concat([df_Belem_2003, df_Belem_2013, df_Belem_2023])

# Convertendo a coluna 'DATA (YYYY-MM-DD)' para o formato datetime
df_concatenado_datetime['DATA (YYYY-MM-DD)'] = pd.to_datetime(df_concatenado_datetime['DATA (YYYY-MM-DD)'] + ' ' + df_concatenado_datetime['HORA (UTC)'])

# Definindo a coluna 'DATA (YYYY-MM-DD)' como o índice do tipo DateTimeIndex
df_concatenado_datetime.set_index(['DATA (YYYY-MM-DD)'], inplace=True)
# df_concatenado_datetime.sort_index(inplace=True)

# Removendo a coluna 'HORA (UTC)', pois já não é mais necessária
df_concatenado_datetime.drop(columns=['HORA (UTC)'], inplace=True)

# Visualizando o novo dataframe com DateTimeIndex


# QUESTÃO 1: Analisando os dados e gerando subplot 




# Agrupando os dados por ano e calculando a média das temperaturas e o acumulado de precipitações para cada ano

df_agg = df_concatenado_datetime.groupby(df_concatenado_datetime.index.year).agg({
    'TEMP_AR_BULBO_SECO': 'mean',
    'PRECIPITACAO_TOTAL': 'sum'
})

# Separando os dados por ano
df_2003 = df_agg.loc[2003]
df_2013 = df_agg.loc[2013]
df_2023 = df_agg.loc[2023]

# Criando subplots
fig, axes = plt.subplots(2, 1, figsize=(10, 8))

# Plotando a evolução das temperaturas médias
axes[0].plot(df_2003.index, df_2003['TEMP_AR_BULBO_SECO'], label='2003')
axes[0].plot(df_2013.index, df_2013['TEMP_AR_BULBO_SECO'], label='2013')
axes[0].plot(df_2023.index, df_2023['TEMP_AR_BULBO_SECO'], label='2023')
axes[0].set_title('Evolução das Temperaturas Médias')
axes[0].set_ylabel('Temperatura (°C)')
axes[0].legend()

# Plotando o acumulado de precipitações
axes[1].bar(df_2003.index, df_2003['PRECIPITACAO_TOTAL'], label='2003', alpha=0.7)
axes[1].bar(df_2013.index, df_2013['PRECIPITACAO_TOTAL'], label='2013', alpha=0.7)
axes[1].bar(df_2023.index, df_2023['PRECIPITACAO_TOTAL'], label='2023', alpha=0.7)
axes[1].set_title('Acumulado de Precipitações')
axes[1].set_ylabel('Precipitação (mm)')
axes[1].legend()

plt.tight_layout()
plt.show()

