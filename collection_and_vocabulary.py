'''
The index and vocabulary are created from the medical documents data (*.docs  files).
Each medical document is already pre-proceessed and represented as a BoW. Words are being lowercased, and stopwords have been removed.
The 'raw' folder contains raw queries and documents, as well as an specification of stopwords being removed.
'''

from collections import Counter

'''
COLLECTION
- generate document collection as dictionary; doc-IDs are keys to return document
'''

def generate_collection():
    collection = {}
    with open('nfcorpus/train.docs', 'r') as rf1:
        with open('nfcorpus/dev.docs', 'r') as rf2:
            with open('nfcorpus/test.docs', 'r') as rf3:
                for i in [rf1,rf2,rf3]:
                    for line in i:
                        l = line.split('\t')
                        l[1] = l[1].strip('\n ')
                        collection[l[0]] = l[1]
    print('Collection created successfully containing %s documents' %len(collection))
    return collection


# N = 531162
def get_collection_size():
    a = generate_vocabulary()
    b = (sum(a.values()))
    print('The collection contains %s terms' % (b))
    return b

'''
VOCABULARY
- generate vocabulary as Counter object
- use this Counter object to calculate collection statistics
'''


def generate_vocabulary():
    vocab = Counter()
    list_of_terms= [] # we want all terms to be in a list to make Counter work
    col = generate_collection()
    for i in col.values():
        list_of_terms += i.split()
    for word in list_of_terms:
            vocab[word] += 1
    return vocab

# returns list of all terms
def get_vocabulary():
    a= generate_vocabulary()
    b= (list(a.keys()))
    print(b)


# ||V||= 29052
def get_vocabulary_length():
    a= generate_vocabulary()
    print('The vocabulary contains %s unique words.' %len(a.keys()))
    return len(a.keys())




