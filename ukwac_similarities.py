import gensim

# Retrieving the model
model = gensim.models.Word2Vec.load("UKWAC_model.csv")

# Finding the top 50 similarities for the colours
print("black : ", model.wv.most_similar("black", topn=50))
print()
print("white : ", model.wv.most_similar("white", topn=50))
print()
print("red : ", model.wv.most_similar("red", topn=50))
print()
print("green : ", model.wv.most_similar("green", topn=50))
print()
print("yellow : ", model.wv.most_similar("yellow", topn=50))
print()
print("blue : ", model.wv.most_similar("blue", topn=50))
print()
print("brown : ", model.wv.most_similar("brown", topn=50))
print()
print("orange : ", model.wv.most_similar("orange", topn=50))
print()
print("pink : ", model.wv.most_similar("pink", topn=50))
print()
print("purple : ", model.wv.most_similar("purple", topn=50))
print()
print("grey : ", model.wv.most_similar("grey", topn=50))
print()