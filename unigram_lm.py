'''
UNIGRAM LM with Jelinek-Mercer-Smoothing
- computing a global and a local language model
- then writing a function that averages
# TODO: generellere Funktion schreiben: Cumpute LM, die dict als input nimmt, und dann dict mit probabilities returned
# TODO: consider working with log-probabilitiies (=avoid underflow, adding is faster than mulptiplication)
'''

from collection_and_vocabulary import *
from collections import Counter

'''
GLOBAL LM
-count how often each term occurs in the entire collection (=nominator)
-count the total amount of all terms in the collection (=nominator)

'''
def generate_global_lm():
    global_lm= {}
    global_lm= {}
    N = get_collection_size()
    global_lm = generate_vocabulary()
    for i in global_lm.keys():
        global_lm[i]= global_lm[i]/N
    return global_lm


'''
LOCAL LMs
-idea: calculate a LM for each single document in the collection
-count how often each term occurs in the entire collection (=nominator)
-count the total amount of all terms in the collection (=nominator)
'''

# Generating
def generate_local_LMs():
    all_local_lms = {} # this is what will be returned: a dictionary with doc-IDs being keys pointing to dictionaries with words being keys and tf being values
    collection= generate_collection()
    for i in collection.keys(): # TODO: this is a modified version of the generate_vocab() function > maybe possible to generalize it?
            vocab_of_doc = Counter()
            list_of_terms = []  # we want all terms to be in a list to make Counter work
            doc_as_string = collection[i] # therefore read them in as string
            list_of_terms += doc_as_string.split() # then split this string into list of strings ['word1', 'word2',...]
            for word in list_of_terms: # TODO: reimplement with an extended version of Counter: https://www.dataquest.io/blog/python-counter-class/
                    vocab_of_doc[word] += 1
            doc_length = len (list_of_terms) # we want probabilities/rel. frequencies; this means we'll normalize raw count by N (=number of terms in each doc)
            vocab_of_doc_normalized = {}
            for key in vocab_of_doc.keys():
                if doc_length != 0:   #TODO: report that MED-961 is an empty doc
                    vocab_of_doc_normalized[key] = vocab_of_doc[key]/doc_length
            return (vocab_of_doc_normalized)
    all_local_lms[i]= vocab_of_doc_normalized[i]

generate_local_LMs()

