import pandas as pd
import numpy as np

import re
import os

import unidecode

import nltk
nltk.download('punkt')
nltk.download('stopwords')

from nltk.corpus import stopwords
from string import punctuation
from nltk import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer as dtk

stopw = stopwords.words('portuguese')

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

preprocessed = "preprocessed"

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
Extrai os dados 'news', 'category', 'data_information','normalized_text', 'preprocessed' e 'label'
"""
def get_content():
    
    aux = os.listdir(fake_meta_inf)
    meta_files = sorted(aux)
    
    aux = os.listdir(fake_folder)
    files = sorted(aux)
    
    news = []
    category = []
    data_inf = []
    normalized_text = []
    preprocessed = []
    label = []
    
    for i, j in zip(meta_files, files):
        
        arq = fake_meta_inf + "/" + i
        text = pd.read_fwf(arq)
        lista = text[text.columns[0]].tolist()
        
        news.append((fake_folder + "/" + j))
        category.append(lista[1])
        data_inf.append(arq)
        normalized_text.append((normalized_fake + "/" + j))
        label.append("fake")
        
        text = preprocessamento((normalized_fake + "/" + j))
        
        # save the text
        file_name = "preprocessed" + "/" + "fake" + "/" + j
        file = open(file_name, "w+")
        file.write(text)
        file.close()
        
        preprocessed.append(file_name)
 
    aux = os.listdir(true_meta_inf)
    meta_files = sorted(aux)
    
    aux = os.listdir(true_folder)
    files = sorted(aux)
    
    for i,  j in zip(meta_files, files):

        arq = true_meta_inf + "/" + i
        text = pd.read_fwf(arq)
        lista = text[text.columns[0]].tolist()

        news.append((true_folder + "/" + j))
        category.append(lista[1])
        data_inf.append(arq)
        normalized_text.append((normalized_true + "/" + j))
        label.append("true")
        
        text = preprocessamento((normalized_fake + "/" + j))
        
        # save the text
        file_name = "preprocessed" + "/" + "true" + "/" + j
        file = open(file_name, "w+")
        file.write(text)
        file.close()
        
        preprocessed.append(file_name)

    return news, category, data_inf, normalized_text, label 
        

def preprocessamento(news):
    
    file = open(news, 'rt')
    text = file.read()
    file.close()

    # lower case the text
    text = text.lower()

    # remove numbers
    number = find_numbers(text)
    for iten in number:
        if iten !="":
            text = text.replace(iten, "0")

    # remove emails 
    email = find_email(text)
    for iten in email:
        if iten != "":
            text = text.replace(iten, "EMAIL")
   
    # remove url   
    url = find_url(text)     
    for iten in url:
        if iten != "":
            text = text.replace(iten, "URL")
    
    # remove punctuation
    for iten in punctuation:
        if iten in text:
            text = text.replace(iten, "") 
    
    text = text.strip()        
         
    # split the words and do the lower case
    words = nltk.word_tokenize(text)
      
    # stopwords from each word    
    stripped = [unidecode.unidecode(word.lower()) for word in words if word.lower() not in stopw]
            
    text = dtk().detokenize(stripped)
   
    return text
    
