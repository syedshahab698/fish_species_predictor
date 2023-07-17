from flask import Flask, render_template, request
from predict_species import predict_species

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the user's input
    weight = float(request.form['weight'])
    length1 = float(request.form['length1'])
    length2 = float(request.form['length2'])
    length3 = float(request.form['length3'])
    height =float (request.form['height'])
    width = float(request.form['width'])

    # Make a prediction
    species = predict_species(weight, length1, length2, length3, height, width)

    return render_template('index.html', species=species)

if __name__ == '__main__':
    app.run(debug=True)
