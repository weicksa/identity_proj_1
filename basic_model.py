from convokit import Corpus, Classifier

filepath = "corpus_comp"
corpus_comp = Corpus(filepath)

cv_classifier_subreddit = Classifier(
    obj_type="utterance", pred_feats=["politeness_strategies"],
    labeller=lambda u: u.meta["label"] == 1)

cv_results = cv_classifier_subreddit.evaluate_with_cv(corpus_comp)

print("Cross-validation accuracy per fold: ", cv_results)
print("Mean accuracy: ", sum(cv_results) / len(cv_results))
