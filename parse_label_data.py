from convokit import Corpus, TextParser
from load_data import load_data

# since there is way less data in the r/bookscirclejerk corpus
# and because of computational limits I trimmed the r/Books
# Corpus to be of ruffly equal size.
# The Trimmed version of the books corpus can be found in the
# github repository.

corpus_books_small = load_data("books.corpus")
corpus_circle = load_data("bookscirclejerk.corpus")
print("done loading")

# for comparison:
# r/books - subset
# number of Utterancees 20000

# r/bookscirclejerk - full (without empty entries)
# number of Utterances 15850

# First, corpora Text next to be parsed
parser = TextParser()

corpus_books_small = parser.transform(corpus_books_small)
corpus_circle = parser.transform(corpus_circle)

# label utterances in corpora,
# 1 == r/bookscirclejerk, 0 == r/books
for circ_utt in corpus_circle.iter_utterances():
    circ_utt.meta["label"] = 1
for book_utt in corpus_books_small.iter_utterances():
    book_utt.meta["label"] = 0

# combine corpora

# save combined corpus
# default location is: .convokit/saved-corpora
corpus_books_small.dump("corpus_books_parsed")
corpus_circle.dump("corpus_circle_parsed")
