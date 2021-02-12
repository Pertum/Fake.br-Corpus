import pandas as pd
import numpy as np
import re
import os

###############################################################################
# Folder Project
Fake_Corpus = "Fake.br-Corpus"

# Full Texts Folders
full_texts_folder ="full_texts"

fake_folder = full_texts_folder + "/" + "fake"
true_folder = full_texts_folder + "/" + "true"
fake_meta_inf = full_texts_folder + "/" + "fake-meta-information"
true_meta_inf = full_texts_folder + "/" + "true-meta-information"

# Size Normalized Texts Folders
size_normalized_text_folder = "size_normalized_texts"

normalized_true = size_normalized_text_folder + "/" + "true"
normalized_fake = size_normalized_text_folder + "/" + "fake"
###############################################################################

def find_url(string):
    # findall() has been used  
    # with valid conditions for urls in string 
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)       
    return [x[0] for x in url] 

def find_email(string):
    regex = r"[\w\.-]+@[\w\.-]+"
    email = re.findall(regex,string)       
    return email

def find_numbers(string):

    regex = r"[-+]?\d*\.?\,?\d+|[-+]?\d+"
    number = re.findall(regex,string)

    return number

"""
Extrai o número das notícias, a categoria e as meta information
"""
def get_content():
    
    aux = os.listdir(fake_meta_inf)
    files = sorted(aux)
    
    news = []
    category = []
    data_inf = []
    normalized_text = []
    preprocessed = []
    label = []
    for i in files:
        
        arq = fake_meta_inf + "/" + i
        text = pd.read_fwf(arq)
        lista = text[text.columns[0]].tolist()
        
        news.append((fake_folder + "/" + i))
        category.append(lista[1])
        data_inf.append(arq)
        normalized_text.append((normalized_fake + "/" + i))
        label.append("fake")
        

    aux = os.listdir(true_meta_inf)
    aux = sorted(aux)
    
    for i in aux:

        arq = true_meta_inf + "/" + i
        text = pd.read_fwf(arq)
        lista = text[text.columns[0]].tolist()

        news.append((true_folder + "/" + i))
        category.append(lista[1])
        data_inf.append(arq)
        normalized_text.append((normalized_true + "/" + i))
        label.append("true")

    return news, category, data_inf, normalized_text, label 
        
        
        
        
    
    
            
    
    