import gensim

# Retrieving the model
model = gensim.models.Word2Vec.load("MLRS_model.csv")

# Finding the top 50 similarities for the colours
print("iswed : ", model.wv.most_similar("iswed", topn=50))
print("abjad : ", model.wv.most_similar("abjad", topn=50))
print("aħmar : ", model.wv.most_similar("aħmar", topn=50))
print("aħdar : ", model.wv.most_similar("aħdar", topn=50))
print("isfar : ", model.wv.most_similar("isfar", topn=50))
print("blu : ", model.wv.most_similar("blu", topn=50))
print("kannella : ", model.wv.most_similar("kannella", topn=50))
print("oranġjo : ", model.wv.most_similar("oranġjo", topn=50))
print("roża : ", model.wv.most_similar("roża", topn=50))
print("vjola : ", model.wv.most_similar("vjola", topn=50))
print("griż : ", model.wv.most_similar("griż", topn=50))
