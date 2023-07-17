import numpy as np
import pickle
from mlp_model import MLPModel

def predict_species(weight, length1, length2, length3, height, width):
    # Load the trained model
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)

    # Make a prediction
    X = np.array([weight, length1, length2, length3, height, width]).reshape(1, -1)
    prediction = model.predict(X)

    return prediction[0]
