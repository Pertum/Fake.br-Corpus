import numpy as np
import pandas as pd
import function as func

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split


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

sub_df = df[features]







