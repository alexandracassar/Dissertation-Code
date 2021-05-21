import os
# import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords

directory = r"C:/Users/alexa/Documents/3rd Year/Dissertation/Corpora/UKWAC"
new_directory = r"C:/Users/alexa/Documents/3rd Year/Dissertation/Corpora/Preprocessed corpus UKWAC"

folders_list = []

# Looping through the subdirectories in the UKWAC corpus
with os.scandir(directory) as dirs:
    for folder in dirs:
        if folder.is_dir():
            folders_list.append(folder)


# Since they are in columns, when it comes to the 2nd column it will stop
stop_words = set(stopwords.words('english'))

# Looping through the files in the UKWAC corpus
for folder in folders_list:
    path = directory + "/" + folder.name
    with os.scandir(path) as files:
        for file in files:
            if file.is_file():
                read_path = path + "/" + file.name
                write_path = new_directory + "/new_" + file.name

                # Reading the original UKWAC files
                with open(read_path, "r", encoding="latin1") as r:
                    # Writing into the new UKWAC files
                    with open(write_path, "w", encoding="utf-8") as w:
                        for line in r:
                            if not line.startswith("<"):
                                lines_list = line.split("\t")
                                if lines_list[0] not in stop_words:
                                    print(lines_list[0], end=" ", file=w)
                            if "</s>" in line:
                                print(end="\n", file=w)
