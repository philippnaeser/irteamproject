## the goal for the pointwise approach is to create a exact relevance score of the document for a specific query

## CREATE POINT-WISE COMPARISON PROCESS

# (1) Create all possible, unique pairs. we compare every query with all documents,
# each pair contains therefore one query and one document

import recordlinkage as recordlinkage

indexer = recordlinkage.Fullindex()
pairs = indexer.index("""query_data, document_data""")
#this returns a pandas.Multiindex
## TODO fill in the data

print(len(pairs), len("""query_data"""), len("""term_incidence_matrix"""))
#sanitiy check: len(pairs)= len(query_data)*len(term_incidence_matrix)


# (2) We now want to compare the records whether this is relevant for a specific query or not.
# Therefore we consider each pair as a candidate pair. Important: Eventhough we have "pairs" we
#take only one document into consideration because the pairs consist of a query and 1(!!) document

compare_query_with_document = recordlinkage.Compare

#here we give in the term_incidence matrix with different similarity values, what will be done in the
#previous step
##TODO think of give in the TIM with different sim values one after another or one BIG TIM with all different sim approaches

result_features = compare_query_with_document.compute(pairs, """query_data, document_data""")

#all comparisions are stored in a DataFrame with horizontally the features (vocabulary) and vertically the record pairs

# (3) we create now a ranking according to some method. As base, we just take the sum of the simvalues
# and rank them ascending

final_ranking = result_features.sum(axis=1).value_counts().sort_index(ascending=False)
print(final_ranking)

##MACHINE LEARNING

#here we apply some machine learning like Ordinal Regression to learn the weights
#and update the sum with those weights. e.g. before: sum = sim_value1 + sim_value2,
#now: sum = sim_value1*weight1 + sim_value2*weight2...
#the ranking of the document is again created by sorting the sums ascending

# (1) create goldstandard

golden_pairs = "the comparison verctors" #pandas.DataFrame
golden_matches_index = "id's of labeled, matching pairs TRAININGSET"  #pandas.MultiIndex which contains the true matches

# (2) Learn classifier

##here I take a binary classifier as base to check whether the process is working
# TODO replace this classifier later with ordinal regression
# TODO take full coding, not only calling a function

#Initialize Classifier
logreg = recordlinkage.LogisticRegressionClassifier()

#Train the classifier
logreg.learn((golden_pairs, golden_matches_index))
print("Intercept:", logreg.intercept)
print("Coefficients/weights: ", logreg.coefficients)

#Predict the match status for all record pairs - this is the multiplication with the sim_values
#like described above

result_logreg = logreg.predict("""document data / term incidence matrix""")

#EVALUATION
confusion_matrix_logreg = recordlinkage.confusion_matrix("id's of matched pairs TESTSET", result_logreg,len("id's of matched pairs TESTSET") )

#calculate F1 score
F1_score = recordlinkage.fscore(confusion_matrix_logreg)
print("F1-score: ", F1_score)
