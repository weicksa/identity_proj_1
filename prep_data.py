from convokit import Corpus, download, PolitenessStrategies, TextParser

# since there is way less data in the r/bookscirclejerk corpus
# and because of computational limits I trimmed the r/Books
# Corpus to be of ruffly equal size.
# The Trimmed version of the books corpus can be found in the
# github repository.

corpus_books_small = Corpus(filename="books.corpus")
corpus_circle = Corpus(filename="bookscirclejerk.corpus")

# for comparison:
# r/books - subset
# number of Utterancees 20000

# r/bookscirclejerk - full (without empty entries)
# number of Utterances 15850

# First, corpora Text next to be parsed
parser = TextParser()

corpus_books_small = parser.transform(corpus_books_small)
corpus_circle = parser.transform(corpus_circle)

# get PolitenessStrategies from convokit
pol_strategies = PolitenessStrategies()

corpus_books_small = pol_strategies.transform(corpus_books_small, markers=True)
corpus_circle = pol_strategies.transform(corpus_circle)

# label utterances in corpora,
# 1 == r/bookscirclejerk, 0 == r/books
for circ_utt in corpus_circle.iter_utterances():
    circ_utt.meta["label"] = 1
for book_utt in corpus_books_small.iter_utterances():
    book_utt.meta["label"] = 0

# combine corpora
corpus_comp = corpus_books_small.merge(corpus_circle, corpus_books_small)

# save combined corpus
corpus_comp.dump("corpus_comp")
