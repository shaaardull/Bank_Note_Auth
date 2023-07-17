from flask import Flask, request
import pandas as pd
import numpy as np
import pickle5


app = Flask(__name__)

pickle_in = open('classifier.pkl', 'rb')
classifier = pickle5.load(pickle_in)


@app.route('/')
def welcome():
    return "Welcome All"


@app.route("/predict")
def predict_note_authentication():
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    
    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    
    return "The predicted value is" + str(prediction)



if __name__ == "__main__":
    app.run()