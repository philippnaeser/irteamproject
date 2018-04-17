from bm25 import BM25
from collection_and_vocabulary import generate_collection, generate_vocabulary

collection = generate_collection()

bm25 = BM25(collection)

scores = bm25.get_scores()

print(scores)