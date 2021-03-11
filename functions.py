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
from nltk.tokenize import RegexpTokenizer

import nlpnet
import string

punctuation = punctuation + "''" + "º" + "ª" +'"' + "°" + '”' 

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

preprocessed_content =[
    'preprocessed',
    'label'   
]

data_information_content = [
                    'author',
                    'link',
                    'category',
                    'date_of_publication',
                    'number_of_tokens',
                    'number_of_word_without_ponctuation',
                    'number_of_types',
                    'number_of_links_inside_the_news',
                    'number_of_words_in_upper_case',
                    'number_of_verbs',
                    'number_of_subjuntive_and_imperative_verbs',
                    'number_of_nouns',
                    'number_of_adjetives',
                    'number_of_adverbs',
                    'number_of_modal_verbs',
                    'number_of_singular_first',
                    'number_of_plural_first',
                    'number_of_pronoums',
                    'pausality',
                    'number_of_characters',
                    'average_sentence_length',
                    'average_word_length',
                    'percentage_of_spelling_erros',
                    'emotiveness',
                    'diversity'
                    ]

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
        
        try:
            file = open(file_name, "r+")
        except:
            file = open(file_name, "w") 
             
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
        
        text = preprocessamento((normalized_true + "/" + j))
        
        # save the text
        file_name = "preprocessed" + "/" + "true" + "/" + j 
        
        try:
            file = open(file_name, "r+")
        except:
            file = open(file_name, 'w') 
        file.write(text)
        file.close()
        
        preprocessed.append(file_name)
           
    return news, category, data_inf, normalized_text, label, preprocessed 
        

def preprocessamento(news, file = True):
    
    # reuso da função
    if file==True:

        arq= open(news, 'rt')
        text = arq.read()
        arq.close()
    else:
        text = news
    
    # lower case the text
    text = text.lower()

    # remove numbers
    number = find_numbers(text)
    for iten in number:
        if iten !="":
            text = text.replace(iten, "")

    # remove emails 
    email = find_email(text)
    for iten in email:
        if iten != "":
            text = text.replace(iten, "")
   
    # remove url   
    url = find_url(text)     
    for iten in url:
        if iten != "":
            text = text.replace(iten, "")

    # tokenize
    words = nltk.word_tokenize(text)
 
    # stopwords from each word and lower case   
    stripped = [unidecode.unidecode(word.lower()) for word in words if word.lower() not in stopw]
            
    text = dtk().detokenize(stripped)
   
    # remove punctuation
    text = text.replace("...", '')
    text = text.replace('”', '')
         
    for iten in punctuation:
        text = text.replace(iten, '')

    return text


def dirs2texts(dirs):
    
    texts = []
    
    for i in dirs:
        file = open(i)
        text = file.read()
        file.close()
        
        texts.append(text)        

    return texts


def dirs2information(dirs):
    
    data=[]
    
    for i in dirs:
        text = pd.read_fwf(i)
        new_row = text[text.columns[0]].tolist()
         
        # insere a informação do autor
        new_row.insert(0,text.columns[0])   

        data.append(new_row)
    
    return data

def getNLPNet():
	tagger = nlpnet.POSTagger('pos-pt', language='pt')
	return tagger

    