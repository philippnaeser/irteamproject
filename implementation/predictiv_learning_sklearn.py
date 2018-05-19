from sklearn import svm, datasets
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import average_precision_score
from itertools import cycle
import pandas as pd

#we have here a multilabel case
class Predictiv_Learner_Sklearn():

    def do_prediction(self, X_train, X_test, y_train, y_test):

        # http://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html

        # Create a simple classifier
        #logreg = LogisticRegression()
        #logreg.fit(X_train, y_train)
        #result = logreg.predict(X_test)


        #classifier = svm.LinearSVC()
        #classifier.fit(X_train, y_train)
        #y_score = classifier.decision_function(X_test)

        #average_precision = average_precision_score(y_test, y_score)

        #print('Average precision-recall score: {0:0.2f}'.format(
        #    average_precision))



        #precision, recall, _ = precision_recall_curve(y_test, y_score)

        #plt.step(recall, precision, color='b', alpha=0.2,
        #         where='post')
        #plt.fill_between(recall, precision, step='post', alpha=0.2,
         #                color='b')

        #plt.xlabel('Recall')
        #plt.ylabel('Precision')
        #plt.ylim([0.0, 1.05])
        #plt.xlim([0.0, 1.0])
        #plt.title('2-class Precision-Recall curve: AP={0:0.2f}'.format(
         #   average_precision))

        # Use label_binarize to be multi-label like settings
        Y_test = label_binarize(y_test, classes=[0, 1, 2, 3])
        Y_train = label_binarize(y_train, classes=[0, 1, 2, 3])
        n_classes = Y_train.shape[1]

        # We use OneVsRestClassifier for multi-label prediction
        # Run classifier
        classifier = OneVsRestClassifier(svm.LinearSVC())
        classifier.fit(X_train, Y_train)
        y_score = classifier.decision_function(X_test)
        result = classifier.predict(X_test)

        result_dataframe = pd.DataFrame(y_score)
        print(result_dataframe.columns.values)
        result_dataframe['relevance_score'] = result_dataframe[[0, 1, 2, 3]].apply(func=self.determine_relevance_score, axis=1)


        # For each class
        precision = dict()
        recall = dict()
        average_precision = dict()
        for i in range(n_classes):
            precision[i], recall[i], _ = precision_recall_curve(Y_test[:, i],
                                                                y_score[:, i])
            average_precision[i] = average_precision_score(Y_test[:, i], y_score[:, i])

        # A "micro-average": quantifying score on all classes jointly
        precision["micro"], recall["micro"], _ = precision_recall_curve(Y_test.ravel(),
                                                                        y_score.ravel())
        average_precision["micro"] = average_precision_score(Y_test, y_score,
                                                             average="micro")
        print('Average precision score, micro-averaged over all classes: {0:0.2f}'
              .format(average_precision["micro"]))

        plt.figure()
        plt.step(recall['micro'], precision['micro'], color='b', alpha=0.2,
                 where='post')
        plt.fill_between(recall["micro"], precision["micro"], step='post', alpha=0.2,
                         color='b')

        plt.xlabel('Recall')
        plt.ylabel('Precision')
        plt.ylim([0.0, 1.05])
        plt.xlim([0.0, 1.0])
        plt.title(
            'Average precision score, micro-averaged over all classes: AP={0:0.2f}'
                .format(average_precision["micro"]))

        # setup plot details
        colors = cycle(['navy', 'turquoise', 'darkorange', 'cornflowerblue', 'teal'])

        plt.figure(figsize=(7, 8))
        f_scores = np.linspace(0.2, 0.8, num=4)
        lines = []
        labels = []
        for f_score in f_scores:
            x = np.linspace(0.01, 1)
            y = f_score * x / (2 * x - f_score)
            l, = plt.plot(x[y >= 0], y[y >= 0], color='gray', alpha=0.2)
            plt.annotate('f1={0:0.1f}'.format(f_score), xy=(0.9, y[45] + 0.02))

        lines.append(l)
        labels.append('iso-f1 curves')
        l, = plt.plot(recall["micro"], precision["micro"], color='gold', lw=2)
        lines.append(l)
        labels.append('micro-average Precision-recall (area = {0:0.2f})'
                      ''.format(average_precision["micro"]))

        for i, color in zip(range(n_classes), colors):
            l, = plt.plot(recall[i], precision[i], color=color, lw=2)
            lines.append(l)
            labels.append('Precision-recall for class {0} (area = {1:0.2f})'
                          ''.format(i, average_precision[i]))

        fig = plt.gcf()
        fig.subplots_adjust(bottom=0.25)
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('Recall')
        plt.ylabel('Precision')
        plt.title('Extension of Precision-Recall curve to multi-class')
        plt.legend(lines, labels, loc=(0, -.38), prop=dict(size=14))

        plt.show()

        return result_dataframe['relevance_score']

    def determine_relevance_score(self, values):
        result = 0.0
        for index in values.index:
            result = result + ( index * values[index] )
        return result