from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_absolute_error
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.model_selection import KFold 
np.random.seed(0)
from sklearn.model_selection import validation_curve 
from sklearn.datasets import load_iris

plt.style.use('ggplot')

iris = load_iris()

X, y = iris.data, iris.target

kf = KFold (n_splits=20)
list_training_error = []
list_testing_error = []
for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    model = MLPRegressor() # We have used a multilayer perceptron (MLP) regressor model. A MLP is c
    model.fit(X_train, y_train)
    y_train_data_pred = model.predict(X_train)
    y_test_data_pred = model.predict(X_test)
    fold_training_error = mean_absolute_error(y_train, y_train_data_pred)
    fold_testing_error = mean_absolute_error(y_test, y_test_data_pred) 
    list_training_error.append(fold_training_error)
    list_testing_error.append(fold_testing_error)
  
plt.subplot (1,2,1)
plt.plot(range(1, kf.get_n_splits() + 1), np.array(list_training_error).ravel(), 'o-')
plt.xlabel('number of fold')
plt.ylabel('training error')
plt.title('Training error across folds')
plt.tight_layout()
plt.subplot(1,2,2)
plt.plot(range(1, kf.get_n_splits() + 1), np.array(list_testing_error).ravel(), 'o-')
plt.xlabel('number of fold') 
plt.ylabel('testing error')
plt.title('Testing erro across folds')
plt.tight_layout()
plt.show()
