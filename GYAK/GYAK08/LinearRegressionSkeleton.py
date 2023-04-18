import numpy as np


class LinearRegression:
    def __init__(self, epochs: int = 1000, lr: float = 1e-3):
        self.epochs = epochs
        self.lr = lr
        self.m = None
        self.c = None

    def fit(self, X: np.array, y: np.array):    #X_train, y_train lesz
        # Building the model
        m = 0
        c = 0

        L = 0.0001  # The learning Rate
        epochs = 1000  # The number of iterations to perform gradient descent

        n = float(len(X)) # Number of elements in X

        # Performing Gradient Descent 
        losses = []
        for i in range(epochs): 
            y_pred = m*X + c  # The current predicted value of Y

            residuals = y - y_pred
            loss = np.sum(residuals ** 2)
            losses.append(loss)
            D_m = (-2/n) * sum(X * residuals)  # Derivative wrt m
            D_c = (-2/n) * sum(residuals)  # Derivative wrt c
            m = m - L * D_m  # Update m
            c = c - L * D_c  # Update c
            """if i % 100 == 0:
                print(np.mean(y_train-y_pred))"""
            
        self.m = m
        self.c = c
            


    def predict(self, X):
        # Run the model on the test set
        pred = []
        for x in X:
            y_pred = self.m*x + self.c
            pred.append(y_pred)
        
        return pred
    
    def evaluate(self, X, y):
        pred = self.predict(X)
        return np.mean((pred - y)**2)

