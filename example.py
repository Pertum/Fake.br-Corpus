import numpy as np
import pandas as pd
import functions as func

# carrega o dataframe
file_name = "dataframe.csv"
df = pd.read_csv(file_name)

#### Exemplos de uso do Dataframe ###


## Parte 01

# exemplo de filtragem por coluna/linha
aux = df[df['category'] == 'politica']

# sub dataframe da filtragem
sub_df = aux[['preprocessed', 'label']]

# converte o arquivo dos diretórios para texto, dirs2texts retorna uma lista com os textos  
preprocessed = func.dirs2texts(sub_df['preprocessed'])

# exemplo de um dataframe com os textos preprocessados e os labels
labels = sub_df['label'].to_numpy()
sub_df_01 = pd.DataFrame(np.transpose([preprocessed, labels]), columns = ['preprocessed','label'])


## PArte 02

# Exemplo de como extrair os meta-information e gerar um novo dataframe com eles
# extrair os metadados e criar um dataframe de exemplo com meta_content
data_information = func.dirs2information(df['data_information'])
sub_df_02 = pd.DataFrame(data_information, columns=func.data_information_content)


## Parte 03

# Exemplo de concatenação de dataframes
# converte os diretórios para texto, aqui foi convertido os textos preprocessados em uma lista  
preprocessed = func.dirs2texts(df['preprocessed'])
labels = df['label'].to_numpy()

# exemplo de um dataframe com os textos preprocessados e os labels
sub_df_03 = pd.DataFrame(np.transpose([preprocessed, labels]), columns = ['preprocessed','label'])

# por fim, a concatenação
complete_df = pd.concat([sub_df_02, sub_df_03], axis=1)

complete_df.info()

# save a csv file
complete_df.to_csv(r'complete_dataframe.csv', index=True, header=True)

# %%
