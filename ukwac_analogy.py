import gensim

# Retrieving the model
model = gensim.models.Word2Vec.load("UKWAC_model.csv")

# Comparing different vectors and finding the top 20 similarities
print("envy - green: love - : ", model.wv.most_similar(positive=["love", "green"], negative=["envy"], topn=20))
print("fear - green: anger - :", model.wv.most_similar(positive=["anger", "green"], negative=["fear"], topn=20))
print("happy - yellow: worried - :", model.wv.most_similar(positive=["worried", "yellow"], negative=["happy"], topn=20))
print("trust - green: surprised - :", model.wv.most_similar(positive=["surprised", "green"], negative=["trust"], topn=20))
print("sensitive - black: interested - :", model.wv.most_similar(positive=["interested", "black"], negative=["sensitive"], topn=20))
print("pure - white: bored - :", model.wv.most_similar(positive=["bored", "white"], negative=["pure"], topn=20))
print("bored - pink: pure - :", model.wv.most_similar(positive=["pure", "pink"], negative=["bored"], topn=20))
print("calm - grey: powerful - :", model.wv.most_similar(positive=["powerful", "grey"], negative=["calm"], topn=20))
print("grief - purple: disgust - :", model.wv.most_similar(positive=["disgust", "purple"], negative=["grief"], topn=20))
print("surprised - blue: grief - :", model.wv.most_similar(positive=["grief", "blue"], negative=["surprised"], topn=20))
print("disgust - pink: anticipation - :", model.wv.most_similar(positive=["anticipation", "pink"], negative=["disgust"], topn=20))
print("anticipation - orange: calm - :", model.wv.most_similar(positive=["calm", "orange"], negative=["anticipation"], topn=20))
print("natural - brown: love - :", model.wv.most_similar(positive=["love", "brown"], negative=["natural"], topn=20))
print("love - red: natural - :", model.wv.most_similar(positive=["natural", "red"], negative=["love"], topn=20))
