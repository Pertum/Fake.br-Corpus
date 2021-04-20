import functions  as func
import pandas as pd 
from lexical_diversity import lex_div as ld


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

text = "katia abreu diz vai colocar expulsao moldura nao reclamar senadora katia abreu disse expulsao pmdb resultado acao cupula atual legenda segundo oportunista amanha vou botar moldura dourada expulsao porque maos onde veio atestado boa conduta curriculo pessoas expulsaram nao servem pais servem pais beneficios proprios disse katia abreu ue expulsao algo tao bom curriculo tanta choradeira katia sabemos motivo provavelmente katia nao valor pt partido ja deveria absorvido parece pt gostava katia somente ficasse entrincheirada dentro pmdb rebaixar demais resta katia ficar chorando pitangas todos cantos tempo ate momento pt nao cadastrou katia abreu fileiras situacao patetica agricultura dilma"
text_01 = "katia abreu diz vai colocar expulsao moldura reclamar  senadora katia abreu partidoto disse expulsao pmdb resultado acao cupula atual legenda segundo oportunista   amanha vou botar moldura dourada expulsao porque maos onde veio atestado boa conduta curriculo  pessoas expulsaram servem pais  servem pais beneficios proprios  disse katia abreu  ue expulsao algo tao bom curriculo tanta choradeira katia sabemos motivo  provavelmente katia valor pt partido deveria tela absorvido  parece pt gostava katia somente ficasse entrincheirada dentro pmdb  rebaixar demais  resta"
text_02 = "katia abreu diz vai colocar expulsao moldura nao reclamar senadora katia abreu disse expulsao pmdb resultado acao cupula atual legenda segundo oportunista amanha vou botar moldura dourada expulsao porque maos onde veio atestado boa conduta curriculo pessoas expulsaram nao servem pais servem pais beneficios proprios disse katia abreu ue expulsao algo tao bom curriculo tanta choradeira katia sabemos motivo provavelmente katia nao valor pt partido ja deveria absorvido parece pt gostava katia somente ficasse entrincheirada dentro pmdb rebaixar demais resta katia ficar chorando pitangas todos cantos tempo ate momento pt nao cadastrou katia abreu fileiras situacao patetica agricultura dilma"


diversity = ld.ttr(ld.flemmatize(text))
diversity

#%%

doc = nlp(b)

for i, word in enumerate(doc):
    # print(word.text, word.pos_,  word.lemma_, word.dep_)
    print("\n")
    print(word.text, "->", word.lemma_)
    print(word.dep_, "->", spacy.explain(word.dep_))    
    print(word.pos_, "->", spacy.explain(word.pos_))

    # if i>20:
    #     break
#%%

import functions as func
import spacy

#%%
def lexical_features(news, file=False):
    
    nlp = spacy.load("pt_core_news_lg")

    if file==True:
        arq= open(news, 'rt')
        text = arq.read()
        arq.close()
    else:
        text = news
    
    text = nlp(text)
    
    # print(text)

    return text

news = func.fake_folder + "/2750.txt"

text = lexical_features(news, True)






#%%
import pandas as pd
import functions as func
import numpy as np
from sklearn.preprocessing import PolynomialFeatures, LabelBinarizer, StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix



file_name = "complete_dataframe.csv"

data = pd.read_csv(file_name)
sub_data = data[data['category'] == 'politica']

# preprocessed = sub_data['preprocessed']
preprocessed = data['preprocessed']

diversity = func.pandas2diversity(preprocessed)
diversity = np.array(diversity)
X = diversity.reshape(-1,1)
X.shape


# tranforma o label par binário
l2b = LabelBinarizer()
# y = l2b.fit_transform(sub_data['label']).ravel()
y = l2b.fit_transform(data['label']).ravel()


# # escala as features
# scalar = StandardScaler()
# scalar.fit(X)
# X = scalar.fit_transform(X)



# cross validation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=X_test.shape[0], random_state=0)

# print(X_train.shape, X_test.shape, X_val.shape)

# treina o modelo
model = LogisticRegression(penalty='none')
model.fit(X_train,y_train)

# predições
y_predict = model.predict(X)
y_test_predict= model.predict(X_test)
y_val_predict=model.predict(X_val)
y_test_predict = model.predict(X_test)

# acurácias
acc_train = accuracy_score(y_test, y_test_predict)
acc_val = accuracy_score(y_val, y_val_predict)
acc_test = accuracy_score(y_test, y_test_predict)

print(acc_train, acc_val, acc_test)

# métricas
tn, fp, fn, tp = confusion_matrix(y_test, y_test_predict).ravel()

lbr = (fp/(tp+fp))
fcr = (tp/(tp+fn))
fpr = (tp/(tp+fp))
f1_score = 2*(fpr*fcr)/(fpr+fcr)

print('LBR - %0.3f'% lbr)
print('FCR - %0.3f'% fcr)
print('FPR - %0.3f'% fpr)
print('F1  - %0.3f'% f1_score)

