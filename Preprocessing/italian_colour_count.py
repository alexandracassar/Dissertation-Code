import os

directory = r"C:/Users/alexa/Documents/3rd Year/Dissertation/Corpora/Preprocessed corpus ITWAC"
new_directory = r"C:/Users/alexa/Documents/3rd Year/Dissertation/Corpora/Colour Sentences ITWAC/ITWAC_subset.txt"
data_list = []
list_of_colour_sents = []
list_of_sents = []

# Count of sentences with colour terms in ITWAC
count = 0
# Count of sentences without colour terms in ITWAC
count2 = 0

colours = ["nero", "nera", "neri", "nere",
           "bianco", "bianca", "bianchi", "bianche",
           "rosso", "rossa", "rossi",  "rosse",
           "verde", "verdi",
           "giallo", "gialla", "gialli", "gialle",
           "blu",
           "marrone", "marroni" 
           "arancione",
           "rosa",
           "viola",
           "grigio", "grigia", "grigie", "grigi"]

for file in os.listdir(directory):
    path = directory + "/" + file
    with open(path, "r", encoding="utf-8") as f:
        data = f.read()
        sentences = data.split("\n")
        for line in sentences:
            data_list.append(line.strip())

# Loops through the corpus and counts how many colour terms there are
for sentence in data_list:
    split_sentence = sentence.split(" ")
    for word in split_sentence:
        if word in colours:
            if count != 43000:
                count += 1
                list_of_colour_sents.append(sentence)
            break

# Loops through the corpus and counts how many colour terms there are
for sentence in data_list:
    split_sentence = sentence.split(" ")
    for word in split_sentence:
        if word not in colours:
            if count2 != 207000:
                count2 += 1
                list_of_sents.append(sentence)
            break

# Writing the sentences including colour terms to the text file
with open(new_directory, "w", encoding="utf-8") as w:
    for line in list_of_colour_sents:
        w.write(line)
        w.write("\n")
# Writing the sentences not including colour terms to the text file
    for line in list_of_sents:
        w.write(line)
        w.write("\n")
w.close()