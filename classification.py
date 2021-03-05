import numpy as np
import pandas as pd
# import function as func

from sklearn.preprocessing import PolynomialFeatures, LabelBinarizer, StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix


# carrega o dataframe
file_name = "complete_dataframe.csv"
df = pd.read_csv(file_name)


# features
features = [ 'number_of_modal_verbs',
            'number_of_singular_first',
            'number_of_plural_first',
            'number_of_pronoums',
            'pausality',
            # 'number_of_characters',
            'average_sentence_length',
            'average_word_length',
            'percentage_of_spelling_erros',
            'emotiveness',
            'diversity',
            'label'
            ]

# subdataframe
sub_df = df[features]

# dataset com as features
X = sub_df[features[:-1]]

# tranforma o label par binário
lb = LabelBinarizer()
y = lb.fit_transform(sub_df['label']).ravel()

# escala as features
scalar = StandardScaler()
scalar.fit(X)
X = scalar.fit_transform(X)

# cross validation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=X_test.shape[0], random_state=0)

# print(X_train.shape, X_test.shape, X_val.shape)

# treina o modelo
model = LogisticRegression()
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
print('F1 score - %0.3f'% f1_score)