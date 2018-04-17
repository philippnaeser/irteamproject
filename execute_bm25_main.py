from bm25 import BM25
from collection_and_vocabulary import generate_collection, generate_vocabulary, get_collection_size

collection = generate_collection()
size = get_collection_size()

corpus = []

for words in collection.values():
    word_list = words.split()
    corpus.append(word_list)

bm25 = BM25(corpus)
query = []
query.append('statin')
query.append('breast')
query.append('cancer')
average_idf = 0.5


scores = bm25.get_scores(query,average_idf)

print(scores)