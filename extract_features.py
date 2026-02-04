from convokit import Corpus, PolitenessStrategies, 
BoWTransformer
from elfen.extractor import Extractor

import Sys
import polars as pl

from load_data import load_data

# one function for convokit features
def get_convo_features(corpus):
    # get PolitenessStrategies from convokit
    pol_strategies = PolitenessStrategies()
    # get BoWTransformer from convokit
    bow_trans = BoWTransformer()
    # extract features
    corpus = pol_strategies.transform(corpus, markers=True)
    corpus = bow_trans.transform(corpus)
    return(corpus)

# one function for *all* ELFEN features
# input for elfen feature extractor expects a pandas dataframe
def get_elfen_features(corpus):
    db_corp = pl.from_pandas(corpus)
    extractor = Extractor(data = db_corp)
    # extract *all* features that ELFEN provides
    # WARNING: this requires additional lexicons to be installed manually
    feats = extractor.extract_features()

    # returns a polars database
    return(extractor)


if __name__ == "__main__":
    # get filename from terminal argument
    filename = Sys.argv[0]
    # default filenames of parsed data are:
    # - corpus_books_parsed
    # - corpus_circle_parsed
    data = load_data(filename)
    print(f"\n {40*-}\nExtracting Convokit features ...")
    conv_feat = get_convo_features(data)
    print(f"\n {40*-}\n- Done Extracting Convokit features -")
    # convert Convokit corpus to Pandas Dataframe
    print(f"\n {40*-}\n- Saving Corpus with only Convokit features ...")
    conv_savename = f"convo_{filename}"
    # default location of dump() is {user}/.convokit/saved-corpora
    conv_feat.dump(conv_savename)
    print(f"\n {40*-}\n- Done saving Convokit features -")
    data_panda_df = conv_feat.get_utterances_dataframe()
    print(f"\n {40*-}\nExtracting ELFEN features ...")
    elfen_feat = get_elfen_features(data_panda_df)
    print(f"\n {40*-}\n- Done Extracting ELFEN features -")
    print(f"\n {40*-}\n- Saving Corpus as Polars Database ...")

    savename = f"feats_{filename}.json"
    elfen_feat.data.write_ndjson(savename)
    print(f"\n {40*-}\n- Done saving -")

