class Collection:
    '''
    We want to present the document collection in the following way:
    - it's an instance of the Collection class
    - it has an attribute collection that is a  dictionary
    - the dictionary's keys are the doc-IDs
    - the corresponding values are the document contents represented as a list of strings
    '''
    def __init__(self):
        self.collection={}
        self.collection_length= 0

    def generate_collection(self):
        '''
        The index and vocabulary are created from the medical documents data (*.docs  files).
        Each medical document is already pre-proceessed and represented as a BoW. Words are being lowercased, and stopwords have been removed.
        The 'raw' folder contains raw queries and documents, as well as an specification of stopwords being removed.
        '''
        with open('nfcorpus/train.docs', 'r') as rf1:
            with open('nfcorpus/dev.docs', 'r') as rf2:
                with open('nfcorpus/test.docs', 'r') as rf3:
                    for i in [rf1, rf2, rf3]:
                        for line in i:
                            l = line.split('\t')
                            l[1] = l[1].strip('\n ').split()
                            self.collection[l[0]] = l[1] # since we want document represented as a list of strings
        print('Collection created successfully containing %s documents' % len(self.collection))
        for key in self.collection: #don't forget to update collection_length
            self.collection_length += len(self.collection[key])


    def get_collection(self):
        return self.collection


    def get_collection_size(self):  # N = 531162
        return self.collection_length

'''
#Sanity Checks
a=Collection()
a.generate_collection()
with open('check.txt', 'w') as wf: wf.write(str(a.collection))
print(len(a.collection))
print(len(a.collection.values()))
print(a.collection_length)
'''