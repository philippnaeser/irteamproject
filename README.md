# Team Project FSS 2018 - Information Retrieval and Web Search

This is the documentation for our university team project, where we had the task to learn to rank on a full-text English retrieval data set for Medical Information Retrieval[http://www.cl.uni-heidelberg.de/statnlpgroup/nfcorpus/].

In order to replicate our results, the code contained in each folder should should be run sequentially. Additionally, we provide in each folder a zipped Python .pkl file that is the output of the corresponding Jupyter notebook.

**0_Collection_and_Inverted_Index**
- read in all 3633 docs (already being precomputed BoWs),
- generate vocabulary, calculate collection statistics
- create inverted index of the collection, represented as a Pandas dataframe 

**1_Document Representation**
- this folder covers the feature generation process 
- each .ipynb file covers one IR model (TFIDF, UnigramLM, BM25, Word Embeddings), and produces one or more Pandas dataframes as outputs that represents the document collection within the respective models
- the embeddings_experiments.ipynb documents our (failed) try of using pretrained embeddings for the rating.

**2_Query Representation**
- ...

