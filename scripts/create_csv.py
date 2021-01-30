"""
This script creates a new .CSV file with data information, the news (fake and true ones), the labels, the normalized texts and the preprocessed texts all togheter in the same dataframe. 

31/01/2021  -   Created the folder scripts and the scritp "create_csv" - @pertum 

@author:pertum    
"""

"""Anterior comments from previous analysis

The files with missing informations about the authors (in the true folder) were corrected manually (Pertum - 09/01/2021)
 
The size_normalized_text "586.txt" doesn´t exist... so, by convienecy, this file was removed from the dataset. Primarlly this was made because a music of Gabriel Pensador it's not a fake news ??? end second because the full_text 586.txt" were incomplete. 
Another reason why "586.txt" was removed it's because this file was 
not normilized with the respective true news (Pertum - 09/01/2021)

The fake file "1607.txt" was removed too. He was removed because it wasb incomplete, incomplete in meta information as well in full text content (Pertum - 09/01/2021)
 
"""
    
import numpy as np
import pandas as pd
import os

###############################################################################
# Folder Project
Fake_Corpus = "Fake.br-Corpus"

# Full Texts Folders
full_texts_folder = Fake_Corpus + "/" +  "full_texts"

fake_folder = full_texts_folder + "/" + "fake"
true_folder = full_texts_folder + "/" + "true"
fake_meta_inf = full_texts_folder + "/" + "fake-meta-information"
true_meta_inf = full_texts_folder + "/" + "true-meta-information"

# Size Normalized Texts Folders
size_normalized_text_folder = Fake_Corpus + "/" + "size_normalized_texts"

normalized_true = size_normalized_text_folder + "/" + "true"
normalized_fake = size_normalized_text_folder + "/" + "fake"
###############################################################################

