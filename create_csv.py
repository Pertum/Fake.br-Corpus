"""
Este script gera um novo banco de dados .CSV com as:
- data information
- the news (falsas e verdadeiras)
- the labels 
- the normalized texts, and 
- the preprocessed texts 

Tudo no mesmo dataframe.

09-01-2021 
-> Os arquivos de informações que faltavam informações sobre os autores foram corrigidos manualmente. 

-> O texto normalizado "586.txt" não existia, então, por conveniência, ele foi ele foi removido do dataset, bem como as correspondentes noticias falsas e verdadeiras. Primeiramente essa decisão foi tomada por uma música do Gabriel pensador não é uma notícia falsa e segundo, o texto original estava incompleto 

-> O arquivo "586.txt" também foi removido. Este foi removido por estar incompleto tanto no meta information quanto no texto da notícia.

-> Os arquivos/notícias removidas foram separados em uma pasta removed_files.

@author:pertum    
"""
    
import numpy as np
import pandas as pd
import os
import functions as func

metadata_content=[
                    'news', 
                    'category',                         
                    'data_information',
                    'normalized_text',
                    'preprocessed',
                    'label'
                ]

# lista de informações
news, category, data_inf, normalized_text, label = func.get_content()


# dataframe
# df = pd.DataFrame(columns = metadata_content)






