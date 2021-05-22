import os

directory = r"C:/Users/alexa/Documents/3rd Year/Dissertation/Corpora/Preprocessed corpus MLRS"
data_list = []

# Count of sentences with colour terms in MLRS
count = 0

colours = ["iswed", "abjad", "aħmar", "aħdar", "isfar", "blu", "kannella", "oranġjo", "roża", "vjola", "griż"]

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
        for colour in colours:
            if word == colour:
                count +=1
                break

print(count)