import re
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