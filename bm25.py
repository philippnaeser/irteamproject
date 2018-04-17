import math
from six import iteritems
from six.moves import xrange


# BM25 parameters.
PARAM_K1 = 1.5
PARAM_B = 0.75
EPSILON = 0.25


class BM25(object):

    def __init__(self, collection): #ehm. corpus
        self.corpus_size = len(collection)
        self.avgdl = sum(float(len(x)) for x in collection) / self.corpus_size
        self.corpus = collection
        self.frequency = []
        self.df = {}
        self.idf = {}
        self.initialize()

    def initialize(self):
        for document in self.corpus:
            frequencies = {}
            for word in document:
                if word not in frequencies:
                    frequencies[word] = 0
                frequencies[word] += 1
            self.frequency.append(frequencies)

            for word, freq in iteritems(frequencies):
                if word not in self.df:
                    self.df[word] = 0
                self.df[word] += 1

        for word, freq in iteritems(self.df):
            self.idf[word] = math.log(self.corpus_size - freq + 0.5) - math.log(freq + 0.5)

#Average_idf: average_idf = sum(map(lambda k: float(bm25.idf[k]), bm25.idf.keys())) / len(bm25.idf.keys())

    def get_score(self, query, index, average_idf):
        score = 0
        for word in query:
            if word not in self.frequency[index]:
                continue
            idf = self.idf[word] if self.idf[word] >= 0 else EPSILON * average_idf
            score += (idf * self.frequency[index][word] * (PARAM_K1 + 1)
                      / (self.frequency[index][word] + PARAM_K1 * (1 - PARAM_B + PARAM_B * len(query) / self.avgdl)))
        return score

    def get_scores(self, query, average_idf):
        scores = []
        for index in xrange(self.corpus_size):
            score = self.get_score(query, index, average_idf)
            scores.append(score)
        return scores


    def get_bm25_weights(corpus):
        bm25 = BM25(corpus)
        average_idf = sum(float(val) for val in bm25.idf.values()) / len(bm25.idf)

        weights = []
        for doc in corpus:
            scores = bm25.get_scores(doc, average_idf)
            weights.append(scores)

        return weights