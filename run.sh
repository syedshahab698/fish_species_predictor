# a) Install dependencies
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

# b) Run all necessary parts of the codebase
# Train the model
python train_model.py

# Run the Flask app
FLASK_APP=app.py flask run
