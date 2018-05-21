import mord
from sklearn import linear_model, metrics, preprocessing

class Predictiv_Learner_Mord():

    def do_prediction(self, X_train, X_test, y_train, y_test):

        clf2 = mord.LogisticAT(alpha=1.0)
        clf2.fit(X_train, y_train)
        result = clf2.predict(X_test)
        matrix = metrics.confusion_matrix(y_test, result)
        print(matrix)

        score = metrics.average_precision_score(y_test, result)
        print(score)

        # ranking = metrics.label_ranking_average_precision_score(y.values.argmax(axis=1), result)
        # print('ranking: ', ranking)

        #print('Mean Absolute Error of LogisticAT %s' %
        #      metrics.mean_absolute_error(clf2.predict(X), y))

        #clf3 = mord.LogisticIT(alpha=1.)
        #clf3.fit(X, y)
        #print('Mean Absolute Error of LogisticIT %s' %
        #      metrics.mean_absolute_error(clf3.predict(X), y))

        #clf4 = mord.LogisticSE(alpha=1.)
        #clf4.fit(X, y)
        #print('Mean Absolute Error of LogisticSE %s' %
        #      metrics.mean_absolute_error(clf4.predict(X), y))