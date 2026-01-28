from convokit import Corpus, PolitenessStrategies
from load_data import load_data

# since there is way less data in the r/bookscirclejerk corpus
# and because of computational limits I trimmed the r/Books
# Corpus to be of ruffly equal size.

corpus_books_small = load_data("corpus_books_parsed")
corpus_circle = load_data("corpus_circle_parsed")

# for comparison:
# r/books - subset
# number of Utterancees 20000

# r/bookscirclejerk - full (without empty entries)
# number of Utterances 15850


# get PolitenessStrategies from convokit
pol_strategies = PolitenessStrategies()

corpus_books_small = pol_strategies.transform(corpus_books_small, markers=True)
corpus_circle = pol_strategies.transform(corpus_circle)

# INSERT further feature extraction here:


corpus_books_small.dump("corpus_books_feat")
corpus_circle.dump("corpus_circle_feat")

# combine corpora
corpus_comp = corpus_books_small.merge(corpus_circle, corpus_books_small)

# save combined corpus
# default location is: .convokit/saved-corpora
corpus_comp.dump("corpus_comp")
