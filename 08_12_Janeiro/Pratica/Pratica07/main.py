import pandas as pd
import numpy as np
from unidecode import unidecode



def processar_nomes_colunas(df):
    # Função para remover acentuação e substituir espaços por underscores em um texto
    def remover_acentuacao_substituir_espacos(texto):
        sem_acentos = unidecode(texto)
        return sem_acentos.replace(' ', '_')

    # Aplica a função para cada coluna do DataFrame
    df.columns = [remover_acentuacao_substituir_espacos(coluna) for coluna in df.columns]


# QUESTAO 1 IMPORTANDO DADOS

df_Belem_2003 = pd.read_csv("datasets/BELEM_2003.CSV", sep=';', decimal=',' , encoding='latin-1') 
df_Belem_2013 = pd.read_csv("datasets/BELEM_2013.CSV", sep=';', decimal=',' , encoding='latin-1') 
df_Belem_2023 = pd.read_csv("datasets/BELEM_2023.CSV", sep=';', decimal=',' , encoding='latin-1') 


# Exibindo os primeiros registros do DataFrame
print("DADOS BELEM 2003 \n")
print(df_Belem_2003.head)

print("\nDADOS BELEM 2013 \n")
print(df_Belem_2013.head)

print("\nDADOS BELEM 2023 \n")
print(df_Belem_2023.info())


# Exercício 2: Juntando os datasets

# print("DADOS NULLS BELEM 2003 \n")

# print(df_Belem_2003.isnull().sum())

# print("\nDADOS NULLS BELEM 2013 \n")
# print(df_Belem_2013.isnull().sum())

# print("\nDADOS NULLS BELEM 2023 \n")
# print(df_Belem_2023.isnull().sum())


df_multIndex =  pd.MultiIndex.from_tuples([()] for data in df_Belem_2003[DATA (YYYY-MM-DD)])

df_combined = pd.concat([df_Belem_2003, df_Belem_2013, df_Belem_2023])


print("\nDADOS DE BELEM COMBINADOS 2003,2013,2023 \n")
print(df_combined.head)

# Exercício 3: Analisando os DataFrame

# 3.1

print("\nCOMPARAÇÃO  DOS DADOS\n")
print("ANÁLISE DE 2003\n")


colunas_para_media = ['PRECIPITAï¿½ï¿½O TOTAL, HORï¿½RIO (mm)', 'TEMPERATURA DO AR - BULBO SECO, HORARIA (ï¿½C)', 'TEMPERATURA DO PONTO DE ORVALHO (ï¿½C)','TEMPERATURA Mï¿½XIMA NA HORA ANT. (AUT) (ï¿½C)','TEMPERATURA Mï¿½NIMA NA HORA ANT. (AUT) (ï¿½C)','TEMPERATURA ORVALHO MAX. NA HORA ANT. (AUT) (ï¿½C)','TEMPERATURA ORVALHO MIN. NA HORA ANT. (AUT) (ï¿½C)']
media_colunas = df_Belem_2003[colunas_para_media].mean()

colunas_para_media = ['PRECIPITAï¿½ï¿½O TOTAL, HORï¿½RIO (mm)', 'TEMPERATURA DO AR - BULBO SECO, HORARIA (ï¿½C)', 'TEMPERATURA DO PONTO DE ORVALHO (ï¿½C)','TEMPERATURA Mï¿½XIMA NA HORA ANT. (AUT) (ï¿½C)','TEMPERATURA Mï¿½NIMA NA HORA ANT. (AUT) (ï¿½C)','TEMPERATURA ORVALHO MAX. NA HORA ANT. (AUT) (ï¿½C)','TEMPERATURA ORVALHO MIN. NA HORA ANT. (AUT) (ï¿½C)']
max_colunas = df_Belem_2003[colunas_para_media].max()

colunas_para_media = ['PRECIPITAï¿½ï¿½O TOTAL, HORï¿½RIO (mm)', 'TEMPERATURA DO AR - BULBO SECO, HORARIA (ï¿½C)', 'TEMPERATURA DO PONTO DE ORVALHO (ï¿½C)','TEMPERATURA Mï¿½XIMA NA HORA ANT. (AUT) (ï¿½C)','TEMPERATURA Mï¿½NIMA NA HORA ANT. (AUT) (ï¿½C)','TEMPERATURA ORVALHO MAX. NA HORA ANT. (AUT) (ï¿½C)','TEMPERATURA ORVALHO MIN. NA HORA ANT. (AUT) (ï¿½C)']
min_colunas = df_Belem_2003[colunas_para_media].min()

dados_2003 = {'Média': media_colunas, 'Valor Max':max_colunas, 'Valor Min':min_colunas}
df_dados_2003 = pd.DataFrame(dados_2003)

print(df_dados_2003)




