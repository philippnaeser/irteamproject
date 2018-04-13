'''
The vocabulary is created from the medical documents data (*.docs  files).
Each medical document is already pre-proceessed and represented as a BoW. Words are being lowercased, and stopwords have been removed.
The 'raw' folder contains raw queries and documents, as well as an specification of stopwords being removed.
In order to create the vocabulary, we should use all documents in our collection (test+dev+train).
'''

import re

# generate document collection that contains each document once
# vocabulary is saved to textfile and printed out as list of Strings

# def generate_vocabulary():
def generate_vocabulary():
    vocabulary = []
    with open('nfcorpus/train.docs', 'r') as a:
        with open('nfcorpus/dev.docs', 'r') as b:
            with open('nfcorpus/dev.docs', 'r') as c:
                with open('vocabulary.txt', 'w') as wf:
                    not_cleansed = a.read() + b.read() + c.read()  # uncleansed because retrieved doc may appear several times within one set, as well as in test/dev/train set
                    cleansed = re.sub(r'MED-\d+\t', '', not_cleansed)
                    vocabulary = sorted(set(cleansed.split()))
                    wf.write(str(vocabulary))  # only str can be written to file
                    print('\n Vocabulary successfully created')
                    print('\n The vocabulary contains %s words. ' % str(len(vocabulary)))
                    return (vocabulary)

def print_vocabulary():
    a = generate_vocabulary()
    print(a)
