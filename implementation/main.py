from implementation.data_load import Data_Loader
from implementation.predictiv_learn_mord import Predictiv_Learner_Mord
from implementation.predictiv_learning_sklearn import Predictiv_Learner_Sklearn

data_loader = Data_Loader()
X_train, y_train, X_test, y_test = data_loader.load_dev_data()
print('data load finished')

pred_sklear = Predictiv_Learner_Sklearn()
pred_sklear.do_prediction(X_train.as_matrix(), X_test.as_matrix(), y_train.values, y_test.values)

#pred_mord = Predictiv_Learner_Mord()
#pred_mord.do_prediction(X_train, X_test, y_train, y_test)

print('predictive done')