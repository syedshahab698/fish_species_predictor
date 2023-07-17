import pandas as pd
from mlp_model import MLPModel
import pickle

def train_model():
    # Load the dataset
    df = pd.read_csv('Fish.csv')

    # Split the dataset into inputs and target
    X = df[['Weight', 'Length1', 'Length2', 'Length3', 'Height', 'Width']]
    y = df['Species']

    # Create and train the model
    model = MLPModel()
    model.train(X, y)

    # Save the trained model
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)

if __name__ == '__main__':
    train_model()