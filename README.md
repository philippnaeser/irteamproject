# Team Project FSS 2018 - Information Retrieval and Web Search

This is the documentation for our university team project, where we had the task to learn to rank on a full-text English retrieval data set for [Medical Information Retrieval]([http://www.cl.uni-heidelberg.de/statnlpgroup/nfcorpus/).

In order to replicate our results, the code contained in each folder should should be run sequentially. Additionally, we provide in each folder one or more zipped Python .pkl file that is the output of the corresponding Jupyter notebook.
The zip files are sometimes split into multiple files of 100MB, since github only allows files this large.

**0_Collection_and_Inverted_Index**
- read in all 3633 docs (already being precomputed BoWs),
- generate vocabulary, calculate collection statistics
- create inverted index of the collection, represented as a Pandas dataframe 

**1_Document Representation**
- this folder covers the feature generation process 
- each .ipynb file covers one IR model (TFIDF, UnigramLM, BM25, Word Embeddings), and produces one or more Pandas dataframes as outputs that represents the document collection within the respective models
- the embeddings_experiments.ipynb documents our (failed) try of using pretrained embeddings for the rating.

**2_Query Representation**
- this folder covers the process of calculating our scores for each feature for every query document pair.
- the .ipynb file contains everything from calculating tfidf for the queries to calculating the final scores for our ranker and creating a file readable by RankLib
- the outputs from the previous steps are used here, so we need those .pkl files (either let the scripts run or unzip the results.zip in each pickle folder.

**3_ranklib_framework**
- in this folder, we put the computed scores into the RankLib framework to create a ranking model and evaluate it on the test set.
- to train and evaluate a ranker, simply run the pointwise_approach.sh or pairwise_approach.sh scripts. To simply evaluate the sent in models without training, use the pointwise_eval.sh or pairwise_eval.sh
- both approaches use the train.csv as training, dev.csv as validation and test.csv as test set. The evaluation is run on the test set.
- since the framework runs on java, please make sure to have JAVA_HOME set in your environment. 
- if you are running this on windows, you may not be able to use the sh command in the powershell/cmd. You can either copy the commands and input them manually or install e.g. a version of git, which provides a sh.exe
- you can also skip the calculation of the scores by unzipping the sets.zip, which contains the train, dev and test set as used in our computations

