import numpy as np


class MySolutions:
    """ a kNN classifier with L2 distance """

    def __init__(self, X_train, y_train, X_test):
        self.X_train_original = X_train
        self.y_train_original = y_train
        self.X_test_original = X_test
        pass

    def get_simple_logistic_reg(self):
        """
        Train the simple Logistic Regression classifier (from sklearn) with default hyperparameters.
        Return predicted class probabilities on the training and testing data.

        Returns:
            Predicted class probabilities and labels for train and test data in format:
            train_predicted_labels, train_predicted_probas, test_predicted_labels, test_predicted_probas
        """
        # some imports if needed
        ### YOUR CODE HERE    
        return labels_train, probas_train, labels_test, probas_test
    
    def get_simple_naive_bayes(self):
        """
        Train the Naive Bayes classifier with Normal distribution as a prior.
        Use sklearn version (correct one!) and default hyperparameters.
        
        Returns:
            Predicted class probabilities for train and test data.
        """
        # some imports if needed
        ### YOUR CODE HERE
        return labels_train, probas_train, labels_test, probas_test


    def get_best_solution(self):
        """
        Train your best model. You can run some preprocessing (analysing the dataset might be useful),
        normalize the data, use nonlinear model etc. Get highscore!
        Please, do not use any external libraries but sklearn and numpy.

        Returns:
            Predicted class probabilities for train and test data.
        """
        # some imports if needed
        ### YOUR CODE HERE
        return labels_train, probas_train, labels_test, probas_test
