import pandas as pd
import numpy as np

# QUESTAO 1 IMPORTANDO DADOS

print("\n DADOS BRUTOS DO DATASET\n")

df_Belem_2003 = pd.read_csv("datasets/BELEM_2003.CSV", sep=';', decimal=',' , encoding='latin-1') 
df_Belem_2013 = pd.read_csv("datasets/BELEM_2013.CSV", sep=';', decimal=',' , encoding='latin-1') 
df_Belem_2023 = pd.read_csv("datasets/BELEM_2023.CSV", sep=';', decimal=',' , encoding='latin-1') 





# Concatenando os dataframes em um único dataframe
df_concatenado_datetime = pd.concat([df_Belem_2003, df_Belem_2013, df_Belem_2023])

# Convertendo a coluna 'DATA' para o formato datetime
df_concatenado_datetime['DATA'] = pd.to_datetime(df_concatenado_datetime['DATA'] + ' ' + df_concatenado_datetime['HORA'])

# Definindo a coluna 'DATA' como o índice do tipo DateTimeIndex
df_concatenado_datetime.set_index(['DATA'], inplace=True)
df_concatenado_datetime.sort_index(inplace=True)

# Removendo a coluna 'HORA', pois já não é mais necessária
df_concatenado_datetime.drop(columns=['HORA'], inplace=True)

# Visualizando o novo dataframe com DateTimeIndex
print(df_concatenado_datetime)
