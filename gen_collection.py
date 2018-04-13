'''
documents appear several times within train/dev/test.docs
e.g. doc MED-10 may appear twice within train.docs and once within dev/test.docs each
goal: generate a collection that contains every doc exactly once
'''

def generate_collection():
    with open('nfcorpus/train.docs', 'r') as a:
        with open('nfcorpus/dev.docs', 'r') as b:
            with open('nfcorpus/dev.docs', 'r') as c:
                    with open('collection.txt', 'w') as wf:
                        redundant = a.readlines() + b.readlines() + c.readlines()
                        concise= sorted(set(redundant))
                        print('There are %s docs in the collection' %len(concise))
                        wf.write(str(concise))
                        return concise

def print_collection():
    a=generate_collection()
    print(a)

#TODO: write function retrieve_doc() that given a key (MED-...) returns the document (=list of strings)
