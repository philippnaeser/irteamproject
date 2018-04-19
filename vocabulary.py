class Vocabulary:
    '''
    A vocabulary, represented as an ordered tuple that contains each word exactly once, is generated from a list of strings.
    Later on, a vocabulary object may be created on the collection level as well as for each document.
    It may then be used to calculate summary statistics (N,TF,...)
        '''

    def __init__(self, list_of_terms):
        self.vocabulary = ()
        assert type(list_of_terms) is list, 'require list as input'
        for i in range(len(list_of_terms)):
            assert type(list_of_terms[i]) is str, "every list element has to be string"
        self.vocabulary = tuple(sorted(set(list_of_terms)))
        self.vocabulary_size=len(self.vocabulary)

    def get_vocabulary(self):
        return self.vocabulary

    def print_vocabulary(self):
        print(self.vocabulary)

    def get_vocabulary_size(self): # ||V||= 29052
        return self.vocabulary_size


