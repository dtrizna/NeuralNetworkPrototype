import numpy as np
import matplotlib.pyplot as plt
import scipy.io
from modules.forwardProp import L_model_forward

def load_2D_dataset(visualize=False):
    data = scipy.io.loadmat('datasets/binary_classification_2D/data.mat')
    train_X = data['X'].T
    train_Y = data['y'].T
    test_X = data['Xval'].T
    test_Y = data['yval'].T

    if visualize:
        plt.scatter(train_X[0, :], train_X[1, :], s=40, \
            c=train_Y.squeeze(), cmap=plt.cm.get_cmap("Spectral"))
        plt.show()

    return train_X, train_Y, test_X, test_Y

def predict_dec(parameters, X):
    AL, _ = L_model_forward(X, parameters)
    predictions = (AL > 0.5)
    return predictions

def plot_decision_boundary(model, X, y):
    # Set min and max values and give it some padding
    x_min, x_max = X[0, :].min() - 1, X[0, :].max() + 1
    y_min, y_max = X[1, :].min() - 1, X[1, :].max() + 1
    h = 0.01
    # Generate a grid of points with distance h between them
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    # Predict the function value for the whole grid
    Z = model(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    # Plot the contour and training examples
    plt.contourf(xx, yy, Z, cmap=plt.cm.get_cmap("Spectral"))
    plt.ylabel('x2')
    plt.xlabel('x1')
    plt.scatter(X[0, :], X[1, :], c=y, cmap=plt.cm.get_cmap("Spectral"))
    plt.show()

#load_2D_dataset(True)
#plot_decision_boundary(lambda x: predict_dec(parameters, x.T), train_X, train_Y)