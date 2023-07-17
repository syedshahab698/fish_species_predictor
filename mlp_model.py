from sklearn.neural_network import MLPClassifier
import numpy as np

class MLPModel:
    def __init__(self):
        self.model = MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=1000)

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)
