import numpy as np
import pandas as pd
import functions as func

# carrega o dataframe
file_name = "dataframe.csv"
df = pd.read_csv(file_name)

# exemplo de filtragem por coluna/linha
aux = df[df['category'] == 'politica']

# sub dataframe da filtragem
sub_df = aux[['preprocessed', 'label']]

# converte os diretórios para texto, aqui foi convertido os textos preprocessados em uma lista  
preprocessed = func.dirs2texts(sub_df['preprocessed'])
labels = sub_df['label'].to_numpy()

#%%
headers = ['preprocessed',
            'label']

# exemplo de um dataframe com os textos preprocessados e os labels
sub_df_01 = pd.DataFrame(np.transpose([preprocessed, labels]), columns = headers)



# ## extrair os metadados e criar um dataframe de exemplo com meta_content

# data_information = func.dirs2information(df['data_information'])
# sub_df_02 = pd.DataFrame(np.transpose([data_information]), columns=func.data_information_content)

# %%
