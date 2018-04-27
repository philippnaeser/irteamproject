##Goal of pairwise approach is to find a exact relevance ranking of the documents regarding a specific query


##create a full index od our document data because we want to compare each document with every other document
#Important: we need to do this for every query, such that we have a 1:(n:n) matching
# (1) Create all possible, unique pairs. for every query, we compare every document with every other document in our data.
# if we have e.g. 5000 query we have to perform this process 5000 times
#TODO create the query embedding

import recordlinkage as recordlinkage

indexer = recordlinkage.Fullindex()
pairs = indexer.index("""document_data""")
#this returns a pandas.Multiindex
## TODO fill in the data

print(len(pairs), len("""term_incidence_matrix"""))
#sanitiy check: len(pairs)= (len(term_incidence_matrix)*len(term_incidence_matrix) - len(term_incidence_matrix))


# (2) here we give in the term_incidence matrix with different similarity values, what will be done in the
# #previous step. All comparisions are stored in a DataFrame with horizontally the features (vocabulary) and vertically the record pairs

compare_query_with_document = recordlinkage.Compare
result_features = compare_query_with_document.compute(pairs, """document_data""")

# (3) Calculate the exact relevance ranking
##TODO think of give in the TIM with different sim values one after another or one BIG TIM with all different sim approaches
#TODO create heuristic
    #such that every document is assigned a random position number
    #start comparing, if one document has a higher score than the other document it gets a higher position



##MACHINE LEARNING

#here we apply some machine learning like RankBoost and RankingSVM

# (1) create goldstandard

golden_pairs = "the comparison verctors" #pandas.DataFrame
golden_matches_index = "id's of labeled, matching pairs TRAININGSET"  #pandas.MultiIndex which contains the true matches

# (2) Learn classifier
# TODO insert the classifiers: RankBoost and RankingSVM
# TODO update the relevance scores based on the prediction



#EVALUATION
confusion_matrix = recordlinkage.confusion_matrix("id's of matched pairs TESTSET", "result_classifier",len("id's of matched pairs TESTSET") )

#calculate Discounted Cumulative Gain (this works for multiple relevance judgement)
