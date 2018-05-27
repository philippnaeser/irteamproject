import pickle
import pandas as pd
from sklearn.model_selection import train_test_split

class Data_Loader():

    def __init__(self):
        self.data_test_url = '../2_query_representation/pickle/test_scores.pkl'
        self.data_train_url = '../2_query_representation/pickle/train_scores.pkl'
        self.data_dev_url = '../2_query_representation/pickle/dev_scores.pkl'

    def load_data(self):
        test_data = pd.read_pickle(self.data_test_url)
        train_data = pd.read_pickle(self.data_train_url)

        test_data_rel = test_data['rel']
        train_data_rel = train_data['rel']

        test_data_pred = test_data[['tfidf', 'bim25', 'bim25_alt', 'unigram', 'cosine', 'fasttext', 'word2vec', 'qid']]
        train_data_pred = train_data[['tfidf', 'bim25', 'bim25_alt', 'unigram', 'cosine', 'fasttext', 'word2vec', 'qid']]
        
        print('Number of training data: ', len(train_data_pred))
        print('Number of test data: ', len(test_data_pred))

        return train_data_pred, \
               train_data_rel, \
               test_data_pred, \
               test_data_rel

    def load_dev_data(self):
        dev_data = pd.read_pickle(self.data_dev_url)
        sorted_data = dev_data.sort_index()
        length = len(dev_data.index)
        #dev_data_small = dev_data
        dev_data_small = dev_data.loc[dev_data['qid'] < '200']
        length_small = len(dev_data_small.index)
        print('Number of records: ', length_small)

        dev_data_rel = dev_data_small['rel']
        dev_data_pred = dev_data_small[['tfidf', 'bim25', 'bim25_alt', 'unigram', 'cosine', 'fasttext', 'word2vec', 'qid']]

        # Limit to the two first classes, and split into training and test
        X_train, X_test, y_train, y_test = train_test_split(dev_data_pred, dev_data_rel,
                                                            test_size=.2)

        print('Number of training data: ', len(X_train))
        print('Number of test data: ', len(X_test))
        return X_train, y_train, X_test, y_test
