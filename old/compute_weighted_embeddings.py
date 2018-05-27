# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

def get_weighted_embeddings(embeddings, tfidf_embed):
    sum_of_tfidf_weights=tfidf_embed.sum(axis=0)#vector containing the normalizing constant for each doc
    weighted_embeddings=tfidf_embed.mask(tfidf_embed!=0, other=(tfidf_embed*embeddings).div(sum_of_tfidf_weights))
    print('done')
    return weighted_embeddings

#Load the pickle files needed
fasttext_embeddings = pd.read_pickle('fasttext_embeddings.pkl')
word2vec_embeddings = pd.read_pickle('word2vec_embeddings.pkl')
tfidf = pd.read_pickle('tfidf.pkl')
train_tfidf = pd.read_pickle('queries/train_tfidf.pkl')
dev_tfidf = pd.read_pickle('queries/dev_tfidf.pkl')
test_tfidf = pd.read_pickle('queries/test_tfidf.pkl')

#As this is  computationally rather expensive, only run it for one set at a time
#It is probably preferable to unzip the embeddings.zip and the queries/query_embeddings.zip, where these computations are already stored
#Fasttext
print('starting')
documents_fasttext = get_weighted_embeddings(fasttext_embeddings, tfidf)
#train_queries_fasttext = get_weighted_embeddings(fasttext_embeddings, train_tfidf)
#dev_queries_fasttext = get_weighted_embeddings(fasttext_embeddings, dev_tfidf)
#test_queries_fasttext = get_weighted_embeddings(fasttext_embeddings, test_tfidf)
#Let's save those again, as computing them might take a while
documents_fasttext.to_pickle('documents_fasttext.pkl')
#train_queries_fasttext.to_pickle('queries/train_queries_fasttext.pkl')
#dev_queries_fasttext.to_pickle('queries/dev_queries_fasttext.pkl')
#test_queries_fasttext.to_pickle('queries/test_queries_fasttext.pkl')

#Word2vec
#documents_word2vec= get_weighted_embeddings(word2vec_embeddings, tfidf)
#train_queries_word2vec = get_weighted_embeddings(word2vec_embeddings, train_tfidf)
#dev_queries_word2vec = get_weighted_embeddings(word2vec_embeddings, dev_tfidf)
#test_queries_word2vec = get_weighted_embeddings(word2vec_embeddings, test_tfidf)
#Save them as well
#documents_word2vec.to_pickle('documents_word2vec.pkl')
#train_queries_word2vec.to_pickle('queries/train_queries_word2vec.pkl')
#dev_queries_word2vec.to_pickle('queries/dev_queries_word2vec.pkl')
#test_queries_word2vec.to_pickle('queries/test_queries_word2vec.pkl')
