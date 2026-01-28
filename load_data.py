from convokit import Corpus
import os

# default Path to dumped corpora is {user}/.convokit/saved-corpora/{corpora_name}


def load_data(filename):
    full_name = "~/.convokit/saved-corpora/" + filename
    filepath = os.path.expanduser(full_name)
    print(filepath)
    corpus = Corpus(filepath)
    print(f"loaded corpus: {filename} successfully")
    return corpus
