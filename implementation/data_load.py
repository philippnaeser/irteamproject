import pickle
from sklearn.model_selection import train_test_split

class Data_Loader():

    def __init__(self):
        self.data_test_url = '../queries/scores/test_scores.pkl'
        self.data_train_url = '../queries/scores/train_scores.pkl'
        self.data_dev_url = '../queries/scores/dev_scores.pkl'

    def load_data(self):
        test_data = pickle.load(open(self.data_test_url, "rb"))
        train_data = pickle.load(open(self.data_train_url, "rb"))

        test_data_rel = test_data['rel']
        train_data_rel = train_data['rel']

        test_data_pred = test_data[['tfidf', 'bim25', 'unigram', 'qid']]
        train_data_pred = train_data[['tfidf', 'bim25', 'unigram', 'qid']]

        return train_data_pred, \
               train_data_rel, \
               test_data_pred, \
               test_data_rel

    def load_dev_data(self):
        dev_data = pickle.load(open(self.data_dev_url, "rb"))
        sorted_data = dev_data.sort_index()
        length = len(dev_data.index)
        #dev_data_small = dev_data
        dev_data_small = dev_data.loc[dev_data['qid'] < '100']
        length_small = len(dev_data_small.index)
        print('Number of records: ', length_small)

        dev_data_rel = dev_data_small['rel']
        dev_data_pred = dev_data_small[['tfidf', 'bim25', 'unigram', 'qid']]

        # Limit to the two first classes, and split into training and test
        X_train, X_test, y_train, y_test = train_test_split(dev_data_pred, dev_data_rel,
                                                            test_size=.2)

        print('Number of training data: ', len(X_train))
        print('Number of test data: ', len(X_test))
        return X_train, y_train, X_test, y_test
