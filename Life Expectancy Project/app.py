import pickle
import numpy as np
from wsgiref import simple_server
from flask import Flask, request, app, render_template

from flask import Response
import pandas as pd
import pickle

app = Flask(__name__)
model = pickle.load(open("Life_Expectancy.sav", "rb"))
scale = pickle.load(open("scaler1.sav","rb"))

@app.route('/',methods=['GET'])
def home():
    return render_template("home.html")

@app.route("/predict", methods=['POST'])
def predict():
    float_feat = [float(x) for x in request.form.values()]
    final_feat = [np.array(float_feat)]
    prediction = model.predict(final_feat)

    return render_template("home.html",prediction_text="Life expextancy is {}%".format(prediction))
    return render_template("home.html")
if __name__ == "__main__":
    host = '0.0.0.0'
    port = 5000
    app.run(debug=True)