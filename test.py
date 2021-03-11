import functions  as func
import pandas as pd 
import numpy as np
from string import punctuation


file_name = "dataset_fakenews_elei__es2018.xlsx"
sheet_name = "Cópia de DB"
data = pd.read_excel(file_name, index_col=0, sheet_name=sheet_name)

data.info()

# exemplo de filtragem por coluna/linha
sub_data = data[data['Único/Repetido'] == 'Único']
sub_data = sub_data[['Agência', 'Link','Matéria', 'Texto da fake']]
del data

sub_data.info()

tagger = func.getNLPNet()

a = sub_data["Texto da fake"][0]
b = func.preprocessamento(a,file=False)

c = tagger.tag(b)[0]
c
d = c.count('N')
d

def count_occ(taggs, sigla):
    count=0
    for tag in taggs:
        if tag[1] == sigla:
            count = count+1
    return count

count_occ(c, 'N')
