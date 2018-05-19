from implementation.data_load import Data_Loader
from implementation.predictiv_learn_mord import Predictiv_Learner_Mord
from implementation.predictiv_learning_sklearn import Predictiv_Learner_Sklearn
import pandas as pd

data_loader = Data_Loader()
X_train, y_train, X_test, y_test = data_loader.load_dev_data()
print('data load finished')

pred_sklear = Predictiv_Learner_Sklearn()
scores = pred_sklear.do_prediction(X_train, X_test, y_train, y_test)

#pred_mord = Predictiv_Learner_Mord()
#pred_mord.do_prediction(X_train, X_test, y_train, y_test)

#result = pd.concat([X_test, scores], axis=1)
scores_dataframe = pd.DataFrame(scores)
new_index = X_test.index.values

#X_test.set_index('test', inplace = True)
#X_test['key'] = X_test.index
X_test = X_test.reset_index()

result = X_test.join(scores_dataframe)
result_sorted = result.sort_values(['qid', 'relevance_score'], ascending=[True, False])

print('predictive done')