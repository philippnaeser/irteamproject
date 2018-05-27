from data_load import Data_Loader
from predictiv_learning_sklearn import Predictiv_Learner_Sklearn
import pandas as pd

data_loader = Data_Loader()
X_train, y_train, X_test, y_test = data_loader.load_dev_data()
print('data load finished')


pred_sklear = Predictiv_Learner_Sklearn()
ranked_result = pred_sklear.do_prediction(X_train, X_test, y_train, y_test)

print('prediction done')