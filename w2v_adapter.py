from gensim.models import word2vec
import numpy as np
import nltk
import pandas as pd
import swifter


class Word2VecAdapter:
    def __init__(self, pre_trained_model=None, num_features=250, min_count=40, workers=4,
                 window=10, sample=0.001):

        self.num_features = num_features
        self.min_count = min_count
        self.workers = workers
        self.window = window
        self.sample = sample
        self.wv = pre_trained_model
        if pre_trained_model:
            self.word_index = set(self.wv.index_to_key)

    def fit(self, X):
        if not self.wv:
            X = X.swifter.allow_dask_on_strings().apply(nltk.word_tokenize)
            model = word2vec.Word2Vec(X, workers=self.workers,
                                      vector_size=self.num_features, min_count=self.min_count,
                                      window=self.window, sample=self.sample)
            self.wv = model.wv
            self.word_index = set(self.wv.index_to_key)

    def predict(self, comment):

        key_words = filter(lambda w: w in self.word_index, nltk.word_tokenize(comment))
        vectors = self.wv[key_words]
        return np.divide(np.sum(vectors, axis=0), len(vectors))

    def fit_transform(self, X):
        if not self.wv:
            self.fit(X)
        return self.transform(X)

    def transform(self, X):
        return X.swifter.apply(lambda x: pd.Series(self.predict(x)))
