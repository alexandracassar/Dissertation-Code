import os
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import gensim

directory = r"C:/Users/alexa/Documents/3rd Year/Dissertation/Corpora/Preprocessed corpus MLRS"
data_list = []

# Reading the newly created files
for file in os.listdir(directory):
    path = directory + "/" + file
    with open(path, "r", encoding="utf-8") as f:
        data = f.read()
        data_list.append(data)

sentence_list = []

# Tokenizing the data into individual sentences
for text in data_list:
    sents = sent_tokenize(text)
    sentence_list.append(sents)

casefold_list = []

# Tokenizing the sentences into individual words
for sents in sentence_list:
    for sent in sents:
        casefold = sent.casefold()
        casefold_list.append(casefold)

words_list = []

# Case folding the data so that all words are lower-cased
for sent in casefold_list:
    words = word_tokenize(sent)
    words_list.append(words)

# Creating a model using the data
model = gensim.models.Word2Vec(words_list)

# Saving the model
model.save("MLRS_model.csv")
