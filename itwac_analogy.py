import gensim

# Retrieving the model
model = gensim.models.Word2Vec.load("ITWAC_model.csv")

# Comparing different vectors and finding the top 20 similarities
print("paura - verde: rabbia - :", model.wv.most_similar(positive=["rabbia", "verde"], negative=["paura"], topn=20))
print("gioia - giallo: guaio - :", model.wv.most_similar(positive=["guaio", "giallo"], negative=["gioia"], topn=20))
print("fiducia - verde: sorpreso - :", model.wv.most_similar(positive=["sorpreso", "sorpreso", "sorpresi", "verde"], negative=["fiducia"], topn=20))
print("sensibile - nero: interesse - :", model.wv.most_similar(positive=["interesse", "nero", "neri", "nere", "nera"], negative=["sensibile"], topn=20))
print("puro - bianco: triste - :", model.wv.most_similar(positive=["triste", "tristi", "bianco", "bianca", "bianchi", "bianche"], negative=["puro"], topn=20))
print("triste - rosa: puro - :", model.wv.most_similar(positive=["puro", "rosa"], negative=["triste"], topn=20))
print("calma - grigio: forte - :", model.wv.most_similar(positive=["forte", "grigio"], negative=["calma"], topn=20))
print("dolore - viola: disgusto - :", model.wv.most_similar(positive=["disgusto", "viola"], negative=["dolore"], topn=20))
print("sorpreso - blu: guaio - :", model.wv.most_similar(positive=["guaio", "blu"], negative=["sorpreso", "sorpreso", "sorpresi"], topn=20))
print("disgusto - rosa: anticipazione - :", model.wv.most_similar(positive=["anticipazione", "rosa"], negative=["disgusto"], topn=20))
print("anticipazione - arancione: calma - :", model.wv.most_similar(positive=["calma", "arancione"], negative=["anticipazione"], topn=20))
print("naturali - marrone: amore - :", model.wv.most_similar(positive=["amore", "marrone", "marroni"], negative=["naturale"], topn=20))
print("amore - rosso: naturale - :", model.wv.most_similar(positive=["naturali", "naturale", "rosso"], negative=["amore"], topn=20))
