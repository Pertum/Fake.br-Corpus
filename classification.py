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

# exemplo de um dataframe com os textos preprocessados e os labels
sub_df = pd.DataFrame([np.transpose(preprocessed), sub_df['label']], func.preprocessed_content)
