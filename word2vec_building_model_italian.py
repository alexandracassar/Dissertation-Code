import os
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import gensim

directory = r"C:/Users/alexa/Documents/3rd Year/Dissertation/Corpora/Subset ITWAC/ITWAC_subset.txt"
data_list = []

with open(directory, "r", encoding="utf8") as f:
    data = f.read()
    # print(data)
    data_list.append(data)

# print(data_list[:2])

sentence_list = []

# tokenizing the data into individual sentences
for text in data_list:
    # print(text)
    sents = sent_tokenize(text)
    sentence_list.append(sents)

# print(sentence_list[:5])

casefold_list = []

# tokenizing the sentences into individual words
for sents in sentence_list:
    # print(sents)
    for sent in sents:
        # print(sent)
        casefold = sent.casefold()
        casefold_list.append(casefold)

# print(casefold_list[:5])

words_list = []

# case-folding the data so that all words are lower-cased
for sent in casefold_list:
    # print(sent)
    words = word_tokenize(sent)
    words_list.append(words)

# print(words_list[:5])

# creating a model using the data
model = gensim.models.Word2Vec(words_list)
# print(model)

# saving the model
model.save("ITWAC_model.csv")
# print(model)
