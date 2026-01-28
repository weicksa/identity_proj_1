from convokit import Corpus


def load_data(filepath):
    corpus = Corpus(filepath)
    return corpus
