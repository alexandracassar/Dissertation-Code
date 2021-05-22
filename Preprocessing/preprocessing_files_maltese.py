import os

directory = r"C:/Users/alexa/Documents/3rd Year/Dissertation/Corpora/MLRS"
new_directory = r"C:/Users/alexa/Documents/3rd Year/Dissertation/Corpora/Preprocessed corpus MLRS"

folders_list = []

# Looping through the subdirectories in the MLRS corpus
with os.scandir(directory) as dirs:
    for folder in dirs:
        if folder.is_dir():
            folders_list.append(folder)


# Since they are in columns, when it comes to the 2nd column it will stop
stop_list = ["LIL", "LIL-DEF", "GEN", "FUT", "NEG", "PREP-DEF", "DEF", "COMP", "X-PUN", "PREP", "X-ABV", "CONJ-CORD"]

# Looping through the files in the MLRS corpus
for folder in folders_list:
    path = directory + "/" + folder.name
    with os.scandir(path) as files:
        for file in files:
            if file.is_file():
                read_path = path + "/" + file.name
                write_path = new_directory + "/new_" + file.name

                # Reading the original MLRS files
                with open(read_path, "r", encoding="utf8") as r:
                    # Writing into the new MLRS files
                    with open(write_path, "w", encoding="utf8") as w:
                        for line in r:
                            if line.startswith("<") == False:
                                lines_list = line.split("\t")
                                # print(lines_list)
                                if lines_list[1] not in stop_list:
                                    if len(lines_list) == 4:
                                        if lines_list[2] != "null":
                                            print(lines_list[2], end=" ", file=w)
                                        else:
                                            print(lines_list[0], end=" ", file=w)
                                    else:
                                        print(lines_list[0], end=" ", file=w)
                            if "</s>" in line:
                                print(end="\n", file=w)
