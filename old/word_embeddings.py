'''
This code may take up to an hour (although already optimized > pd.mask()
It generates an tfidf-weighted vector in both 100d embedding spaces for each document.
When running this code in Jupyter, the kernel is likely to die: execute this code in a separate .py file
'''
###########
# Word2Vec
############
import pandas as pd
import numpy as  np
tfidf=pd.read_pickle('tfidf.pkl')
fasttext_embeddings=pd.read_pickle('fasttext_embeddings.pkl')
word2vec_embeddings=pd.read_pickle('word2vec_embeddings.pkl')
columns=tfidf.columns
sum_of_tfidf_weights=tfidf.sum(axis=0)#vector containing the normalizing constant for each doc
pd.
weighted_word2vec_embeddings=tfidf.mask(tfidf!=0, other=(tfidf*word2vec_embeddings).div(sum_of_tfidf_weights))
weighted_word2vec_embeddings.to_pickle('weighted_word2vec_embeddings.pkl')
###########
# FastText
############
'''
import pandas as pd
import numpy as  np
tfidf=pd.read_pickle('tfidf.pkl')
fasttext_embeddings=pd.read_pickle('fasttext_embeddings.pkl')
word2vec_embeddings=pd.read_pickle('word2vec_embeddings.pkl')
sum_of_tfidf_weights=tfidf.sum(axis=0)#vector containing the normalizing constant for each doc
weighted_fasttext_embeddings=tfidf.mask(tfidf!=0, other=(tfidf*fasttext_embeddings).div(sum_of_tfidf_weights))
weighted_fasttext_embeddings.to_pickle('weighted_fasttext_embeddings.pkl')
'''