# Dissertation-Code

Code files:

preprocessing_files_english.py, preprocessing_files_maltese.py, preprocessing_files_italian.py: 
Changing the corpora's format to give us only the words in the corpus since they are in columns. 

english_colour_count.py, italian_colour_count.py, maltese_colour_count.py: 
Counts how many sentences have colour terms till they reach 43,000 and 203,000 sentences without colour terms. The amounts used were in order to match the numbers of the Maltese (MLRS) corpus. This was done for the Italian (ITWAC) and the English (UKWAC) corpus in order to create a subset for them.

word2vec_building_model.py: 
Reads in the newly created corpora files and performs sentence tokenization, case-folding and word tokenization on the data. Then a Word2Vec model for each corpus is created and saved into a .csv file.

mlrs_similiarities.py, ukwac_similiarities.py, itwac_similiarities.py: 
Reads in the model and creates the top 50 most similar words to the colour terms.

mlrs_analogy.py, ukwac_analogy.py, itwac_analogy.py: 
Reads in the model and creates the top 20 most similar words in analogies using colour terms and emotion words.
