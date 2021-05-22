import gensim

# Retrieving the model
model = gensim.models.Word2Vec.load("MLRS_model.csv")

# Comparing different vectors and finding the top 20 similarities
print("għira - aħdar: imħabba - : ", model.wv.most_similar(positive=["imħabba", "aħdar"], negative=["għira"], topn=20))
print("biża - aħdar: rabja - :", model.wv.most_similar(positive=["rabja", "aħdar"], negative=["biża"], topn=20))
print("ferħ - isfar: inkwiet - :", model.wv.most_similar(positive=["inkwiet", "isfar"], negative=["ferħ"], topn=20))
print("fiduċja - aħdar: sorpriż - :", model.wv.most_similar(positive=["sorpriż", "aħdar"], negative=["fiduċja"], topn=20))
print("sensittiv - iswed: interess - :", model.wv.most_similar(positive=["interess", "iswed"], negative=["sensittiv"], topn=20))
print("pur - abjad: imdejjaq - :", model.wv.most_similar(positive=["imdejjaq", "abjad"], negative=["pur"], topn=20))
print("imdejjaq - roża: pur - :", model.wv.most_similar(positive=["pur", "roża"], negative=["imdejjaq"], topn=20))
print("kalm - griż: qawwi - :", model.wv.most_similar(positive=["qawwi", "griż"], negative=["kalm"], topn=20))
print("niket - vjola: stmerrija - :", model.wv.most_similar(positive=["stmerrija", "vjola"], negative=["niket"], topn=20))
print("sorpriż - blu: niket - :", model.wv.most_similar(positive=["niket", "blu"], negative=["sorpriż"], topn=20))
print("stmerrija - roża: antiċipazzjoni - :", model.wv.most_similar(positive=["antiċipazzjoni", "roża"], negative=["stmerrija"], topn=20))
print("antiċipazzjoni - oranġjo: kalm - :", model.wv.most_similar(positive=["kalm", "oranġjo"], negative=["antiċipazzjoni"], topn=20))
print("naturali - kannella: imħabba - :", model.wv.most_similar(positive=["imħabba", "kannella"], negative=["naturali"], topn=20))
print("imħabba - aħmar: naturali - :", model.wv.most_similar(positive=["naturali", "aħmar"], negative=["imħabba"], topn=20))
